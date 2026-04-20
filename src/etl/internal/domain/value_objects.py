from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(frozen=True)
class MessageMetadata:
    chat_id: int
    sender_id: Optional[int]
    text: Optional[str]
    attached_files: List[str] = field(default_factory=list)
