from abc import ABC, abstractmethod

class AnalizadorBase(ABC):
    @abstractmethod
    def extraer_metadatos(self, ruta_archivo):
        """
        Extrae metadatos del archivo y los devuelve en un formato unificado.
        El formato unificado es un diccionario con claves comunes como:
        - 'autor': Autor o creador
        - 'fecha_creacion': Fecha de creación
        - 'tamano': Tamaño del archivo
        - 'dimensiones': Para imágenes o similares (ancho x alto)
        - 'duracion': Para audio/video
        - Y otras específicas según el tipo, pero mapeadas a claves comunes cuando sea posible
        """
        pass