from application import db
from application.dto.dtos import MessageDto

class Message(db.Model): # type: ignore  [pyright thinking Model is wrong here]
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))  
    content = db.Column(db.String(255))  

    @staticmethod
    def to_dto(msg) -> MessageDto:
        return MessageDto(
            id=msg.id,
            title=msg.title,
            content=msg.content,
        )
