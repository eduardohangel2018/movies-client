from django.db import models


# class User(models.Model):
#     _id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     data_nasc = models.DateField()

#     def __str__(self):
#         return self.name


# class Movie(models.Model):
#     _id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.CharField(blank=False, max_length=30)
#     director = models.CharField(max_length=30, unique=True)
#     producer = models.CharField(max_length=30)
#     release_date = models.CharField(max_length=10)
#     rt_score = models.CharField(max_length=10)

#     def __str__(self):
#         return Movie.title
