from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Category
from user.models import LibraryUser


def front_page(request):
    return render(request, "library/base_template.html")


@login_required(login_url="http://localhost:8000/login/")
def list_books(request):
    books = Book.objects.filter(available=True)
    categories = Category.objects.all()
    context = {"books":books, "categories":categories}
    if request.method == "POST":
        category = request.POST.get("category")
        context["books"] = Book.objects.filter(category__name=category)
    return render(request, "library/book_list.html", context)


@login_required(login_url="http://localhost:8000/login/")
def reserve_book(request, user_id, book_id):
    user = get_object_or_404(LibraryUser, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)
    user.books.add(book)
    user.save()
    book.available = False
    book.save()
    context = {"book":book}
    return render(request, "library/book.html", context)
