import logging
from injector import inject

from application.repository.message_repository import MessageRepository

from application.dto.dtos import MessageDto

from application.service.message_service import MessageService

class MessageServiceImpl(MessageService):

    @inject
    def __init__(self, repository: MessageRepository) -> None:
        self._repository = repository
        self._logger = logging.getLogger(__name__)


    def get_messages(self) -> list[MessageDto]:
        return self._repository.get_messages()


    def add_message(self, req: MessageDto) -> MessageDto:
        return self._repository.insert_message(req)
