from datetime import datetime
from time import strftime, time, localtime
from attendance.models import facial_attendance
from lecture.models import Lecture

def my_cron_job():
    now = datetime.now()
    lec1 = Lecture.objects.get(code='L001')
    facial_attendance.objects.create(username=20151937, lecture=lec1, result='{"' + str(now.hour) + '" : "ATTEND"}' )
