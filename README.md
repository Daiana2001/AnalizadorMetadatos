## Descripción
AnalizadorMetadatos es un proyecto en Python que permite extraer metadatos unificados de diferentes tipos de archivos, incluyendo imágenes (.jpg, .png, .tiff), documentos PDF y archivos de audio (.mp3, .wav, .ogg). El programa utiliza una estructura de clases para analizar cada tipo de archivo y devuelve los metadatos en un formato común, facilitando su uso para futuros procesamientos o análisis.

## Características
- Extracción de metadatos de imágenes (tamaño, dimensiones, autor, fecha, etc.).
- Extracción de metadatos de PDFs (autor, fecha de creación, número de páginas, etc.).
- Extracción de metadatos de archivos de audio (autor, título, duración, etc.).
- Interfaz de entrada por teclado para especificar la ruta del archivo.
- Estructura modular con soporte para agregar nuevos tipos de archivos.

## Requisitos
- Python 3.13 o superior.
- Bibliotecas:
  - `pillow` (para imágenes)
  - `PyPDF2` (para PDFs)
  - `mutagen` (para audios)
- Entorno virtual (recomendado).
