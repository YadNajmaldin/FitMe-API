from peewee import *
import datetime
DATABASE = SqliteDatabase('fits.sqlite')


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