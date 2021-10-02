base=open("D:\Descargas\datos_abiertos_covid19/211001COVID19MEXICO.csv","r")
baseLeerLinea=base.readlines()

#mujer,hombre,nospeci
sexoT=[0,0,0]

entidadResT={36:0,97:0,98:0,99:0}
municipioResT={}


for x in range(1,33):
	entidadResT[x]=0
	municipioResT[x]={}


muni=open("muncipios.txt","r")
for muni in muni.readlines():
	munItem=muni.split("\t")
	numEntidad=int(munItem[2].replace("\n",""))
	municipioResT[numEntidad]={}
	for x in range(int(munItem[0]),int(munItem[1])):
		municipioResT[numEntidad][x]=0
	municipioResT[numEntidad][999]=0


edadT={}
for x in range(0,150):
	edadT[x]=0


embarazoT=[0,0,0]
diabetisT=[]
epocT=[]
asmaT=[0,0,0]
hipertensionT=[]
cardioT=[]
obesidadT=[]
tabaquismoT=[]



for x in baseLeerLinea:
	cortar=x.split(',')
	sexo=cortar[5]
	if sexo=="1":sexoT[0]+=1
	elif  sexo=="2":sexoT[1]+=1
	elif sexo=="99":sexoT[2]+=1
	else:pass
	#-------------
	embarazo=cortar[17]
	if embarazo=="1":embarazoT[0]+=1
	elif embarazo=="2":embarazoT[1]+=1
	else:embarazoT[2]+=1


	#-------------
	asma=cortar[22]
	if asma=="1":asmaT[0]+=1
	elif asma=="2":asmaT[1]+=1
	else:asmaT[2]+=1

	entidadResT[int(cortar[7].replace('"',""))]+=1
	edadT[int(cortar[15])]+=1
	try:
		municipioResT[int(cortar[7].replace('"',""))][int(cortar[8].replace('"',""))]+=1
	except Exception as e:
		municipioResT[int(cortar[7].replace('"',""))][999]+=1






"""

	diabetisT.append(x.split(',')[20])
	epocT.append(x.split(',')[21])


	hipertensionT.append(x.split(',')[24])
	cardioT.append(x.split(',')[26])
	obesidadT.append(x.split(',')[27])
	tabaquismoT.append(x.split(',')[29])"""

print(sexoT)
print("\n\n")
print(entidadResT)
print("\n\n")
print(edadT)
print("\n\n")
print (asmaT)
print("\n\n")
print (embarazoT)
print("\n\n")
print (municipioResT)