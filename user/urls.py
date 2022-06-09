from django.urls import path
from .views import CreateView, ReadView, HomeView

urlpatterns = [
    path('create', CreateView.as_view()),
    path('read', ReadView.as_view()),
    path('home', HomeView.as_view()),
]