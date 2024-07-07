from django.urls import path
from .views import create_info,read,update
urlpatterns = [
    path('create/', create_info,name='create'),
    path('read/', read,name='read'),
    path('update/<int:pk>/', update,name='update'),
]
