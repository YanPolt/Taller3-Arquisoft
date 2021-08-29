from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.get_measurements, name='measurementList'),
    path('list/<int:pk>/', views.get_measurement_id),
    path('list/delete/<int:pk>/', views.delete_measurement_id),
    path('list/update/<int:pk>/<int:new_value>/<str:new_place>/', views.update_measurement_id),

]