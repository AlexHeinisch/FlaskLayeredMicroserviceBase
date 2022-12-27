from application.repository.impl.sqlalchemy_message_repository import SQLAlchemyMessageRepository
from application.repository.models import Message


def test_get_messages(
    sample_message1: Message,
    sample_message2: Message,
    message_repo: SQLAlchemyMessageRepository,
    mock_sqlalchemy
    ):
    mock_sqlalchemy.session.execute.return_value.all.return_value = [(sample_message1,),(sample_message2,)]
    results = message_repo.get_messages()
    assert Message.to_dto(sample_message1) in results
    assert Message.to_dto(sample_message2) in results
    assert len(results) == 2

def test_insert_message(
    sample_message3: Message,
    message_repo: SQLAlchemyMessageRepository,
    mock_sqlalchemy
    ):
    message_repo.insert_message(Message.to_dto(sample_message3))
    mock_sqlalchemy.session.add.assert_called_once()
    mock_sqlalchemy.session.commit.assert_called_once()
