from django.db import models
from django.contrib.auth.models import User
from .schedule import Schedule
from .task import Task


class Detail(models.Model):
    objects = models.Manager()
    schedule = models.ForeignKey(Schedule, related_name='details', blank=False, null=False, on_delete=models.CASCADE)
    taskmaster = models.ForeignKey(User, related_name='tasks_assignment', blank=False, null=False,
                                   on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='assignments', blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'detail'
        unique_together = (('schedule', 'task'),)
        indexes = [
            models.Index(fields=['schedule', ]),
        ]
        # app_label = 'apps.models.models.detail.Detail'
