from django.test import TestCase
from django.contrib.auth.models import User

from .models import Board

class BoardTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        # Create an a board
        test_board = Board.objects.create(title='Board title')
        test_board.save()


    def   test_board_content(self):
        board = Board.objects.get(id=1)
        title = f'{board.title}'
        self.assertEqual(title, 'Board title')