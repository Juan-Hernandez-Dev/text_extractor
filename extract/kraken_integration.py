# src/kraken_integration.py
import subprocess
import os

def run_kraken(image_path: str, output_path: str, model_path: str):
    """
    Ejecuta el comando Kraken para procesar una imagen.
    """
    print("from kraken_integration: ", model_path)
    kraken_command = [
        'kraken', '-i', 'img/image.png', 'output/text.txt', 'binarize', 'segment', 'ocr', '--model', 'kraken/models/McCATMuS_nfd_nofix_V1.mlmodel'
    ]

    try:
        subprocess.run(kraken_command, check=True)
        print("Running command:", " ".join(kraken_command))
        print(f"Kraken ejecutado con éxito, salida en {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Kraken: {e}")
