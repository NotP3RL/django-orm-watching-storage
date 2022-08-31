from datacenter.models import Passcard, Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.all(), passcode=passcode)
    visits = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        entered_at = timezone.localtime(visit.entered_at)
        visit_duration = get_duration(visit)
        formatted_visit_duration = format_duration(visit_duration)
        is_visit_strange = is_visit_long(visit)
        visit_info = {
            'entered_at': entered_at,
            'duration': formatted_visit_duration,
            'is_strange': is_visit_strange
        }
        this_passcard_visits.append(visit_info)


    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
