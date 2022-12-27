import logging
from werkzeug.exceptions import BadRequest
from typing import cast
from flask import Blueprint, request

# DI
from injector import inject

# Validation
from application.dto.schemas import AddMessageSchema
from application.dto.dtos import MessageDto
from application.service.message_service import MessageService


message = Blueprint('message', __name__)
logger = logging.getLogger(__name__)

@inject
@message.route('', methods=['GET'])
def get_messages(service: MessageService):
    logger.info(f'[GET] message')
    return AddMessageSchema(many=True).dump(service.get_messages())

@inject
@message.route('', methods=['POST'])
def post_message(service: MessageService):
    body = request.get_json()
    if not body:
        raise BadRequest()
    req: MessageDto = cast(MessageDto, AddMessageSchema().load(body))
    return AddMessageSchema().dump(service.add_message(req)), 201
