from ultralytics import YOLO
import cv2
from tqdm import tqdm

from utils import initialize_video
from config import (
    MODEL_PATH,
    TRACKER,
    CLASSES,
    CONFIDENCE_THRESHOLD,
    MIN_FRAMES_CONFIRMATION,
)


def process_video(
    video_path,
    confidence=CONFIDENCE_THRESHOLD,
    min_frames=MIN_FRAMES_CONFIRMATION,
):
    """
    Procesa un video utilizando YOLOv8 y BoT-SORT para detectar,
    rastrear y contar personas.

    Args:
        video_path (str): Ruta del video de entrada.
        confidence (float): Umbral mínimo de confianza para aceptar una detección.
        min_frames (int): Cantidad mínima de frames para confirmar una persona.

    Returns:
        tuple:
            summary (list): Lista con todas las detecciones.
            confirmed_ids (set): IDs únicos confirmados.
            output_path (str): Ruta del video procesado.
    """

    # Cargar modelo YOLO
    model = YOLO(MODEL_PATH)

    # Inicializar video de entrada y salida
    cap, out, output_path = initialize_video(video_path)

    # Obtener número total de frames para la barra de progreso
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Variables de seguimiento
    summary = []
    confirmed_ids = set()
    id_frames = {}

    # Inicializar tracking
    results = model.track(
        source=video_path,
        stream=True,
        show=False,
        save=False,
        tracker=TRACKER,
        persist=True,
        classes=CLASSES,
    )

    try:

        for frame_idx, result in enumerate(
            tqdm(
                results,
                total=total_frames,
                desc="Procesando video",
                unit="frame",
            )
        ):

            frame = result.orig_img

            if result.boxes.id is not None:

                boxes = result.boxes.xyxy.cpu().numpy()
                ids = result.boxes.id.cpu().numpy().astype(int)
                confs = result.boxes.conf.cpu().numpy()

                for box, track_id, conf in zip(boxes, ids, confs):

                    # Ignorar detecciones de baja confianza
                    if conf < confidence:
                        continue

                    x1, y1, x2, y2 = map(int, box)

                    # Contabilizar frames vistos por cada persona
                    id_frames[track_id] = id_frames.get(track_id, 0) + 1

                    # Confirmar persona cuando supera el mínimo de frames
                    if id_frames[track_id] >= min_frames:
                        confirmed_ids.add(track_id)

                    # Dibujar bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2,
                    )

                    # Etiqueta
                    label = f"Persona {track_id} | {conf:.2f}"

                    cv2.putText(
                        frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2,
                    )

                    # Guardar información para exportar posteriormente
                    summary.append(
                        {
                            "frame": frame_idx,
                            "id_persona": track_id,
                            "confianza": round(float(conf), 4),
                        }
                    )

            # Mostrar contador de personas únicas confirmadas
            cv2.putText(
                frame,
                f"Total Personas: {len(confirmed_ids)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3,
            )

            # Escribir frame procesado
            out.write(frame)

    finally:
        # Liberar recursos aunque ocurra un error
        cap.release()
        out.release()

    return summary, confirmed_ids, output_path