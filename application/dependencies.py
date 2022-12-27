from application.repository.impl.sqlalchemy_message_repository import SQLAlchemyMessageRepository
from application.repository.message_repository import MessageRepository
from application.service.impl.message_service_impl import MessageServiceImpl
from application.service.message_service import MessageService

from flask_sqlalchemy import SQLAlchemy

from application import db
from injector import Binder, singleton

def configure(binder: Binder):
    binder.bind(SQLAlchemy, to=db, scope=singleton)

    binder.bind(MessageService, to=MessageServiceImpl, scope=singleton)

    binder.bind(MessageRepository, to=SQLAlchemyMessageRepository, scope=singleton)
