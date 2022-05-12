from djongo import models

# Create your models here.

class Bodypart (models.Model):
    bodypart = models.TextField(max_length=50)

# class SubBodypart (models.Model):
#     body_partid = models.ManyToManyRel()
#     Subbodypart = models.AutoField(max_length=50)

class Symptom (models.Model):
    symptomname = models.TextField(max_length=100)
