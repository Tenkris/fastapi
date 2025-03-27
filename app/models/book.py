import uuid
import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from app.utils.basemeta import BaseMeta

class BookModel(Model):
    class Meta(BaseMeta):
        table_name = "books"
    
    def get_current_time_utc():
        return datetime.datetime.now(datetime.timezone.utc)
    
    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    author = UnicodeAttribute()
    isbn = UnicodeAttribute()
    publication_year = NumberAttribute()
    price = NumberAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=get_current_time_utc)
    updated_at = UTCDateTimeAttribute(default_for_new=get_current_time_utc)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)
        super().save(*args, **kwargs) 