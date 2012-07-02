# -*- coding: utf-8 -*-
from events.models import Event, Link
from people.models import Person


from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin


from django import forms


class EventForm(forms.ModelForm):
	people = forms.ModelMultipleChoiceField(
		Person.objects.all(),
		widget=FilteredSelectMultiple("Ucastnici", False, attrs={'rows': '10'})
	)

	class Meta:
		model = Event


class LinkInline(admin.TabularInline):
	model = Link
	extra = 3


class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		('Základní popis', {'fields': ['name', 'description', 'photo']}),
		('Datum akce', {'fields': ['date_start', 'date_end']}),
		('Účastníci', {'fields': ['people']}),
	]

	form = EventForm
	filter_horizontal = ('people',)
	inlines = [LinkInline]

	list_display = ('name', 'description', 'date_start', 'admin_photo')
	list_filter = ['date_start']
	date_hierarchy = 'date_start'

	save_on_top = True
	search_fields = ['name', 'description']


admin.site.register(Event, EventAdmin)
