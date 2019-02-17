from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    student_id=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.student_id

