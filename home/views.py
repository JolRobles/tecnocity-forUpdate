from django.shortcuts import render
from django.template import Context

# Create your views here.

def mostrar_inicio(request):
	return render(request, 'index.html', {})

