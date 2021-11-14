import os , time

var1=0
var2=0



# FONCTION RENVOYANT LE NOMBRE DE LIGNES D'UN FICHIER TEXTE
while True:
	def countLigne1(fichier1):

		Liste1=open(fichier,'r')
		i=1
		Ligne1=Liste1.readline()
		# "Tant que la ligne n'est pas égale à "" "
		#  ==> tant qu'on est pas arrivé à la fin 
		while Ligne1!="":
			#on lit une ligne
			Ligne1=Liste1.readline()
			#on ajoute 1 à notre compteur
			i+=1
		#on retourne le compteur
		return i
		chaine_to_string1 = str(countLigne1("Generated Tokens Avancé.txt"))
		try:
			with open(f'saves/ref1.txt','r', encoding='utf-8', buffering=2**10) as fr1:
				copy1 = fr1.read()		
			var1_to_copy = str(copy1)
			var1-=int(var1_to_copy)
			var1+=int(chaine1_to_string)
			result1=str(var1)
			chaine1 = str("NORMAL: "+result1)
			print(chaine1)
			clear1 = open(f'saves/ref1.txt', 'r+')
			clear1.truncate(0) # need '0' when using r+
			clear1.close()
			pass
		except:
			chaine2_to_string_saves = str(countLigne2("Generated Tokens Avancé.txt"))
			with open(f'saves/ref2.txt','w',newline='\n', encoding='utf-8', buffering=2**10) as filehandle2:
				filehandle2.write(chaine2_to_string_saves)
	var1=0
	time.sleep(2)
	def countLigne2(fichier2):

		Liste2=open(fichier2,'r')
		i2=1
		Ligne2=Liste2.readline()
		# "Tant que la ligne n'est pas égale à "" "
		#  ==> tant qu'on est pas arrivé à la fin 
		while Ligne2!="":
			#on lit une ligne
			Ligne2=Liste2.readline()
			#on ajoute 1 à notre compteur
			i2+=1
		#on retourne le compteur
		return i2
		chaine2_to_string = str(countLigne2("Generated Tokens Avancé.txt"))
		try:
			with open(f'saves/ref2.txt','r', encoding='utf-8', buffering=2**10) as fr2:
				copy2 = fr2.read()		
			var2_to_copy = str(copy2)
			var2-=int(var2_to_copy)
			var2+=int(chaine2_to_string)
			result2=str(var2)
			chaine2 = str("NORMAL: "+result2)
			print(chaine2)
			clear2 = open(f'saves/ref2.txt', 'r+')
			clear2.truncate(0) # need '0' when using r+
			clear2.close()
			pass
		except:
			chaine2_to_string_saves = str(countLigne2("Generated Tokens Avancé.txt"))
			with open(f'saves/ref2.txt','w',newline='\n', encoding='utf-8', buffering=2**10) as filehandle2:
				filehandle2.write(chaine2_to_string_saves)
	var2=0
	time.sleep(2)



#on note que sous windows le symbole "\" doit etre doublé quand il y a certains caractères