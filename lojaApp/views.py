from django.shortcuts import render, redirect, get_object_or_404
from .forms import SorveteForm, sorvete, comentario, ComentarioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Comentarios

def cadastrarComentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarComentario')
    else:
        form = ComentarioForm()
    return render(request, 'lojaApp/feedback.html', {
        'titulo': 'Cadastrar Novo Comentario',
        'form': form,
    })

def listarComentario(request):
    return render(request, 'lojaApp/feedback_list.html', {
        'titulo': 'Lista de Comentarios',
        'lista': comentario.objects.all(),
    })

@login_required
def editarComentario(request, pk):
    obj = get_object_or_404(comentario, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listarComentario')
    else:
        form = ComentarioForm(instance=obj)
    return render(request, 'lojaApp/form_comentario.html', {
        'titulo': f'Editar Comentario: {obj}',
        'form': form,
    })

@login_required
def excluirComentario(request, pk):
    obj = get_object_or_404(comentario, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listarComentario')
    return render(request, 'lojaApp/model_delete.html', {
        'titulo': 'Excluir Comentario',
        'objeto': obj,
        'url_cancelar': 'listarComentario',
    })
# Index


def index(request):
    return render(request, 'lojaApp/index.html')

# Cardápio


def cardapio(request):
    return render(request, 'lojaApp/cardapio.html', {
        'titulo': 'Cardápio',
        'sorvetes': sorvete.objects.all(),
    })

# Sorvete
       
def listarSorvete(request):
    return render(request, 'lojaApp/model_list.html', {
        'titulo': 'Lista de Sorvetes',
        'lista': sorvete.objects.all(),
        'criar_url': 'cadastrarSorvete',
        'editar_url': 'editarSorvete',
        'excluir_url': 'excluirSorvete',
    })

@login_required
def cadastrarSorvete(request):
    if request.method == 'POST':
        # Adicione request.FILES aqui
        form = SorveteForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('listarSorvete')
    else:
        form = SorveteForm()
    return render(request, 'lojaApp/form_sorvete.html', {'form': form}
                  )

@login_required
def editarSorvete(request, pk):
    obj = get_object_or_404(sorvete, pk=pk)
    if request.method == 'POST':
        form = SorveteForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listarSorvete')
    else:
        form = SorveteForm(instance=obj)
    return render(request, 'lojaApp/form_sorvete.html', {
        'titulo': f'Editar Sorvete: {obj}',
        'form': form,
    })

@login_required
def excluirSorvete(request, pk):
    obj = get_object_or_404(sorvete, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listarSorvete')
    return render(request, 'lojaApp/model_delete.html', {
        'titulo': 'Excluir Sorvete',
        'objeto': obj,
        'url_cancelar': 'listarSorvete',
    })

# Autenticação

def cadastrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'lojaApp/cadastrarUsuario.html', {
        'titulo': 'Cadastrar Usuário',
        'form':form,
        })

    # Galeria
def galeria(request):
    sorvete_list = sorvete.objects.all()
    return render(request, 'lojaApp/galeria.html', {'sorvetes': sorvete_list})