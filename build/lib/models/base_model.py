import uuid
import datetime


class BaseModel():
    id = uuid.uuid4()
    created_at = datetime.datetime.utcnow()
    updated_at = datetime.datetime.utcnow()

    def __str__(self) -> str:
        return __name__, self.id, self.__dict__
    
    def save(self):
        updated_at = datetime.datetime.utcnow()
        self.__dict__ = self
        self.created_at.isoformat()