from abc import ABC, abstractmethod

from application.dto.dtos import MessageDto

class MessageRepository(ABC):

    @abstractmethod
    def get_messages(self) -> list[MessageDto]:
        ...

    @abstractmethod
    def insert_message(self, dto: MessageDto) -> MessageDto:
        ...
