import sys
import getopt
from functions import init, track, remove


def init_options():
	''' 
	init_options é a função responsável por tratar os argumentos de entradas do programa,
	organizando as opções, método (e chave)  e saida de acordo com as entradas.
	:return method : método utilizado na guarda da pasta 
	:return option : ação a ser desempenhada pelo programa
	:return directory : pasta onde a ação devará ser executada
	:return out :
	:return key :
	'''
	method		= None
	option 		= None
	directory 	= None
	out 		= None
	key 		= None

	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv,"i:t:x:o:", ['hash', 'hmac='])
	except getopt.GetoptError as error:
		print(error)
		opts = []
		args=[]

	for op, arg in opts:
		if op == '--hash':
			method = op
		if op == '--hmac':
			method 	= op
			key 	= arg

		if op in ('-i', '-t', '-x'):
			option 		= op
			directory	= arg
	
		if op == '-o':
			out = arg		

	if out == None:
		out = "."
	return method, option, directory, out, key



def main():
	method = None
	option = None
	directory = None
	out = None
	key = None

	method, option, directory, out, key= init_options()


	if option == '-i':
		init(method, directory, out, key)
	elif option == '-t':
		track(method, directory,out, key)
	elif option == '-x':
		if remove(directory):
			print("Programa guarda removido da pasta "+ str(directory))





main()