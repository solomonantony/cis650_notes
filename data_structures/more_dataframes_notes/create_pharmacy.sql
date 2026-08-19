-- Create the Physician table
CREATE TABLE Physician (
    physician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    physician_name TEXT NOT NULL,
    physician_phone TEXT NOT NULL,
    physician_specialty TEXT NOT NULL
);

-- Create the Patients table
CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    patient_date_of_birth DATE NOT NULL,
    patient_diagnosis TEXT,
    patient_medications TEXT
);

-- Create the Prescription table
CREATE TABLE Prescription (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    physician_id INTEGER NOT NULL,
    dosage TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id) ON DELETE CASCADE,
    FOREIGN KEY (physician_id) REFERENCES Physician (physician_id) ON DELETE CASCADE
);
