from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy.exc import SQLAlchemyError

mapper_registery = registry()

@mapper_registery.mapped
class UsermanagemantTable():
    __tablename__ = 'solution_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    address = Column(String)

    def __repr__(self):
        return "<SystemSettingsTable(%r, %r, %r, %r)>" % (self.id,
                                                        self.name,
                                                        self.occupation,
                                                        self.address)


def init_db(engine):
    try:
        with engine.begin() as connection:
            mapper_registery.metadata.create_all(connection)
    except SQLAlchemyError as e:
        raise Exception(e)
    finally:
        engine.dispose()