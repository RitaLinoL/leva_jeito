import os, shutil
import hashlib, hmac
from BTrees.OOBTree import OOBTree



def init(method, directory,out, key):
	path = None
	try:		
		path_guarda = str(directory) +".guarda/"

		#se já existir programa guarda : apaga
		if os.path.isdir(path_guarda):
			remove(str(directory) +"/.guarda/")

		os.makedirs(str(directory) +"/.guarda")

		guarda = open(path_guarda +"guarda.txt", "w+")	
		guarda.close()
		
		guarda_tree = OOBTree()

		for i in os.listdir(directory):
			if i == ".guarda":
				continue

			if method == '--hash':
				hasher = hashlib.sha1()
			elif method == '--hmac':
				hasher = hmac.new(key.encode(), digestmod=hashlib.sha1)
			if (os.path.isfile(directory+i)):
				print(i)
				with open(directory+i, 'rb') as node:
					buf = None
					buf = node.read()
					hasher.update(buf)
				guarda_tree.update({i:hasher.hexdigest()})
				continue
			if (os.path.isdir(directory+i)):
				guarda_tree.update({i:create_hash_dir(i, directory, method, key, directory+".guarda/")})
		
		tree_to_file("guarda", directory, directory+".guarda/", guarda_tree)

	except OSError as error:
		print(error)


def create_hash_dir(name, directory, method, key, root_guarda):
	dir_tree = OOBTree()

	path  = directory+name+"/"
	for i in os.listdir(path):
		if i == ".guarda":
			continue

		if method == '--hash':
			hasher = hashlib.sha1()
		elif method == '--hmac':
			hasher = hmac.new(key.encode(), digestmod=hashlib.sha1)

		if (os.path.isfile(path+i)):
			with open(path+i, 'rb') as node:
				buf = None
				buf = node.read()
				hasher.update(buf)
			dir_tree.update({i:hasher.hexdigest()})
			continue

		if (os.path.isdir(path+i)):
			dir_tree.update({i:create_hash_dir(i, path, method, key, root_guarda)})
	return dir_tree



def tree_to_file(name,directory, root_guarda, tree):
	file = open(root_guarda+name+".txt", "w+")
	for k in tree.keys():
		if os.path.isfile(directory+k):
			file.write(k+"\t"+tree[k]+"\n")
		if type(tree[k]) == type(OOBTree()):
			file.write(k+"\tdir\n")
			tree_to_file(k, directory+k+"/", root_guarda, tree[k])
	file.close()

def file_to_tree(name, directory, root_guarda, file):
	file = open(,"r")



	return tree


	
def track(method, directory,out, key):
	os.makedirs(directory+".tmp/")
	

	remove(directory+".tmp/")


def remove(directory):
	try:		
		for i in os.listdir(directory):
		    os.remove(os.path.join(directory, i))
		os.rmdir(directory) # Now the directory is empty of files	
		return True
	except OSError as error:
		print(error)
		return False



