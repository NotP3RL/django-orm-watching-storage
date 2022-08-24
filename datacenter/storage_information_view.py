from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    format_non_closed_visits = []
    for non_closed_visit in non_closed_visits:
        entered_at = timezone.localtime(non_closed_visit.entered_at)
        time_now = timezone.now()
        delta = time_now - entered_at
        seconds_inside = delta.total_seconds()
        hours_inside = int(seconds_inside // 3600)
        minutes_inside = int((seconds_inside % 3600) // 60)
        who_entered = non_closed_visit.passcard.owner_name
        format_non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': f'{hours_inside}:{minutes_inside}'
        })

    context = {
        'non_closed_visits': format_non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
