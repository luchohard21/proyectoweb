from django.shortcuts import render

# Create your views here.
#vista pagina 1
def inicio(request):
    return render(request, 'app/inicio.html')

#vista pagina 2
def quienesomos(request):
    return render(request, 'app/quienesomos.html')

#vista pagina 3    
def servicios(request):
    return render(request, 'app/servicios')

#vista pagina 4
def reservatuhora(request):
    return render(request, 'reservatuhora.html')

#vista pagina 5
def contactanos(request):
    return render(request, 'app/contactanos.html')

#vista pagina 6
def dejanostuopinion(request):
    return render(request, 'app/dejanostuopinion.html')    