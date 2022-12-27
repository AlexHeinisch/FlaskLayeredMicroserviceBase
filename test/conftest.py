from application.repository.models import Message
import pytest
from application.repository.models import Message

@pytest.fixture(scope='session')
def sample_message1():
    msg: Message = Message(
        id=1,
        title='Title 1',
        content='message content 1'
    )
    return msg

@pytest.fixture(scope='session')
def sample_message2():
    msg: Message = Message(
        id=2,
        title='Title 2',
        content='message content 2'
    )
    return msg

@pytest.fixture(scope='session')
def sample_message3():
    msg: Message = Message(
        id=3,
        title='Title 3',
        content='message content 3'
    )
    return msg
