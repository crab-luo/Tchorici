from django.shortcuts import render


def home(request):
	return render(request, 'tchorici/index.html', {})
