from django.db import models

class OSAnalytics(models.Model):
    os = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'OSAnalytics'

    def __str__(self) -> str:
        return self.os
