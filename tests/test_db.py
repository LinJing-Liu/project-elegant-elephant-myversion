# test_db.py

import unittest
from peewee import *
import os
os.environ['TESTING'] = 'true'

from app import TimelinePost

MODELS = [TimelinePost]

# use an in memory SQLite database for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_create_timeline_post(self):
        fist_post = TimelinePost.create(name='Marlene', email='marlene@example.com', content='Hello World, I\'m Marlene!')
        assert fist_post.id == 1
        second_post = TimelinePost.create(name='Marlene', email='marlene@example.com', content='Hello World, I\'m Marlene!')
        assert second_post.id == 2
