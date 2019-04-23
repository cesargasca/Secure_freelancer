from django.urls import path

from apps.sf import views

app_name = 'sf'
urlpatterns = [
    path('index.html/', views.index, name='index'),
]