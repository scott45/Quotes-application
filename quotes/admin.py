from django.contrib import admin
from .models import Quote
admin.autodiscover()

admin.site.register(Quote)
