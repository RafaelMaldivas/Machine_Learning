from colorama import init
import pydf
from colorama import Fore, Back, Style
from termcolor import colored

init()

print(Fore.RED + 'Vermelho é uma cor surpreendente!')
print(Fore.MAGENTA + 'E acabou os meus problemas com cores no terminal')
print(Back.GREEN + 'Legalize iT')
print(Style.BRIGHT + 'O brilho de toda manhã ensolarada')
print(Fore.BLUE, Style.BRIGHT, Back.LIGHTYELLOW_EX + "Descobrindo nesse curso coisas bem legais")
print(Style.RESET_ALL)
print('Voltando ao normal !!')
print(colored('Hoje eu acordei para sorrir mostrar os dentes...', 'blue', 'on_red'))
print(colored('Hello, World!', 'red', 'on_grey'))


pdf = (
    '<h1>Legalize a Maconha</h1><br/><p>A Maconha vem sendo criminalizada há muitos anos como forma'
    'de punir os negros, pois é parte da cultura desses povos o uso de cannabis sativa, sendo assim'
    'é totalmente esquecido que a planta não serve apenas para recreação e ficar chapado, mas também'
    ' é um potente remédio contra doenças como asma, glaucoma, entre outras moléstias</p>')

with open('teste_doc.txt', 'r') as f:
    f.write(pdf)
