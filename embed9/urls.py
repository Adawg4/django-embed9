from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from embed9 import views

urlpatterns = [
    path('widget/<app>/<model>/<pk>/', views.widget, name='widget'),
    path('loader/<app>/<model>/<pk>/', views.loader, name='loader'),
    path('preview/<app>/<model>/<pk>/', csrf_exempt(views.preview), name='preview'),
]
