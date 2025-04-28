# src/main.py
import os
from preprocess import enhance_contrast
from kraken_integration import run_kraken
from config import IMG_DIR, PREPROCESSED_DIR, OUTPUT_DIR, KRACKEN_MODEL_PATH

def main():
    # Rutas de las imágenes
    input_image_path = os.path.join(IMG_DIR, "image.png")
    preprocessed_image_path = os.path.join(PREPROCESSED_DIR, "input_contrast.png")
    output_text_path = os.path.join(OUTPUT_DIR, "test.txt")

    # Preprocesar imagen
    enhance_contrast(input_image_path, preprocessed_image_path)

    # Ejecutar Kraken
    run_kraken(preprocessed_image_path, output_text_path, KRACKEN_MODEL_PATH)

if __name__ == "__main__":
    main()