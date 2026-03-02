from django.shortcuts import render,get_object_or_404

from product.models import Car


# Create your views here.

def product(request):
    return render(request, 'product.html')



def next_to_page(request):
    cars = Car.objects.all()
    context = {
        'cars':cars
    }
    return render(request, 'next_page.html', context)




def car_dateil(request, id):
    car = get_object_or_404(Car, id=id)


    context = {
        'car': car
    }
    return  render(request, 'car_dateil.html', context)
