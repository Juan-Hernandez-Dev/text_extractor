# src/preprocess.py
from PIL import Image, ImageEnhance
import os

def enhance_contrast(image_path: str, output_path: str, factor: float = 2.0):
    """
    Mejora el contraste de una imagen y la guarda en la ruta de salida.
    """
    img = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)
    img.save(output_path)
    print(f"Imagen procesada y guardada en {output_path}")
