import os
from preprocess import enhance_contrast
from kraken_integration import run_kraken
from config import IMG_DIR, PREPROCESSED_DIR, OUTPUT_DIR, KRACKEN_MODEL_PATH

def main():
    # Crear carpetas si no existen
    os.makedirs(PREPROCESSED_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Iterar sobre todas las imágenes en IMG_DIR
    for file in os.listdir(IMG_DIR):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            print(f"[INFO] Procesando: {file}")

            input_image_path = os.path.join(IMG_DIR, file)
            print("from main, input path: ", input_image_path)
            filename_wo_ext = os.path.splitext(file)[0]
            preprocessed_image_path = os.path.join(PREPROCESSED_DIR, f"{filename_wo_ext}_contrast.png")
            output_text_path = os.path.join(OUTPUT_DIR, f"{filename_wo_ext}.txt")

            # Preprocesar imagen
            enhance_contrast(input_image_path, preprocessed_image_path)

            # Ejecutar Kraken
            run_kraken(preprocessed_image_path, output_text_path, KRACKEN_MODEL_PATH)

            print(f"[OK] Guardado: {output_text_path}")

if __name__ == "__main__":
    main()