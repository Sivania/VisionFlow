from django.test import TestCase
from .models import Action

class MyModelTestCase(TestCase):
    def test_creation(self):
        my_instance = Action(name='Example', description='This is an example.')
        my_instance.save()
        # Further testing logic