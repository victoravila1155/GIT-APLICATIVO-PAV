import sqlalchemy as db
import persistence.model as mod

engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/pavdatos', echo=True, future=True)
mod.Base.metadata.create_all(engine)