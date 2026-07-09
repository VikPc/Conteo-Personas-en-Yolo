import argparse
import time
from logging_config import logger
from detector import process_video
from exporter import save_csv


def main():

    parser = argparse.ArgumentParser(

        description="Conteo de personas mediante YOLOv8"

    )

    parser.add_argument(

        "--input",

        required=True,

        help="Ruta del video"

    )

    parser.add_argument(

        "--confidence",

        default=0.75,

        type=float,

        help="Confianza mínima"

    )

    parser.add_argument(

        "--min-frames",

        default=30,

        type=int,

        help="Frames mínimos para confirmar una persona"

    )

    args = parser.parse_args()

    start_time = time.time()

    logger.info("Iniciando procesamiento...")

    summary, confirmed_ids, output_path = process_video(

        args.input,

        confidence=args.confidence,

        min_frames=args.min_frames

    )

    save_csv(summary)
    elapsed = time.time() - start_time
    logger.info(f"Tiempo total: {elapsed:.2f} segundos")
    print("\n========== RESUMEN ==========")
    print(f"Personas únicas detectadas : {len(confirmed_ids)}")
    print(f"Video generado             : {output_path}")
    print("=============================")


if __name__ == "__main__":
    main()