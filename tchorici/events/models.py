# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google

TYPES = (
    ('article', 'Článek'),
    ('photos', 'Fotografie'),
    ('other', 'Ostatní'),
)


class Event(models.Model):
    slug = models.SlugField(verbose_name='Adresa', editable=False, unique=True)
    name = models.CharField(max_length=50, verbose_name='Název', \
        help_text='''
            Pokuste se do názvu zahrnout co nejvíce informací. Ideální tvar je
            "Název, Místo Rok" (např. "NP Sarek, Švédsko 2012")
        ''')
    description = models.CharField(max_length=200, verbose_name='Popis', \
        blank=True, help_text='''
            Popis není povinné vyplňovat, ale určitě to není na škodu. Zvláště
            u důležitějších akcí. Měl by ale být stručný. Maximum je 200 znaků.
        ''')

    photo = models.ImageField(upload_to='events/', verbose_name='Fotografie', \
        help_text='''
            Obrázek by měl být v poměru 4:1, bude převeden na rozměry 800x200.
        ''')

    date_start = models.DateField(verbose_name='Začátek', \
        help_text='''
            Vyplněn musí být alespoň začátek akce. Podle toho jsou pak události
            řazeny.
        ''')
    date_end = models.DateField(verbose_name='Konec', blank=True, null=True)

    people = models.ManyToManyField('people.Person', blank=True, \
        verbose_name='Účastníci')

    location = models.CharField(max_length=100, verbose_name='Umístění', \
        blank=True, null=True, help_text='''
            Popisek k tomu, kde se akce odehrála. Tedy například Šumava,
            Jizerské hory, Švédsko... Podle této hodnoty by mělo být možné
            najít umístění na mapě (třeba na maps.google.com).
        ''')

    def admin_photo(self):
        if self.photo:
            return '<img src="%s" width=400 height=100>' % (self.photo.url)
    admin_photo.short_description = 'Fotografie'
    admin_photo.allow_tags = True

    def admin_link_to_map(self):
        if self.location:
            return '''<a href="https://maps.google.com/maps?q=%s"
                      target="_blank">&raquo;</a>''' \
                    % (self.location)
    admin_link_to_map.short_description = 'Mapa'
    admin_link_to_map.allow_tags = True

    def save(self):
        super(Event, self).save()
        self.slug = slugify(self.name)

        if self.photo.width != 800:
            import Image
            img = Image.open(self.photo.path)
            img = img.resize((800, 200), Image.ANTIALIAS)
            img.save(self.photo.path)

        try:
            ping_google()
        except Exception:
            pass

        super(Event, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('events.views.detail', (), {
            'id': self.id,
            'slug': self.slug,
        })

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date_start', 'name']

        verbose_name = 'Událost'
        verbose_name_plural = 'Události'


class Link(models.Model):
    event = models.ForeignKey('events.Event', related_name='link')

    url = models.URLField(primary_key=True, verbose_name='Adresa', \
        help_text='''
            Adresa odkazovaného zdroje. Je dobré využívat takové zdroje, které
            během pár týdnů nepřestanou existovat.
        ''')
    name = models.CharField(max_length=35, verbose_name='Název', \
        help_text='''
            Název by měl obsahovat hlavně název serveru, na který odkaz vede.
        ''')
    description = models.CharField(max_length=100, verbose_name='Popis', \
        blank=True, help_text='''
            Popisek by pak měl podat informaci o tom, co se v odkazu dá najít
        ''')
    type = models.CharField(max_length=7, choices=TYPES, verbose_name='Typ')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'description']

        verbose_name = 'Odkaz'
        verbose_name_plural = 'Odkazy'
