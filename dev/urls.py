from django.urls import path

from dev.views import FindMyIp,FindMyGps

app_name = 'dev'
urlpatterns = [
    # path('', Main.as_view(), name = 'index'),
    path('findmyip', FindMyIp.as_view(), name = 'findmyip'),
    path('findmygps', FindMyGps.as_view(), name = 'findmygps'),
]