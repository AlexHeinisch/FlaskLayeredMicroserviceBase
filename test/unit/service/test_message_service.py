from application.repository.models import Message
from application.service.message_service import MessageService

def test_insert_user_success(
        mock_repository,
        message_service: MessageService,
        sample_message1: Message
    ):
    mock_repository.insert_message.return_value = Message.to_dto(sample_message1)

    returned_message = message_service.add_message(Message.to_dto(sample_message1))
    assert returned_message == Message.to_dto(sample_message1)
    mock_repository.insert_message.assert_called_once_with(Message.to_dto(sample_message1))
    # do further service logic checks here
