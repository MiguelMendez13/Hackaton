base=open("D:\Descargas\lel/muni.csv","r")

municipio = 0;
estados=["AGUASCALIENTES",
"BAJACALIFORNIA",
"BAJACALIFORNIASUR",
"CAMPECHE",
"COAHUILA",
"COLIMA",
"CHIAPAS",
"CHIHUAHUA",
"CIUDADDEMEXICO",
"DURANGO",
"GUANAJUATO",
"GUERRERO",
"HIDALGO",
"JALISCO",
"MEXICO",
"MICHOACAN",
"MORELOS",
"NAYARIT",
"NUEVOLEON",
"OAXACA",
"PUEBLA",
"QUERETARO",
"QUINTANAROO",
"SANLUISPOTOSI",
"SINALOA",
"SONORA",
"TABASCO",
"TAMAULIPAS",
"TLAXCALA",
"VERACRUZ",
"YUCATAN",
"ZACATECAS"]

estadosdic = {'AGUASCALIENTES': [] ,'BAJACALIFORNIA' : [],'BAJACALIFORNIASUR':[],'CAMPECHE':[] ,'COAHUILA':[],'COLIMA':[],'CHIAPAS':[],
'CHIHUAHUA':[],'CIUDADDEMEXICO':[],'DURANGO':[],'GUANAJUATO':[],'GUERRERO':[],'HIDALGO': [], 'JALISCO': [],'MEXICO': [],'MICHOACAN': [],
'MORELOS':[],'NAYARIT':[],'NUEVOLEON':[],'OAXACA':[],'PUEBLA': [],'QUERETARO':[],'QUINTANAROO': [], 'SANLUISPOTOSI': [],'SINALOA': [],
'SONORA':[],'TABASCO': [],'TAMAULIPAS': [],'TLAXCALA':[],'VERACRUZ': [],'YUCATAN':[],'ZACATECAS': []}


for linea in base.readlines():
	cortar=linea.split(',')

	municipio += 1
	print(int(cortar[2])-1)
	try:
		estadosdic[estados[int(cortar[2])-1]].append(cortar[1])
	except Exception as e:
		print(e)

for x in estadosdic:
	print(x)
	print(estadosdic[x])


