import datetime
from dentist_office import DentistOffice, Staff, Patient, Appointment
# Create the dentist office
murray_dental = DentistOffice("Murray Dentists")
# Create a staff object
staff_amir = Staff(office=murray_dental, name="Amir", position="Front office staff")
murray_dental.add_staff(staff_amir)
# create a patient object
patient1 = Patient(patient_name= 'solomon', 
                      phone='270-111-2222', 
                      address='123 Lake Dr Murray',
                      date_of_birth=datetime.datetime.strptime('1/1/1970', '%m/%d/%Y'))

staff_amir.register_patient(patient1)
patient2 = Patient(patient_name= 'Lance', 
                      phone='270-111-3333', 
                      address='345 Lake Dr Murray',
                      date_of_birth=datetime.datetime.strptime('1/1/1980', '%m/%d/%Y'))
staff_amir.register_patient(patient2)
# update patient object
print(murray_dental.list_patients())
staff_amir.update_patient_info(old_name='Lance', new_name='Lin')
print(murray_dental.list_patients())
# Create an appointment
appointment1 = Appointment(patient=patient1,when='Monday 4/14/2025 10:00 am', reason='Dental Cleaning')
staff_amir.book_appointment(appointment1)
print(murray_dental.list_appointments())

staff_amir.cancel_patient_appointment('solomon')
print(murray_dental.list_appointments())

