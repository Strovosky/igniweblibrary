from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import LibraryUser
from library.models import Book


@login_required(login_url="http://localhost:8000/login/")
def profile_view(request):
    "This function view will manage the logic of the profile page."

    if request.method == "GET":
        return render(request, "user/profile.html")



@login_required(login_url="http://localhost:8000/login/")
def delete_reserve(request, user_id, book_id):
    "This view will be in charge of getting a book out of a user reserve list."
    user = get_object_or_404(LibraryUser, pk=user_id)
    book = get_object_or_404(Book, pk=book_id)
    user.books.remove(book)
    book.available = True
    book.save()
    return render(request, "user/profile.html")


