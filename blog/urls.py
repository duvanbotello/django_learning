from django.urls import path #importamos django
from . import views #importamos la vista

urlpatterns = {
    path('', views.blog, name="blog")
}