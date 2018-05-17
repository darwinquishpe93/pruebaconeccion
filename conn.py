from peewee import *
    db = SqliteDatabase ('pruebadb')

    class Student (Model)
        username = Charfield(maxlength=255, unique=true)
        points = integerfield(default =0 )

    Class Meta:
        database = db
    if __name__ = "__main__":
        db.connect()
        db.create_table([Student], safe = true)
        #asdasdasd
        #asdasd1
