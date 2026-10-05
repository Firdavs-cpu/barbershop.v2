from django.shortcuts import render
from .models import Service


def home(request):
    services = Service.objects.all()
    context = {
    'services' : services
}
    return render(request, 'main/index.html', context)

