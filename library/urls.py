from django.urls import path
from library.views import front_page, list_books, reserve_book


urlpatterns = [
    path(route="", view=front_page, name="front_page"),
    path(route="all_books/", view=list_books, name="list_books"),
    path(route="reserve_book/<int:user_id>/<int:book_id>/", view=reserve_book, name="reserve_book")
]


