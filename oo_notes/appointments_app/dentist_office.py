class DentistOffice:
    def __init__(self, name='CIS650'):
      self.name = name
      self.patients = []
      self.appointments = []
    
    def add_patient(self, patient):
      self.patients.append(patient)
    
    def add_appointment(self, appointment):
      self.appointments.append(appointment)
    
    def find_patient(self, name):
       return next((p for any_patitient in self.patients if p.name == name), None)
    
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
    
    def cancel_appointment(self, existing_appointment):
       existing_appointment = [appointment for appointment in self.appointments
                               if appointment == existing_appointment]
       existing_appointment.status="Canceled"
    def list_patients(self):
       return self.patients
    

class Staff:
    def __init__(self, name, office, position):
      self.name = name
      self.office = office
      self.position = position
    def register_patient(self, patient):
       self.office.add_patient(patient)
    def book_appointment(self, appointment):
       self.office.add_appointment(appointment)
    def update_patient_info(self,old_name, new_name=None, new_address = None, new_history=None):
       return self.office.update_patient(old_name, new_name, new_address, new_history)
    def cancel_patient_appointment(self, existing_appointment):
       return self.office.cancel_appointment(self, existing_appointment)
    

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
    
    def print_details(self):
       print(f'{self.name}, {self.date_of_birth}')


    @property
    def details(self):
        return self.name + '(' + self.phone + ')'

class Appointment:
    def __init__(self, patient, when, reason, description=""):
        self.patient = patient
        self.appointment_time = when
        self.reason = reason
        self.description = description
        self.status = 'Scheduled'

    @property
    def details(self):
        return (self.patient.details + self.appointmentTime + self.description)
