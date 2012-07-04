# -*- coding: utf-8 -*-
from people.models import Person

from django.contrib import admin
from django import forms


class PersonForm(forms.ModelForm):
	def clean_photo(self):
		from django.core.files.images import get_image_dimensions
		p = get_image_dimensions(self.cleaned_data['photo'])
		width, height = p

		if width != height:
			raise forms.ValidationError('Fotografie musí mít čtvercový formát')

		return self.cleaned_data['photo']

	class Meta:
		model = Person


class PersonAdmin(admin.ModelAdmin):
	form = PersonForm
	fieldsets = [
		('Informace o osobě', {'fields': ['first_name', 'last_name']}),
		('Fotografie', {'fields': ['photo']}),
	]
	list_display = ('__unicode__', 'admin_photo')

admin.site.register(Person, PersonAdmin)


