from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import  get_template as GetHTML
from django.shortcuts import render
import mysql.connector

def saludo(request):
	conexion = mysql.connector.connect(
		host="localhost",
		port=3306,
		user="root",
		password="",
		db="fryptotienda1"
	)
	cursor=conexion.cursor()
	cursor.execute("select database();")
	registro=cursor.fetchone()
	cursor.execute("select * from productos")
	resultados=cursor.fetchall()
	imprimir=""
	for fila in resultados:
		imprimir=imprimir+str(fila[0])+" "+str(fila[1])+" "+str(fila[2])+" "+str(fila[3])+"<br>"

	return HttpResponse("<h1>"+imprimir+"</h1>")