from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, ListAttribute
from app.utils.config import Config
from datetime import datetime, timezone

def empty_list():
    return []

class LevelModel(Model):
    class Meta:
        table_name = "levels_intania_dev"
        region = Config.AWS_REGION_NAME
        
    level = NumberAttribute(hash_key=True, default=1)
    boss_image_s3 = UnicodeAttribute(null=True)
    background_image_s3 = UnicodeAttribute(null=True)
    boss_hp = NumberAttribute(default=100)
    boss_attack = NumberAttribute(default=10)
    boss_name = UnicodeAttribute()
    question_ids = ListAttribute(of=UnicodeAttribute, default=empty_list)
    created_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))
    updated_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))
    
    def to_dict(self):
        return {
            'level': self.level,
            'boss_image_s3': self.boss_image_s3,
            'background_image_s3': self.background_image_s3,
            'boss_hp': self.boss_hp,
            'boss_attack': self.boss_attack,
            'boss_name': self.boss_name,
            'question_ids': self.question_ids,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        } 