from django.db import models

class CronJobLog(models.Model):
    # Your existing fields...
    code = models.CharField(max_length=64, db_index=True)
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)
    is_success = models.BooleanField(default=False)
    message = models.TextField(default='', blank=True)
    ran_at_time = models.TimeField(null=True, blank=True, db_index=True, editable=False)

    def __str__(self):
        return "%s (%s)" % (self.code, "Success" if self.is_success else "Fail")

    class  my_meta:
        # Replacing `index_together` with `indexes`
        indexes = [
            models.Index(fields=['code', 'is_success', 'ran_at_time']),
            models.Index(fields=['code', 'start_time', 'ran_at_time']),
            models.Index(fields=['code', 'start_time']),
        ]
        app_label = 'django_cron'
