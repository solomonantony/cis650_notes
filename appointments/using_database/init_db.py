from sqlalchemy import create_engine
from models import Base

engine = create_engine('dentist_appointments.db', echo=True)
Base.metadata.drop_all(engine)  # Optional: clean up old tables
Base.metadata.create_all(engine)
