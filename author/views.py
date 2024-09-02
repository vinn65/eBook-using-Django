from django.shortcuts import redirect, render

from .forms import AuthorForm
from .models import Author
# Create your views here.

def index(request):
    authors = Author.objects.all()
    return render(request,'author/index.html',{
        'authors':authors
    })


def detail(request,pk):
    author = Author.objects.get(pk=pk)
    
    return render(request, 'author/author.html',{
        'author':author
    })

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('author:index')
    else:
        form = AuthorForm()
    return render(request,'author/add.html',{
        'form':form
    })