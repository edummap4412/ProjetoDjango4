from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ProdutoModelForm, EmailContato
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html',context)




def produto(request):
    if str(request.user) != "AnonymousUser":
        form = ProdutoModelForm(request.POST, request.FILES)
        if str(request.method) == 'POST':
            if form.is_valid():
                form.save()

                form = ProdutoModelForm()
                messages.success(request, 'Produto salvo com sucesso')

            else:
                messages.error(request, 'Erro ao salvar produtos.')

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def contato(request):
    form= EmailContato(request.POST or None)
    if str(request.method) =='POST':
        if form.is_valid():
            form.save()
            messages.success("Email enviado com sucesso.")
            form =EmailContato()
    context = {
        'formulario': form
    }
    return render(request, 'contato.html',context)
