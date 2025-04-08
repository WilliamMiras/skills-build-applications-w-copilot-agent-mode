from pymongo import MongoClient
from django.conf import settings
from django.core.management.base import BaseCommand
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many([
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        db.teams.insert_one({"_id": ObjectId(), "name": "Blue Team", "members": []})

        db.activities.insert_many([
            {"_id": ObjectId(), "user": "thundergod", "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user": "metalgeek", "activity_type": "Crossfit", "duration": 120},
            {"_id": ObjectId(), "user": "zerocool", "activity_type": "Running", "duration": 90},
            {"_id": ObjectId(), "user": "crashoverride", "activity_type": "Strength", "duration": 30},
            {"_id": ObjectId(), "user": "sleeptoken", "activity_type": "Swimming", "duration": 75},
        ])

        db.leaderboards.insert_one({"_id": ObjectId(), "team": "Blue Team", "points": 100})

        db.workouts.insert_many([
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon", "duration": 90},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength", "duration": 30},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
