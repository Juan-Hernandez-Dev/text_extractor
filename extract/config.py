# src/config.py
import os

# Rutas del proyecto
IMG_DIR = os.path.join(os.getcwd(), "img")
PREPROCESSED_DIR = os.path.join(os.getcwd(), "preprocessed")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")

# Modelo de Kraken
KRACKEN_MODEL_PATH = os.path.join(os.getcwd(), "kraken\models\McCATMuS_nfd_nofix_V1.mlmodel")
# Reemplazamos los backslashes porque la CLI está mensita
KRACKEN_MODEL_PATH = str(KRACKEN_MODEL_PATH).replace("\\", "/")