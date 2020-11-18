from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.UserAppListView.as_view()),
    path('profile/<int:pk>/', views.UserAppView.as_view({'post': 'create', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

