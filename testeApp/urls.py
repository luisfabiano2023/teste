
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_info,name='create'),
    path('read/', views.delete_info,name='read'),
    path('update/<int:pk>/', views.update_info,name='update'),
]
