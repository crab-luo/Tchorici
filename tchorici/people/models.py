# -*- coding: utf-8 -*-

from django.db import models


class Person(models.Model):
	first_name = models.CharField(max_length=20, verbose_name='Jméno', \
		help_text='Jan, Jéňa, Jenda, Honza, Honzík? To je otázka. Každopádně se křestní jméno zobrazí na webu.')
	last_name = models.CharField(max_length=30, verbose_name='Příjmení', \
		help_text='Příjmení už se na webu zobrazovat nebude, slouží pouze k rozlišení osob')

	photo = models.ImageField(upload_to='photos/', verbose_name='Fotka', \
		help_text='Fotka musí mít čtvercové rozměry. Bude zmenšena na velikost 100x100.')

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

	def admin_photo(self):
		if self.photo:
			return '<img src="%s" width=100 height=100>' % (self.photo.url)
	admin_photo.short_description = 'Fotografie'
	admin_photo.allow_tags = True

	class Meta:
		ordering = ['first_name', 'last_name']
		unique_together = ('first_name', 'last_name')

		verbose_name = 'Osoba'
		verbose_name_plural = 'Osoby'



