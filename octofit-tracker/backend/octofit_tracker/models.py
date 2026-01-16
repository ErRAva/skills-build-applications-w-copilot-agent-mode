from djongo import models
from django.contrib.auth.models import AbstractUser

# Team model
class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

# Activity model
class Activity(models.Model):
	user_email = models.EmailField()
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()
	team = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.user_email} - {self.activity_type}"

# Leaderboard model
class Leaderboard(models.Model):
	team = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.team}: {self.points}"

# Workout model
class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	suggested_for = models.CharField(max_length=100)
	def __str__(self):
		return self.name
