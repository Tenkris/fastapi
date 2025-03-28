from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute, UTCDateTimeAttribute , NumberAttribute
from app.utils.config import Config
from datetime import datetime, timezone

class UserModel(Model):
    class Meta:
        table_name = "users_intania_dev"
        region = Config.AWS_REGION_NAME
        
    email = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()
    name = UnicodeAttribute()
    tel = UnicodeAttribute()
    role = UnicodeAttribute()
    career = UnicodeAttribute(null=True)
    gender = UnicodeAttribute(null=True)
    hobbies = UnicodeAttribute(null=True)
    reason = UnicodeAttribute(null=True)
    age = NumberAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=lambda: datetime.now(timezone.utc))

    @staticmethod
    def validate_phone(phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be 10 digits")
    def to_dict(self):
        return {
            'id': self.email,
            'name': self.name,
            'email': self.email,
            'tel': self.tel,
            'role': self.role,
            'age': self.age,
            'career': self.career,
            'gender': self.gender,
            'hobbies': self.hobbies if self.hobbies else None,
            'reason': self.reason,
            'created_at': self.created_at.isoformat()
        }
    
