from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.Create.as_view(), name='Create'),
    path('results/<int:pk>/', views.Results.as_view(), name='results'),
]