# -*- coding: utf-8 -*-
from people.models import Person

from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		('Informace o osobě', {'fields': ['first_name', 'last_name']}),
		('Fotografie', {'fields': ['photo']}),
	]
	list_display = ('__unicode__', 'admin_photo')

admin.site.register(Person, PersonAdmin)


