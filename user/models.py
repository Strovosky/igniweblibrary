from django.db.models import CharField, ImageField, BooleanField, ManyToManyField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from library.models import Book



class MyUserManager(BaseUserManager):
    """This class will specify how to create the LibraryUser."""
    
    def create_user(self, first_name, last_name, username, password):
        if not first_name:
            raise ValueError("The user must have a first name.")
        if not last_name:
            raise ValueError("The user must have a last name.")
        if not username:
            raise ValueError("The user must have a username.")
        
        user = self.model(first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, username, password):
        if not first_name:
            raise ValueError("The user must have a first name.")
        if not last_name:
            raise ValueError("The user must have a last name.")
        if not username:
            raise ValueError("The user must have a username.")
        
        user = self.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        
        return user


class LibraryUser(AbstractBaseUser, PermissionsMixin):
    """This model will create the table for the library users."""

    first_name = CharField(verbose_name="first name", max_length=70)
    last_name = CharField(verbose_name="last name", max_length=70)
    username = CharField(verbose_name="username", max_length=70, unique=True)
    profile_pic = ImageField(verbose_name="profile picture", default="default_pic.jpg")
    is_staff = BooleanField(verbose_name="is staff", default=False)
    is_active = BooleanField(verbose_name="is active", default=True)
    is_admin = BooleanField(verbose_name="is admin", default=False)
    is_superuser = BooleanField(verbose_name="is superuser", default=False)

    books = ManyToManyField(verbose_name="books", to=Book)

    objects = MyUserManager()
    
    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        "first_name", "last_name"
    ]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name()
