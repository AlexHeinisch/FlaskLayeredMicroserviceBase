import logging
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.exc
from injector import inject
from application.repository.message_repository import MessageRepository

from application.dto.dtos import MessageDto
from application.repository.models import Message

class SQLAlchemyMessageRepository(MessageRepository):

    @inject
    def __init__(self, db: SQLAlchemy) -> None:
        super().__init__()
        self._db = db
        self._logger = logging.getLogger(__name__)

    def get_messages(self) -> list[MessageDto]:
        self._logger.error(f'[persistence] get_messages')
        query = self._db.select(Message)
        try:
            usrs = self._db.session.execute(query).all()
            return [Message.to_dto(u[0]) for u in usrs]
        except sqlalchemy.exc.NoResultFound:
            return []

    def insert_message(self, dto: MessageDto) -> MessageDto:
        self._logger.debug(f'[persistence] insert_message: dto={dto}')
        msg: Message = Message(id=None, title=dto.title, content=dto.content)
        self._db.session.add(msg)
        self._db.session.commit()
        return Message.to_dto(msg)
