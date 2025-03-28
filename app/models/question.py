from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from app.utils.config import Config
from datetime import datetime, timezone
from enum import Enum

class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    SINGLE_CHOICE = "single_choice"

class QuestionModel(Model):
    class Meta:
        table_name = "questions_intania_dev"
        region = Config.AWS_REGION_NAME
        
    question_id = UnicodeAttribute(hash_key=True)
    question = UnicodeAttribute()
    type = UnicodeAttribute()  # Will store enum as string
    time_countdown = NumberAttribute()
    answer = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))
    updated_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))
    
    def to_dict(self):
        return {
            'question_id': self.question_id,
            'question': self.question,
            'type': self.type,
            'time_countdown': self.time_countdown,
            'answer': self.answer,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        } 