from django.shortcuts import render

from events.models import Event, Link


def list(request):
	events = Event.objects.all().order_by('-date_start')

	return render(request, 'events/list.html', {'events': events})


def detail(request, slug):
	event = Event.objects.get(slug=slug)
	articles = Link.objects.filter(event=event, type='article').all()
	photos = Link.objects.filter(event=event, type='photos').all()
	other = Link.objects.filter(event=event, type='other').all()

	return render(request, 'events/detail.html', {
		'event': event,
		'articles': articles,
		'photos': photos,
		'other': other,
	})
