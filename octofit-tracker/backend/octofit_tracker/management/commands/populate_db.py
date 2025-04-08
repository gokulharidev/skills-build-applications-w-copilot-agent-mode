from django.core.management.base import BaseCommand
from tracker.models import User, Activity
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(username='testuser1', email='testuser1@example.com')
        user2 = User.objects.create(username='testuser2', email='testuser2@example.com')

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date=datetime.now())
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date=datetime.now())

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))