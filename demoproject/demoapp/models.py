from django.db import models

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=30, blank=True, null=True)
    college_city = models.CharField(max_length=30, blank=True, null=True)


class Student(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    college = models.ForeignKey(College, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)