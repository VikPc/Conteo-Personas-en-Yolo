import os
import cv2

from config import OUTPUT_FOLDER


def initialize_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception(f"No se pudo abrir el video: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 30

    fps = int(fps)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    video_name = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"{video_name}_tracking.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    print("\n========== VIDEO ==========")
    print(f"Resolución : {width}x{height}")
    print(f"FPS        : {fps}")
    print(f"Salida     : {output_path}")
    print("===========================\n")

    return cap, out, output_path