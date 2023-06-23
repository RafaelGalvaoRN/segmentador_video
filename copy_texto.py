import pyperclip
from PIL import ImageGrab
from PIL import Image
import pytesseract

#Habilita o tesseract
pytesseract.pytesseract.tesseract_cmd = r'F:\Program Files\Tesseract-OCR\tesseract.exe'

#pega imagem da área de transferência


img = ImageGrab.grabclipboard()
#Salva a imagem da área de transferência em um arquivo
img.save('arquivo.png', 'PNG')
#Lê a imagem da área de transferência
texto = pytesseract.image_to_string(Image.open('arquivo.png'), lang='por')


#retira as quebras de linha e/ou corrige texto

texto = texto.replace('\n',' ')

#Imprime o texto da imagem no editor do pycharm


print(texto)


#copia o texto para a área de transferência para ser usado prontamente
pyperclip.copy(texto)
