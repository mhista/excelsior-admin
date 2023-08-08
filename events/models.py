from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    # Additional fields specific to events

    def __str__(self):
        return self.title

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Additional fields related to RSVPs

    def __str__(self):
        return f"{self.name} - {self.event}"
