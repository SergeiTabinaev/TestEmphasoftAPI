from django.urls import path
from . import views


urlpatterns = [
    path('users/create/', views.RegistrUserView.as_view(), name='create'),

    path('users/', views.user_list_view, name='list'),
    path('users/<int:pk>/', views.user_detail_view, name='detail'),
    path('users/<int:pk>/update', views.user_update_view, name='update'),
    path('users/<int:pk>/delete', views.user_delete_view, name='delete'),

]

