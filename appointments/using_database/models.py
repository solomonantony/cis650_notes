from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    medical_history = Column(Text)
    address = Column(String)
    date_of_birth = Column(Date)

    appointments = relationship("Appointment", back_populates="patient")

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    appointment_time = Column(DateTime, default=datetime.now)
    reason = Column(Text)
    staff_name = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))

    patient = relationship("Patient", back_populates="appointments")
