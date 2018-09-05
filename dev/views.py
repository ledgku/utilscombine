from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class FindMyIp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dev/findmyip.html', {})


class FindMyGps(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dev/findmygps.html', {})