import subprocess
from PIL import Image, ImageEnhance

# Mejorar el contraste
img = Image.open('img/input.png')
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2.0)
img.save('output/img/input_contrast.png')

kraken_command = [
    'kraken', '-i', 'output/img/input_contrast.png', 'output/txt/test.txt', 'binarize', 'segment', 'ocr', '--model', 'kraken/models/McCATMuS_nfd_nofix_V1.mlmodel'
]

# Ejecutar el comando Kraken
subprocess.run(kraken_command)