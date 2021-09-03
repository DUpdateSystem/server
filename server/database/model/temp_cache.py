from time import time

from peewee import *

from ..field.blob import LongBlogField
from ..meta import BaseModel, BaseMeta


class TempCache(BaseModel):
    class Meta(BaseMeta):
        db_table = 'cache_temp'

    key = CharField(primary_key=True, column_name='key')
    value = LongBlogField(column_name='value')
    timestamp = IntegerField(null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_timestamp()

    def update_timestamp(self):
        self.timestamp = time()
