from marshmallow import Schema, fields, validate, RAISE, post_load
from application.dto.dtos import *

class AddMessageSchema(Schema):
    id = fields.Int(
        validate=validate.Range(min=0),
        required=False,
        load_default=-1
    )
    title = fields.Str(
        validate=validate.Length(min=1,max=20),
        required=True
    )
    content = fields.Str(
        validate=validate.Length(min=0,max=200),
        required=True
    )

    @post_load
    def make(self, data, **kwargs) -> MessageDto:
        return MessageDto(**data)

    class Meta:
        unknown = RAISE
