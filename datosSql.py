base=open("D:\Descargas\datos_abiertos_covid19/211001COVID19MEXICO.csv","r")
baseLeerLinea=base.readlines()

#mujer,hombre,nospeci
sexoT=[0,0,0]
entidadResT=[]
municipioResT=[]
edadT=[]
embarazoT=[]
diabetisT=[]
epocT=[]
asmaT=[]
hipertensionT=[]
cardioT=[]
obesidadT=[]
tabaquismoT=[]



for x in baseLeerLinea:


	sexo=x.split(',')[5]
	if sexo=="1":
		sexoT[0]+=1
	elif  sexo=="2":
		sexoT[1]+=1
	elif sexo=="99":
		sexoT[2]+=1



	"""entidadResT.append(x.split(',')[7])
	municipioResT.append(x.split(',')[8])
	edadT.append(x.split(',')[15])
	embarazoT.append(x.split(',')[17])
	diabetisT.append(x.split(',')[20])
	epocT.append(x.split(',')[21])
	asmaT.append(x.split(',')[22])
	hipertensionT.append(x.split(',')[24])
	cardioT.append(x.split(',')[26])
	obesidadT.append(x.split(',')[27])
	tabaquismoT.append(x.split(',')[29])"""

print(sexoT)

