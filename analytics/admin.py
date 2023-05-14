import json
from typing import Dict, Optional

from django.contrib import admin
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

from .models import OSAnalytics


# Register your models here.
@admin.register(OSAnalytics)
class OSAnalyticsAdmin(admin.ModelAdmin):
    
    def changelist_view(self, request: HttpRequest, extra_context: Dict[str, str] | None = ...) -> TemplateResponse:
        stats = (
            OSAnalytics.objects.values('os').annotate(Count('os'))
        )

        as_json = json.dumps(list(stats), cls=DjangoJSONEncoder)
        extra_context = {'stats': as_json} or extra_context
        return super().changelist_view(request, extra_context=extra_context)
