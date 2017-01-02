from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'link',
        'tag_list',
        'date_created',
        'date_updated',
    )
    list_display_links = (
        'link',
        'date_created',
        'date_updated',
    )
    list_editable = [
        'status',
    ]

    def get_queryset(self, request):
        return super(LinkAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Link, LinkAdmin)