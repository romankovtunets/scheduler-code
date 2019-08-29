from rest_framework import mixins

from .models import Schedule, EmailSend
from .serializers import ScheduleSerilizer, EmailSendSerializer


class ScheduleList(mixins.RetriveModelMixin):
    """
    Retrieves list of schedules
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerilizer

class ScheduleCreate(mixins.CreateModelMixin):

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerilizer

class EmailSendList(mixins.RetriveModelMixin):
    """
    Retrieves list of scheduled email dispatch
    """

    queryset = EmailSend.objects.all()
    serializer_class = EmailSendSerializer
