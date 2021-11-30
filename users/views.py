from django.shortcuts import render
from .models import Usuario

# Create your views here.
def usuariolist(request):
    getUsuarios = Usuario.objects.all()
    
    data = {
        'getUsuarios': getUsuarios,
    }
    return render(request, 'usuariolist.html', data)
    