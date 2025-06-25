from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email='test2@example.com', name='Test User2', password='testpass2')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test3@example.com', name='Test User3', password='testpass3')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-06-25', points=10)
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='test4@example.com', name='Test User4', password='testpass4')
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_by=user)
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Team B')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, month='June')
        self.assertEqual(leaderboard.total_points, 100)
