from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute, UTCDateTimeAttribute, NumberAttribute
from app.utils.config import Config
from datetime import datetime, timezone

class UserModel(Model):
    class Meta:
        table_name = "users_intania_dev"
        region = Config.AWS_REGION_NAME
        
    email = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()
    level_id = NumberAttribute(default=1)
    user_image = UnicodeAttribute(null=True)
    attack = NumberAttribute(default=10.0)
    defense = NumberAttribute(default=10.0)
    speed = NumberAttribute(default=10.0)
    critical = NumberAttribute(default=5.0)
    hp = NumberAttribute(default=100.0)
    created_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))

    @staticmethod
    def validate_phone(phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits")
    def to_dict(self):
        return {
            'id': self.email,
            'email': self.email,
            'level_id': self.level_id,
            'user_image': self.user_image,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
            'critical': self.critical,
            'hp': self.hp,
            'created_at': self.created_at.isoformat()
        }
    
