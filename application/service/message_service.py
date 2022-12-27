from abc import ABC, abstractmethod

from application.dto.dtos import MessageDto

class MessageService(ABC):

    @abstractmethod
    def get_messages(self) -> list[MessageDto]:
        ...
        
    @abstractmethod
    def add_message(self, dto: MessageDto) -> MessageDto:
        ...
