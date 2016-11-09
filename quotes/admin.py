from django.contrib import admin
from .models import Quote

admin.autodiscover()


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitter', 'submitted_on')
    search_fields = ['title']


admin.site.register(Quote, QuoteAdmin)
