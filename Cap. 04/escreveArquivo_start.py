#
# Escrevendo arquivos com funções do Python
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def EscreveArquivo():
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.white("Linha gerada com a função 'EscreveArquivo' \r\n")

    arquivo.close()
EscreveArquivo()

def AlteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.white("Linha gerada com a função 'EscreveArquivo' \r\n")

    arquivo.close()
AlteraArquivo()
