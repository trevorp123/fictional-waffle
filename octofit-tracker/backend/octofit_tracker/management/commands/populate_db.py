from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Red Rockets')
        team2 = Team.objects.create(name='Blue Blazers')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_by=user1)
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile', suggested_by=user2)

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=date(2025, 6, 20), points=10)
        Activity.objects.create(user=user2, activity_type='walk', duration=60, date=date(2025, 6, 21), points=8)
        Activity.objects.create(user=user3, activity_type='strength', duration=45, date=date(2025, 6, 22), points=12)

        # Leaderboard
        Leaderboard.objects.create(team=team1, total_points=18, month='June')
        Leaderboard.objects.create(team=team2, total_points=12, month='June')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
