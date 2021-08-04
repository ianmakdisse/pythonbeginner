import os, shutil
#arquivo atual
print("Arquivo atual",__file__)
#nome do arquivo atual
print(os.path.basename(__file__))
#pasta do arquivo atual
print(os.path.dirname(__file__))
#caminho absoluto do arquivo
print(os.path.abspath(__file__))
#lista os arquivos presentes em um diretorio os.listdir()
print(os.listdir())
#para criar um arquivo os.mkdir("caminho"), não funciona com recursividade
#para criar diretorio e sub diretorios os.makdirs()
#os.mkdir("teste00.py")

#renomear um arquivo os.rename() mando minha source e meu destino
#também conseguimos mover o arquivo com o comando rename
#os.rename('teste00.py\\arquivo.txt','teste00.py\\arquivo2.txt')

#conseguimos copiar pastas com a biblioteca shuttil
#shuttil.copy2(source,destiny)

#para copiar um diretorio inteiro podemos utilizar from distulis.dir_util import copy_trees
#para isso iremos enviar dois parametros copy_tree(source,destiny)

#deletando arquivo, não pode executar com pastas
#os.remove("teste00.py\\arquivo2.txt")

#para pastas os.removedirs(), detalhe não funciona para pastas cheias
#os.removedirs("teste00.py")
#shuttil.rmtree() remove as pastas de qualquer forma
#os.mkdir("desafio")
#os.path.isfile() para checar se o arquivo existe

if not (os.path.isdir("desafio")):
    os.mkdir("desafio")
if not (os.path.isdir("desafio\\teste")):
    os.mkdir("desafio\\teste")


#para criar um novo arquivo open("desafio\\arquivo.txt",'w') para escrever do zero
#open("desafio\\arquivo.txt",'a') para acresentar em um arquivo ja existente