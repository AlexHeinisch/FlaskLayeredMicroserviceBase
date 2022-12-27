import json
from application.repository.models import Message
import pytest
from application import db

@pytest.fixture(scope='function')
def client_with_sample_users(
        sample_message1: Message, 
        sample_message2: Message, 
        sample_message3: Message, 
        app, client
    ):
    with app.app_context():
        db.session.add(sample_message1)
        db.session.add(sample_message2)
        db.session.add(sample_message3)
        db.session.commit()
        yield client

def test_get_users_with_limit(
    client_with_sample_users
    ):
    response = client_with_sample_users.get(
        '/message'
    )
    assert '200' in response.status
    assert len(response.json) == 3

def test_post_user_already_exists(
    client,
        sample_message1: Message
    ):
    response = client.post(
        '/message',
        content_type='application/json',
        data=json.dumps({
            'title': sample_message1.title,
            'content': sample_message1.content
        })
    )
    assert '201' in response.status
