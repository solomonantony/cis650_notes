# user interface to use the application
import datetime
from dentist_office import DentistOffice, Staff, Patient, Appointment
murray_dentist = DentistOffice('Murray Dentists')
folder = 'C:/Users/santony/temp/cis650_notes/'
patients = murray_dentist.load_patients_data(folder+'oo_notes/appointments_app/data/patients.csv', 'csv')
if patients: 
    print(f'{len(patients)} patients records loaded')
else:
    print('Error loading patients')
appointments = murray_dentist.load_appointments(folder+'oo_notes/appointments_app/data/appointments.csv', 'csv')
if appointments:
    print(f'{len(appointments)} appointments loaded')
else:
    print('Error loading appointments')
#print(appointments)

