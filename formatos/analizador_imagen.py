from formatos.analizador_base import AnalizadorBase
from PIL import Image
from PIL.ExifTags import TAGS
import os
import datetime

class AnalizadorImagen(AnalizadorBase):
    def extraer_metadatos(self, ruta_archivo):
        try:
            imagen = Image.open(ruta_archivo)
            exif_data = imagen._getexif()
            metadatos = {
                'tamano': os.path.getsize(ruta_archivo),
                'dimensiones': f"{imagen.width} x {imagen.height}",
                'formato': imagen.format,
            }
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'DateTimeOriginal':
                        metadatos['fecha_creacion'] = value
                    elif tag == 'Artist':
                        metadatos['autor'] = value
            
            metadatos.setdefault('autor', 'Desconocido')
            metadatos.setdefault('fecha_creacion', datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo)).strftime('%Y:%m:%d %H:%M:%S'))
            metadatos.setdefault('duracion', None)
            
            return metadatos
        except Exception as e:
            raise ValueError(f"Error al extraer metadatos de imagen: {e}")