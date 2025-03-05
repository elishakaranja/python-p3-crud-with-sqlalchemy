#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,func
from datetime import datetime
import ipdb

from sqlalchemy_sandbox import Base, Student

if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        # birthday=datetime.datetime.now()
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )
    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )
    #session.add(albert_einstein)
    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()
    
    students = session.query(Student)
    print([student for student in students])
    # print(f"New student ID is {albert_einstein.id}.")
    # print(f"New student ID is {alan_turing.id}.")


    
    # ipdb.set_trace()

