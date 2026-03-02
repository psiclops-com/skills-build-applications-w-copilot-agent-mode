from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='superman@dc.com', name='Superman', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Assign users to teams
        marvel.members.add(users[0], users[1])
        dc.members.add(users[2], users[3])

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2026-03-01')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2026-03-01')
        Activity.objects.create(user=users[2], type='swim', duration=60, date='2026-03-01')
        Activity.objects.create(user=users[3], type='walk', duration=20, date='2026-03-01')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=75)
        Leaderboard.objects.create(team=dc, points=80)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
