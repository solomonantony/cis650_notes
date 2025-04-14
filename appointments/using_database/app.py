from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Patient, Appointment
from datetime import datetime, date

# Set up DB
engine = create_engine('sqlite:///clinic.db')
Session = sessionmaker(bind=engine)
session = Session()

# Add new patient
def add_patient():
    print("🔹 Add New Patient")
    name = input("Name: ")
    phone = input("Phone: ")
    medical_history = input("Medical History: ")
    address = input("Address: ")
    dob_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        patient = Patient(
            name=name,
            phone=phone,
            medical_history=medical_history,
            address=address,
            date_of_birth=dob
        )
        session.add(patient)
        session.commit()
        print(f"✅ Patient '{name}' added.\n")
    except Exception as e:
        print(f"❌ Error: {e}")

# List all patients
def list_patients():
    print("📋 List of Patients")
    patients = session.query(Patient).all()
    for p in patients:
        print(f"{p.id}: {p.name}, DOB: {p.date_of_birth}, Phone: {p.phone}")
        print(f"   Address: {p.address}")
        print(f"   History: {p.medical_history}")
    print("")

# Add new appointment
def add_appointment():
    print("🔹 Add Appointment")
    patient_id = int(input("Patient ID: "))
    datetime_str = input("Appointment Time (YYYY-MM-DD HH:MM): ")
    reason = input("Reason: ")
    staff_name = input("Staff Name: ")
    try:
        appointment_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        appt = Appointment(
            patient_id=patient_id,
            appointment_time=appointment_time,
            reason=reason,
            staff_name=staff_name
        )
        session.add(appt)
        session.commit()
        print("✅ Appointment added.\n")
    except Exception as e:
        print(f"❌ Error: {e}")

# List all appointments
def list_appointments():
    print("📋 List of Appointments")
    appts = session.query(Appointment).all()
    for a in appts:
        print(f"{a.id}: {a.appointment_time} - {a.reason} with {a.staff_name}")
        print(f"   Patient: {a.patient.name}")
    print("")

# Menu
def menu():
    while True:
        print("🦷 Dental Clinic Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Appointment")
        print("4. View Appointments")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            list_patients()
        elif choice == "3":
            add_appointment()
        elif choice == "4":
            list_appointments()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.\n")
        input("Press enter to continue...")

if __name__ == "__main__":
    menu()
