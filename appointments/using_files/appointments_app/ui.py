# user interface to use the application
import datetime
import os
from dentist_office import DentistOffice, Staff, Patient, Appointment

def load_data():
    office = DentistOffice('Murray Dentists')
    folder = 'C:/Users/santony/temp/cis650_notes/'
    patients = office.load_patients_data(folder+'oo_notes/appointments_app/data/patients.csv', 'csv')
    if patients: 
        print(f'{len(patients)} patients records loaded')
    else:
        print('Error loading patients')
    appointments = office.load_appointments(folder+'oo_notes/appointments_app/data/appointments.csv', 'csv')
    if appointments:
        print(f'{len(appointments)} appointments loaded')
    else:
        print('Error loading appointments')
    return office

def main():
    while True:
        choice = input("""
                 1. Load data\n
                 2. Manage patient data\n
                 3. Manage appointments\n
                 4. Run reports\n
                 0. Exit
                 >>>  """)
        match choice:
            case '1':
                murray_dentist = load_data()
                print(f'{len(murray_dentist.patients)} patients loaded')
            case '0':
                break
        x = input("Press enter to continue...")
        os.system("cls")

main()





        


