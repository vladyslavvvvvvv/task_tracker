from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=51, verbose_name="task")
    description = models.TextField(verbose_name="description of the task")

    STATUS = [
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("delayed", "Delayed"),
        ("notstarted", "Not Started, Start it!"),
    ]
    status = models.CharField(max_length=20, choices=STATUS, default="not_start")

    PRIORITY_CHOICES = {
        "low": "Low priority",
        "mid": "Mid priority",
        "high": "High priority",
    }

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="mid")

    due_to = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)