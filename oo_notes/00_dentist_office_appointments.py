"""
This application demonstrates Object oriented development.
It uses Patients and Appointments data.
It has some code for testing the functionality
"""
class User(object):
    def __init__():
        pass
    
class Patient(object):
    def __init__ (self, name, phone='123-999-0010'):
        self.name = name
        self.phone = phone
    def update(self, newName, newPhone):
        self.name = newName
        self.phone = newPhone

    @property
    def details(self):
        return self.name + '(' + self.phone + ')'

class Appointment(object):
    def __init__(self, forWhom, when, forWhat):
        self.patient = forWhom
        self.appointmentTime = when
        self.description = forWhat
    @property
    def details(self):
        return (self.patient.details + self.appointmentTime + self.description)

def printList(inputList):
    for item in inputList:
        print(item.details)

def addNewAppointment(newAppointment, appointments):
    # check if the time is taken
    # if not add it to the list
    # if taken, respond with a note
    for appointment in appointments:
        if newAppointment.appointmentTime == appointment.appointmentTime:
            return 'Sorry the time is already taken'
    appointments.append(newAppointment)
    return 'Appointment has been noted'

def cancelAppointment(oldAppointment, appointments):
    appointments.remove(oldAppointment)


if __name__ == '__main__':
    patients = []
    appointments = []
    pat1 = Patient('Solomon', '234-090-0901')
    patients.append(pat1)
    print(pat1)
    pat2 = Patient('Antony')
    patients.append(pat2)
    printList(patients)
    pat1.update('Batman', '345-0912-0010')
    printList(patients)
    print(patients[0])
    # seek what time the patient wants
    # check if it is not taken already
    # then assign it
    # else alert the patient
    seekingTime = input('When do you want the appointment for?')
    app1 = Appointment(pat1, seekingTime, "Consulting")
    print(addNewAppointment(app1, appointments))

    seekingTime = input('When do you want the appointment for?')
    app2 = Appointment(pat2, seekingTime, "Consulting")
    print(addNewAppointment(app2, appointments))

    seekingTime = input('When do you want the appointment for?')
    app3 = Appointment(pat2, seekingTime, "Consulting")
    print(addNewAppointment(app3, appointments))
    
    printList(appointments)
    cancelAppointment(app1,appointments)
    printList(appointments)

    user1 = User()
    