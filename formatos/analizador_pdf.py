# formatos/analizador_pdf.py
from formatos.analizador_base import AnalizadorBase
import PyPDF2
import os
import datetime

class AnalizadorPDF(AnalizadorBase):
    def extraer_metadatos(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'rb') as archivo_pdf:
                lector = PyPDF2.PdfReader(archivo_pdf)
                info = lector.metadata
                
                metadatos = {
                    'tamano': os.path.getsize(ruta_archivo),
                    'num_paginas': len(lector.pages),
                }
                
                if info:
                    metadatos['autor'] = info.author if info.author else 'Desconocido'
                    metadatos['fecha_creacion'] = info.creation_date.strftime('%Y:%m:%d %H:%M:%S') if info.creation_date else datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo)).strftime('%Y:%m:%d %H:%M:%S')
                    metadatos['titulo'] = info.title
                
                # Asegura claves unificadas
                metadatos.setdefault('dimensiones', None)  # No aplica típicamente
                metadatos.setdefault('duracion', None)
                
                return metadatos
        except Exception as e:
            raise ValueError(f"Error al extraer metadatos de PDF: {e}")