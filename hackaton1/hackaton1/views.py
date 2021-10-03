from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import  get_template as GetHTML
from django.shortcuts import render
import mysql.connector

def saludo(request):


	return HttpResponse("<h1>Hola</h1>")