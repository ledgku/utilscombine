from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class FindMyIp(View):
    def get(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return render(request, 'dev/findmyip.html', {
            'ip': ip})


class FindMyGps(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dev/findmygps.html', {})