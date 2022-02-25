import uuid

from django.db import models


# Create your models here.

class Transcript(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=100)
    student_score = models.DecimalField(max_digits=4, decimal_places=2)
    last_modified = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.student_name


class StudentDetail(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    other_name = models.CharField(blank=True, null=True, max_length=50)
    date_of_birth = models.DateField()
    student_email = models.EmailField(blank=True, null=True)
    student_parent_contact = models.CharField(default=0, max_length=10, null=False, blank=False)
    student_house = models.ForeignKey('HouseName', on_delete=models.CASCADE)
    student_class = models.ForeignKey('ClassName', on_delete=models.CASCADE)
    student_program = models.ForeignKey('Programs', on_delete=models.CASCADE)
    student_subjects = models.ManyToManyField('Subjects')

    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Subjects(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Programs(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    program_name = models.CharField(max_length=100)

    def __str__(self):
        return self.program_name


class ClassName(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name


class HouseName(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    house_name = models.CharField(max_length=30)

    def __str__(self):
        return self.house_name
