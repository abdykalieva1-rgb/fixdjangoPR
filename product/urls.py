from django.urls import path
from .views import product, next_to_page, car_dateil

urlpatterns = [
    path('', product, name='product'),
    path('next_to_page/', next_to_page, name='next_to_page'),
    path('car_dateil/<int:id>/', car_dateil, name='car_dateil'),

]

