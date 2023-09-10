import pytesseract
import cv2

# Carregar uma imagem
imagem = cv2.imread("imagem.png")

caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd =  caminho_tesseract

texto_extraido_da_imagem = pytesseract.image_to_string(imagem, lang="eng")

print(texto_extraido_da_imagem)