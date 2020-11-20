from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),

    path('api/v1/', include('UserApp.urls')),

]

urlpatterns += doc_urls
