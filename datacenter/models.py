from django.db import models
from django.utils import timezone


def get_duration(visit):
    entered_at = timezone.localtime(visit.entered_at)
    leaved_at = timezone.localtime(visit.leaved_at)
    delta = leaved_at - entered_at
    seconds = delta.total_seconds()
    return seconds


def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return "%02i:%02i" % (hours, minutes)


def is_visit_long(visit, minutes=60):
    seconds = get_duration(visit)
    return seconds >= minutes*60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
