from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required 

@login_required
def persons_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)
    
    # nome e sobrenome
    # nome ou sobrenome
    if nome or sobrenome:
            persons = Person.objects.filter(
                  Q(nome__icontains=nome) | Q(sobrenome__icontains=sobrenome)
            )
            
    else:
            persons = Person.objects.all()
    
    return render(request, 'clientes/person.html', {'persons': persons})

@login_required
def person_new(request):
    # envia form novo
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:person_list')
    
    return render(request, 'clientes/person_form.html', {'form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('clientes:person_list')
    
    return render(request, 'clientes/person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    
    if request.method =='POST':
       person.delete()
       return redirect('clientes:person_list')
   
    return render(request, 'clientes/person_delete_confirm.html',  {'person': person})



