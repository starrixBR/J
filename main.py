import pathlib

from tarefas import *

HOME = pathlib.Path(__file__).parent.resolve()

SEMENTES = ['https://www.bbc.com/culture/article/20250415-jmw-turner-at-250-why-his-greatest-painting-the-fighting-temeraire-is-so-misunderstood']
#['https://www.bbc.com/news/articles/cqj77pgyq81o']


def raspa_paginas():
	cria_diretorios(HOME, diretorios = 'html textos'.split())
	markups = visita_paginas(SEMENTES, 'textos')
	
	


def faz_glossario():
	diretorio = os.path.join('textos')
	nomes = os.listdir(diretorio)
	for nome in nomes:
		#print(f'Arquivo: {nome}')
		floc = os.path.join(diretorio, nome)
		texto = ler_arquivo(floc)
		lista = []
		for word in texto.split():
			if word not in lista:
				lista.append(word)
				#print(word)
				
		for palavra in sorted(lista):
			print(palavra)
				
	#arq = open('glossario.txt', 'w')
	#arq.write(str(lista))
	#arq.close()
	
	return lista 
	
def conta_frequencia(): 
	diretorio = os.path.join('textos')
	nomes = os.listdir(diretorio)
	frequencia = {}
	for nome in nomes:
		floc = os.path.join(diretorio, nome)
		texto = ler_arquivo(floc)
		for palavra in texto.lower().split():
			palavra = palavra.strip(',.!?:;][')
			if palavra in frequencia:
				frequencia[palavra] += 1
			else:
				frequencia[palavra] = 1
				
	palavras_ordenadas = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
	 
	for palavra, contagem in palavras_ordenadas:
		print(f'{palavra}: {contagem}')
	
def ler_glossario(floc):
	arq = open(floc, 'r')
	conteudo = arq.read()
	arq.close()
	
	print(conteudo)
	
	
#raspa_paginas()

conta_frequencia()


