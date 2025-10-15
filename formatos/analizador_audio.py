# formatos/analizador_audio.py
from formatos.analizador_base import AnalizadorBase
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os
import datetime

class AnalizadorAudio(AnalizadorBase):
    def extraer_metadatos(self, ruta_archivo):
        try:
            audio = mutagen.File(ruta_archivo, easy=True)
            metadatos = {
                'tamano': os.path.getsize(ruta_archivo),
            }
            
            if audio:
                metadatos['autor'] = audio.get('artist', ['Desconocido'])[0]
                metadatos['titulo'] = audio.get('title', ['Desconocido'])[0]
                # Para duración, usa MP3 específico si es mp3
                if ruta_archivo.lower().endswith('.mp3'):
                    mp3 = MP3(ruta_archivo)
                    metadatos['duracion'] = mp3.info.length  # en segundos
                
                # Fecha de creación desde tags o filesystem
                metadatos['fecha_creacion'] = audio.get('date', [datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo)).strftime('%Y:%m:%d %H:%M:%S')])[0]
            
            # Asegura claves unificadas
            metadatos.setdefault('dimensiones', None)
            metadatos.setdefault('duracion', None)
            
            return metadatos
        except Exception as e:
            raise ValueError(f"Error al extraer metadatos de audio: {e}")