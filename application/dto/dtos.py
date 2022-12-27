from dataclasses import dataclass

@dataclass
class MessageDto():
    id: int
    title: str
    content: str
