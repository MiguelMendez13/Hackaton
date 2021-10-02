cop=open("D:\Descargas\CPdescargatxt/CPdescarga2.txt","r")

municipios=[]
ultimo=""
contar=1000
numeros=[]

for x in cop.readlines():
    cortar=x.split("|")
    if ultimo==""or cortar[3]!=ultimo:
        ultimo=cortar[3]
        municipios.append([cortar[3],cortar[4],cortar[0]])
        numeros.append(cortar[0])
    contar+=1



contt=1
fin=99980
for muni in municipios:
    if(muni[2]=="99980"):
        pass
    else:
        muni.append(municipios[contt][2])
    contt+=1


escribir=open("cpRango.txt","w")

for x in numeros:
    escribir.writelines(x+"\n")

escribir.close()
print(municipios)