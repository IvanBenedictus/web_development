from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

# Create your forms here
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
       model = User
       fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
