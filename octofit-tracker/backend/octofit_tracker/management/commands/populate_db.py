from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for collection/index ops
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Create unique index on email for users
        db['users'].create_index('email', unique=True)

        # Sample data
        users = [
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
            {"name": "dc", "members": ["batman@dc.com", "superman@dc.com"]},
        ]
        activities = [
            {"user": "ironman@marvel.com", "activity": "Flight", "duration": 30},
            {"user": "cap@marvel.com", "activity": "Shield Training", "duration": 45},
            {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 60},
            {"user": "superman@dc.com", "activity": "Flying", "duration": 120},
        ]
        leaderboard = [
            {"user": "ironman@marvel.com", "score": 100},
            {"user": "cap@marvel.com", "score": 90},
            {"user": "batman@dc.com", "score": 95},
            {"user": "superman@dc.com", "score": 110},
        ]
        workouts = [
            {"user": "ironman@marvel.com", "workout": "Chest Press", "reps": 20},
            {"user": "cap@marvel.com", "workout": "Push Ups", "reps": 50},
            {"user": "batman@dc.com", "workout": "Pull Ups", "reps": 30},
            {"user": "superman@dc.com", "workout": "Squats", "reps": 100},
        ]

        db['users'].insert_many(users)
        db['teams'].insert_many(teams)
        db['activities'].insert_many(activities)
        db['leaderboard'].insert_many(leaderboard)
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
