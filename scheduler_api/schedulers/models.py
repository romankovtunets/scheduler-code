from django.db import models


class EmailList(models.Model):

    email = EmailField()
    dispatch_date = DateTimeField()

    def __str__(self):
        return self.email


class DatesSkipList(models.Model):

    date = DateTimeField()

    def __str__(self):
        return self.date


class Schedule(models.Model):

    contacts = models.ManyToManyField(
        EmailList,
        )

    days_to_skip = models.ManyToManyField(
        DatesSkipList,
        )
