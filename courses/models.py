from django.db import models
import uuid

class Courses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(null=True, max_length=15)
    course_category = models.CharField(null=True, max_length=15)

    difficulties = [
        ('e','EASY'),
        ('m','MEDIUM'),
        ('h','HARD'),
    ]

    course_diff = models.CharField(
        choices=difficulties,
        default="e",
        max_length=1
    )

    def __str__(self):
        return self.course_name

class EnrolledCourses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(null=True, max_length=15)
    course_category = models.CharField(null=True, max_length=15)

    difficulties = [
        ('e','EASY'),
        ('m','MEDIUM'),
        ('h','HARD'),
    ]

    course_diff = models.CharField(
        choices=difficulties,
        default="e",
        max_length=1
    )

    def __str__(self):
        return self.course_name

 
