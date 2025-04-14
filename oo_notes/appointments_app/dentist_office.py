import pandas as pd
import csv
class DentistOffice:
    def __init__(self, name):
      self.name = name
      self.staff = []
      self.patients = []
      self.appointments = []

    def add_staff(self, staff):
      self.staff.append(staff)
    
    def add_patient(self, patient):
      self.patients.append(patient)
    
    def find_patient(self, name):
       return next((p for p in self.patients if p.name == name), None)
    
    def update_patient(self, old_name, new_name=None, new_address = None, new_history=None):
       patient = self.find_patient(old_name)
       if patient:
        patient.name = new_name or patient.name
        patient.address = new_address or patient.address
        patient.history.append(new_history)
        print(f'Patient {old_name} updated')
        return True
       print(f'Patient {old_name} not found.')
       return False
    
    def add_appointment(self, appointment):
      self.appointments.append(appointment)
    def find_appointment(self, patient_name):
      return next((a for a in self.appointments if a.patient.name == patient_name), None)

    def list_patients(self):
       return [patient.details for patient in self.patients]
    def list_appointments(self):
       return [appointment.details for appointment in self.appointments]
    def cancel_appointment(self, patient_name):
       appointment = self.find_appointment(patient_name)
       if appointment:
          appointment.status = 'Cancelled'
    def load_patients_data(self, file_name, file_type):
      # script to read the data file and load the results to the patients list
      if file_type == 'csv':
         with open(file_name) as patients_file:
            reader = csv.DictReader(patients_file)
            for record in reader:
               self.patients.append(record)
            return self.patients
      return False
    def load_appointments(self, file_name, file_type):
      # script to read the data file and load the results to the appointments list
      if file_type == 'csv':
         with open(file_name) as appointments_file:
            reader = csv.DictReader(appointments_file)
            for record in reader:
               self.appointments.append(record)
            return self.appointments
      return False

               

   
         

      

       
    

class Staff:
    def __init__(self, name, office:DentistOffice, position):
      self.name = name
      self.office = office
      self.position = position
    def register_patient(self, patient):
       self.office.add_patient(patient)
    def book_appointment(self, appointment):
       self.office.add_appointment(appointment)
    def update_patient_info(self,old_name, new_name=None, new_address = None, new_history=None):
       return self.office.update_patient(old_name, new_name, new_address, new_history)
    def cancel_patient_appointment(self, patient_name):
       return self.office.cancel_appointment(patient_name)
    

class Patient:
    def __init__(self, patient_name, phone, address, 
                date_of_birth, history= []):
        self.name = patient_name
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth
        self.history = history
    
    def update(self, newName, newPhone):
        self.name = newName
        self.phone = newPhone

    @property
    def details(self):
        return self.name + '(' + self.phone + ')'

class Appointment:
    def __init__(self, patient:Patient, when, reason, description=""):
        self.patient = patient
        self.appointment_time = when
        self.reason = reason
        self.description = description
        self.status = 'Scheduled'

    @property
    def details(self):
        return (f'{self.patient.details} {self.appointment_time} {self.description} {self.status}')
