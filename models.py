from peewee import *
import os
import datetime
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:  
    DATABASE = connect(os.environ.get('DATABASE_URL')) 
else:
    DATABASE = SqliteDatabase('fits.sqlite')

# DATABASE = SqliteDatabase('fits.sqlite')


class Fit(Model):
    name = CharField()
    steps = CharField()
    description = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Fit], safe=True)
    print("TABLES created")
    DATABASE.close()