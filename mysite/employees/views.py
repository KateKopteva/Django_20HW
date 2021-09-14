from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *
from .models import *

menu = [
        {'title': "Добавить запись", 'url_name': 'add_new_page'}
        ]


def index(request):
    posts = Employees.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'employees/index.html', context=context)


def addpage(request, post_id):
    post = get_object_or_404(Employees, pk=post_id)
    if request.method == "POST":
        form = AddForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddForm(instance=post)
        context = {
            'form': form,
            'id':post.id,
        }
        return render(request, 'employees/addpage.html', context=context)



def addnewpage(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddForm()
        context = {
            'form': form
        }
        return render(request, 'employees/addnewpage.html', context=context)


def delete_e(request, post_id):
    post = Employees.objects.get(pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    else:
        return render(request,'employees/delete.html')
