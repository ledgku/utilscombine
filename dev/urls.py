from django.urls import path

from dev.views import Main

app_name = 'dev'
urlpatterns = [
    path('', Main.as_view(), name = 'index'),
]