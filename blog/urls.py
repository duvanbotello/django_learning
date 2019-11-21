from django.urls import path #importamos django
from blog import views #importamos la vista

urlpatterns = [
    path('', views.blog, name="blog")
]
