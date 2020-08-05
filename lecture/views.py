from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Lecture
from .forms import LectureSettingForm
# Create your views here.


def setting(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = LectureSettingForm(request.POST)
        if form.is_valid():
            lecture.start_time = form.cleaned_data['start_time']
            lecture.end_time = form.cleaned_data['end_time']
            lecture.term = form.cleaned_data['term']
            lecture.count = form.cleaned_data['count']
            lecture.save()
            return HttpResponse('<script type="text/javascript"> window.opener.parent.location.href = "{%url "prof_detail" lecture_id}";</script>')

    else:
        form = LectureSettingForm(instance=lecture)
        context = {'lecture': lecture, 'form': form}
        return render(request, 'setting.html', context)
