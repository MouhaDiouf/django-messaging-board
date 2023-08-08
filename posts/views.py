from django.views.generic import ListView

from .models import Post

# Create your views here.

class HomePage(ListView):
    template_name = "home.html"
    model = Post