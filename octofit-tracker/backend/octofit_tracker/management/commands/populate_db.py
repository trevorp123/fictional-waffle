from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data using PyMongo.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        for collection in ['users', 'teams', 'activity', 'leaderboard', 'workouts']:
            db[collection].delete_many({})

        # Users
        a1 = {"email": "alice@example.com", "name": "Alice", "password": "alicepass"}
        a2 = {"email": "bob@example.com", "name": "Bob", "password": "bobpass"}
        a3 = {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
        user_ids = db.users.insert_many([a1, a2, a3]).inserted_ids

        # Teams
        team1 = {"name": "Red Rockets", "members": [user_ids[0], user_ids[1]]}
        team2 = {"name": "Blue Blazers", "members": [user_ids[2]]}
        teams_ids = db.teams.insert_many([team1, team2]).inserted_ids

        # Workouts
        workout1 = {"name": "Pushups", "description": "Do 20 pushups", "suggested_by": user_ids[0]}
        workout2 = {"name": "Running", "description": "Run 1 mile", "suggested_by": user_ids[1]}
        db.workouts.insert_many([workout1, workout2])

        # Activities
        activity1 = {"user": user_ids[0], "activity_type": "run", "duration": 30, "date": datetime(2025, 6, 20), "points": 10}
        activity2 = {"user": user_ids[1], "activity_type": "walk", "duration": 60, "date": datetime(2025, 6, 21), "points": 8}
        activity3 = {"user": user_ids[2], "activity_type": "strength", "duration": 45, "date": datetime(2025, 6, 22), "points": 12}
        db.activity.insert_many([activity1, activity2, activity3])

        # Leaderboard
        leaderboard1 = {"team": teams_ids[0], "total_points": 18, "month": "June"}
        leaderboard2 = {"team": teams_ids[1], "total_points": 12, "month": "June"}
        db.leaderboard.insert_many([leaderboard1, leaderboard2])

        self.stdout.write(self.style.SUCCESS('Test data populated successfully using PyMongo.'))
