from django.contrib import admin
from Sentiment_Classification.models import *


class ResultAdmin(admin.ModelAdmin):
    list_display = ['sentiment', 'classification']
    list_filter = ()
    search_fields = ['sentiment']
    list_per_page = 25


admin.site.register(Result, ResultAdmin)


