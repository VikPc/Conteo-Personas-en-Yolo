# Conteo de Personas con YOLOv8

Sistema de detección, seguimiento y conteo de personas utilizando **YOLOv8**, **BoT-SORT** y **OpenCV**. El proyecto procesa un video de entrada, identifica personas de forma única mediante tracking y genera un video anotado junto con un archivo CSV con las detecciones realizadas.

## Características

- Detección de personas mediante YOLOv8.
- Seguimiento de objetos con BoT-SORT.
- Conteo de personas únicas.
- Exportación de resultados a CSV.
- Generación de un video procesado con las detecciones.
- Ejecución desde línea de comandos.

## Tecnologías

- Python 3
- YOLOv8 (Ultralytics)
- OpenCV
- Pandas
- NumPy

## Estructura del proyecto

```
Conteo-Personas-en-Yolo/
│
├── src/
│   ├── config.py
│   ├── detector.py
│   ├── exporter.py
│   ├── logging_config.py
│   ├── main.py
│   └── utils.py
│
├── assets/
│   ├── input/
│   └── output/
│
├── logs/
├── requirements.txt
└── .gitignore
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/VikPc/Conteo-Personas-en-Yolo.git
cd Conteo-Personas-en-Yolo
```

Crear un entorno virtual:

```bash
python -m venv env
```

Activarlo:

**Windows**

```bash
env\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Coloque el video de entrada dentro de:

```
assets/input/
```

Ejecute:

```bash
python src/main.py --input assets/input/video.mp4
```

## Salida

Al finalizar el procesamiento se generan:

- Video procesado con las detecciones.
- Archivo CSV con las detecciones registradas.
- Resumen de la ejecución en consola.

## Próximas mejoras

- Estadísticas de rendimiento.
- Optimización del procesamiento.
- Mejora de la documentación.

## Licencia

Este proyecto fue desarrollado con fines académicos y de aprendizaje.
