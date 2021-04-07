from django.contrib import admin
from django.urls import path
from core.views import HelloView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloView.as_view(), name="HeloView"),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
