from django.shortcuts import render, HttpResponse
from .forms import NewProvision
# Create your views here.


def home(request):
    form = NewProvision()
    return render(request, 'home.html', {'form': form})
