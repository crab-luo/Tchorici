from django.shortcuts import render

from events.models import Event, Link

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def list(request, page=1):
	events_list = Event.objects.all().order_by('-date_start')
	paginator = Paginator(events_list, 3)

	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)

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
