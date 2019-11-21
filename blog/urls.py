from django.urls import path #importamos django
from blog import views #importamos la vista

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<id>', views.blog, name="blog")
]
