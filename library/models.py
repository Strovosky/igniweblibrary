from django.db import models



class Category(models.Model):
    "This model will have the different categories a book can have."
    
    name = models.CharField(verbose_name="name", max_length=30)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    "This model will contain all the information of a book."
    
    title = models.CharField(verbose_name="title", max_length=50)
    author = models.CharField(verbose_name="author", max_length=50)
    description = models.TextField(verbose_name="description", max_length=500)
    available = models.BooleanField(verbose_name="available", default=True)
    default_pic = models.ImageField(verbose_name="default book picture", default="default_book.png")

    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.title}"

