import os
import logging

# ==========================================
# CONFIGURACIÓN DE LOGGING (NUEVO)
# ==========================================
OUTPUT_FOLDER = "assets/output"
LOGS_FOLDER = "logs"

# Aseguramos que existan las carpetas antes de que los otros módulos las usen
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(LOGS_FOLDER, exist_ok=True)

# Configuración global del sistema de registro
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOGS_FOLDER, "app.log"), encoding="utf-8"),
        logging.StreamHandler()  # Esto hace que también se vea en la terminal
    ]
)

# Este es el objeto que importarán los demás archivos para registrar eventos
logger = logging.getLogger("people_counter")


# ==========================================
# CONFIGURACIÓN DEL MODELO Y DETECCIÓN
# ==========================================

# Modelo YOLO
MODEL_PATH = "yolov8n.pt"

# Tracker
TRACKER = "botsort.yaml"

# Clases a detectar (0 = persona)
CLASSES = [0]

# Umbral mínimo de confianza
CONFIDENCE_THRESHOLD = 0.75

# Frames mínimos para confirmar una persona
MIN_FRAMES_CONFIRMATION = 30