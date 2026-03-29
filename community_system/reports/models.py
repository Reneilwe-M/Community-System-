# from django.db import models


# class IssueReport(models.Model):
#     ISSUE_TYPES = [
#         ('water', 'Water'),
#         ('electricity', 'Electricity'),
#         ('pothole', 'Pothole'),
#         ('waste', 'Waste'),
#     ]

#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('resolved', 'Resolved'),
#     ]

#     issue_type   = models.CharField(max_length=20, choices=ISSUE_TYPES)
#     description  = models.TextField()
#     photo        = models.ImageField(upload_to='photos/', blank=True, null=True)
#     status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.get_issue_type_display()} — {self.status}"
from django.db import models

from django.contrib.auth.models import User


class Issue(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    issue_type   = models.CharField(max_length=100)
    description  = models.TextField()
    photo        = models.ImageField(upload_to='issue_photos/', blank=True, null=True)
    address      = models.CharField(max_length=255, blank=True, null=True)
    latitude     = models.CharField(max_length=50, blank=True, null=True)
    longitude    = models.CharField(max_length=50, blank=True, null=True)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    priority     = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    created_at   = models.DateTimeField(auto_now_add=True)

    resolution_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.issue_type} — {self.created_at.strftime('%d %b %Y')}"