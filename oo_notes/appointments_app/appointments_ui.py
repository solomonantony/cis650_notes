import datetime
from dentist_office import DentistOffice, Staff, Patient, Appointment
murray_dental = DentistOffice("Murray Dentists")
staff_amir = Staff(office=murray_dental, name="Amir", position="Front office staff")
new_patient = Patient(patient_name= 'solomon', 
                      phone='270-111-2222', 
                      address='123 Lake Dr Murray',
                      date_of_birth=datetime.datetime.strptime('1/1/1970', '%m/%d/%Y'))
print(type(staff_amir.office))
staff_amir.register_patient(new_patient)
print(murray_dental.list_patients())


