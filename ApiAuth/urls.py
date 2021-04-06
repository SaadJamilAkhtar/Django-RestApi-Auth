from django.contrib import admin
from django.urls import path
from core.views import HelloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloView.as_view(), name="HeloView"),
]
