from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpView(UserCreationForm):
    pass
