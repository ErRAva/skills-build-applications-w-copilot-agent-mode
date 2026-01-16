from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.db import connection

# Define models for teams, activities, leaderboard, and workouts
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test123'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test123'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='test123'),
        ]

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', activity_type='Running', duration=30, team='Marvel')
        Activity.objects.create(user_email='spiderman@marvel.com', activity_type='Cycling', duration=45, team='Marvel')
        Activity.objects.create(user_email='batman@dc.com', activity_type='Swimming', duration=60, team='DC')
        Activity.objects.create(user_email='wonderwoman@dc.com', activity_type='Yoga', duration=50, team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength training for superheroes', suggested_for='Marvel')
        Workout.objects.create(name='Agility Boost', description='Agility and flexibility workout', suggested_for='DC')

        # NOTE: Unique index on email for users collection should be created manually using mongosh or pymongo, as Djongo does not support raw MongoDB commands.

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
