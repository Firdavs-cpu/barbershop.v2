from django.shortcuts import render, redirect
from .models import Service
from django.contrib import messages
from .forms import BookingForm


def home(request):
    services = Service.objects.all()
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно записались")
            return redirect('/')
    context = {
    'services' : services,
    'form':form

}
    return render(request, 'main/index.html', context)

