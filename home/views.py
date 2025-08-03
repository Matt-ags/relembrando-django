from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def home(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        user = Usuario(nome=nome)
        user.save()
        return redirect('/home/')

    busca = request.GET.get('busca')  
    if busca:
        usuarios = Usuario.objects.filter(nome__icontains=busca)
    else:
        usuarios = Usuario.objects.all()

    return render(request, 'home.html', {'usuarios': usuarios})

        
def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('/home/')

