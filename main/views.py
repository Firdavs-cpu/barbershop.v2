from django.shortcuts import render
from .models import Service, Booking
from django.contrib import messages


def home(request):
    services = Service.objects.all()  
    if request.method == 'POST':
        service_id = request.POST["service"]
        service = Service.objects.get(id=service_id)
        name = request.POST["name"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        booking = Booking(
        name=name,
        phone=phone,
        service=service,
        date=date
    )   
        booking.save()
        messages.success(request, "Вы успешно записались")
    context = {
    'services' : services
}
    return render(request, 'main/index.html', context)

