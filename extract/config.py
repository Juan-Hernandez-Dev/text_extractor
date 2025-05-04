# src/config.py
import os
from clean_path import clean_path

# Rutas del proyecto
IMG_DIR = "img"
PREPROCESSED_DIR = "preprocessed"
OUTPUT_DIR = "output"

# Modelo de Kraken
KRACKEN_MODEL_PATH = os.path.join(os.getcwd(), "kraken\models\McCATMuS_nfd_nofix_V1.mlmodel")
# Reemplazamos los backslashes porque la CLI está mensita
KRACKEN_MODEL_PATH = clean_path(KRACKEN_MODEL_PATH)