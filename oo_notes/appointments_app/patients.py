class Patient(object):
  patients_count = 0
  def __init__(self, name, phone, address, 
                date_of_birth, history= []):
    self.name = name
    self.phone = phone
    self.address = address
    self.date_of_birth = date_of_birth
    self.history = history
    Patient.patients_count += 1

  def __repr__(self):
    return(vars(self))

  