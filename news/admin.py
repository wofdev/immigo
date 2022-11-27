from django.contrib import admin
from news.models import (
    News,
    Author,
    Tag,
    Attachment,
)

# registering our models to admin site

admin.site.register(News)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Attachment)