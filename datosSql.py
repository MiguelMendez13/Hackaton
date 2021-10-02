base=open("D:\Descargas\datos_abiertos_covid19/211001COVID19MEXICO.csv","r")
baseLeerLinea=base.readlines()

#mujer,hombre,nospeci
sexoT=[0,0,0]

entidadResT={36:0,97:0,98:0,99:0}
for x in range(1,33):
	entidadResT[x]=0


municipioResT=[]


edadT={}
for x in range(0,150):
	edadT[x]=0


embarazoT=[]
diabetisT=[]
epocT=[]
asmaT=[]
hipertensionT=[]
cardioT=[]
obesidadT=[]
tabaquismoT=[]



for x in baseLeerLinea:
	cortar=x.split(',')
	sexo=cortar[5]
	if sexo=="1":
		sexoT[0]+=1
	elif  sexo=="2":
		sexoT[1]+=1
	elif sexo=="99":
		sexoT[2]+=1
	else:
		pass
	#-------------
	entidadResT[int(cortar[7].replace('"',""))]+=1
	edadT[int(cortar[15])]+=1





"""
	municipioResT.append(x.split(',')[8])

	embarazoT.append(x.split(',')[17])
	diabetisT.append(x.split(',')[20])
	epocT.append(x.split(',')[21])
	asmaT.append(x.split(',')[22])
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

