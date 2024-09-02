from django.shortcuts import render, redirect

from book.models import Book
from . forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'book/books.html',{
        'books':books
    })

def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    else:
        form = BookForm()
    return render(request,'book/add.html',{
        'form':form
    })
