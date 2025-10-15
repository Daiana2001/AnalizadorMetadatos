import os
from formatos.analizador_imagen import AnalizadorImagen
from formatos.analizador_pdf import AnalizadorPDF
from formatos.analizador_audio import AnalizadorAudio

def determinar_analizador(ruta_archivo):
    extension = os.path.splitext(ruta_archivo)[1].lower()
    if extension in ['.jpg', '.jpeg', '.png', '.tiff']:
        return AnalizadorImagen()
    elif extension == '.pdf':
        return AnalizadorPDF()
    elif extension in ['.mp3', '.wav', '.ogg']:
        return AnalizadorAudio()
    else:
        raise ValueError(f"Tipo de archivo no soportado: {extension}")

def main():
    # Solicita la ruta al usuario
    ruta_archivo = input("Por favor, ingrese la ruta del archivo : ")
    
    print(f"Intentando analizar: {ruta_archivo}")
    print(f"¿El archivo existe? {os.path.exists(ruta_archivo)}")
    
    if not os.path.exists(ruta_archivo):
        print(f"Archivo no encontrado: {ruta_archivo}")
        print("Por favor, verifique la ruta e intente de nuevo.")
        return
    
    try:
        print("Determinando tipo de analizador...")
        analizador = determinar_analizador(ruta_archivo)
        print(f"Usando analizador: {type(analizador).__name__}")
        
        print("Extrayendo metadatos...")
        metadatos_unificados = analizador.extraer_metadatos(ruta_archivo)
        
        print("\n=== METADATOS UNIFICADOS ===")
        for clave, valor in metadatos_unificados.items():
            print(f"{clave}: {valor}")
        
    except Exception as e:
        print(f"Error durante el análisis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()