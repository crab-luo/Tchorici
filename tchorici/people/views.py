from django.shortcuts import render

from people.models import Person


def list(request):
	people = Person.objects.all()
	return render(request, 'people/list.html', {'people': people})
