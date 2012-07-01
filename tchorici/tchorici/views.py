from django.contrib.flatpages.models import FlatPage

from django.shortcuts import render


def error404(request):
	page = FlatPage.objects.get(url="/error-404/")
	return render(request, 'flatpages/default.html', {'flatpage': page})


def error500(request):
	page = FlatPage.objects.get(url="/error-500/")
	return render(request, 'flatpages/default.html', {'flatpage': page})
