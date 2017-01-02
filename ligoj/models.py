from __future__ import unicode_literals

from django.db import models
import tldextract
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

ACTIVE = 'ACT'
HIDDEN = 'HID'
STATUS = (
    (ACTIVE, 'active'),
    (HIDDEN, 'hidden'),
)

class TaggedLink(TaggedItemBase):
    content_object = models.ForeignKey('Link')

class Link(models.Model):
    link = models.URLField()
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=ACTIVE
    )
    tags = TaggableManager(through=TaggedLink)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        domain = ""
        if tldextract.extract(self.link).registered_domain:
            domain = tldextract.extract(self.link).registered_domain 
        return "%s - %s" % (domain, self.date_updated)