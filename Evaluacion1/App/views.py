from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    '''Esta es la página principal'''
    return render(request, "index.html")

def mostrar_niveles(request):
    return render(request, 'semaforos.html')