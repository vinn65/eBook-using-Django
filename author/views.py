from django.shortcuts import redirect, render, get_object_or_404

from .forms import AuthorForm
from .models import Author
# Create your views here.

def index(request):
    authors = Author.objects.all()
    return render(request,'author/index.html',{
        'authors':authors
    })


def detail(request,pk):
    author = get_object_or_404(Author, pk=pk)

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