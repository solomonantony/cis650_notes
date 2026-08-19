INSERT INTO Physician (physician_name, physician_phone, physician_specialty) VALUES
('Dr. Alice Johnson', '123-456-7890', 'Cardiology'),
('Dr. Bob Smith', '234-567-8901', 'Neurology'),
('Dr. Carol Lee', '345-678-9012', 'Dermatology'),
('Dr. David Kim', '456-789-0123', 'Oncology'),
('Dr. Emma Brown', '567-890-1234', 'Pediatrics');

INSERT INTO Patients (patient_name, patient_date_of_birth, patient_diagnosis, patient_medications) VALUES
('John Doe', '1985-03-15', 'Hypertension', 'Lisinopril'),
('Jane Doe', '1990-07-22', 'Diabetes', 'Metformin'),
('Sam Wilson', '1978-11-05', 'Asthma', 'Albuterol'),
('Lisa Wong', '2002-05-30', 'Acne', 'Isotretinoin'),
('Paul Smith', '1988-02-17', 'Migraines', 'Topiramate'),
('Sophia Garcia', '2015-12-09', 'Allergies', 'Cetirizine'),
('Luke Martinez', '1965-10-14', 'Heart Disease', 'Atorvastatin'),
('Emily Chen', '1993-09-08', 'Anxiety', 'Sertraline'),
('Daniel Patel', '2001-04-23', 'Psoriasis', 'Adalimumab'),
('Olivia Johnson', '1998-06-18', 'Depression', 'Escitalopram');

INSERT INTO Prescription (patient_id, physician_id, dosage, start_date, end_date) VALUES
(1, 1, '10 mg once daily', '2024-01-01', '2024-06-01'),
(2, 2, '500 mg twice daily', '2024-02-01', '2024-08-01'),
(3, 3, '2 puffs as needed', '2024-03-01', NULL),
(4, 4, '20 mg once daily', '2024-04-01', '2024-10-01'),
(5, 2, '25 mg daily', '2024-05-01', '2024-11-01'),
(6, 5, '5 mg daily', '2024-06-01', NULL),
(7, 1, '40 mg once daily', '2024-07-01', '2025-01-01'),
(8, 3, '50 mg daily', '2024-08-01', '2025-02-01'),
(9, 4, '40 mg bi-weekly', '2024-09-01', '2025-03-01'),
(10, 5, '10 mg daily', '2024-10-01', NULL),
(1, 1, '20 mg daily', '2024-01-15', '2024-07-15'),
(2, 2, '500 mg daily', '2024-02-15', '2024-08-15'),
(3, 3, '2 puffs daily', '2024-03-15', '2024-09-15'),
(4, 4, '30 mg once daily', '2024-04-15', '2024-10-15'),
(5, 2, '50 mg daily', '2024-05-15', '2024-11-15'),
(6, 5, '1 pill daily', '2024-06-15', '2024-12-15'),
(7, 1, '60 mg daily', '2024-07-15', NULL),
(8, 3, '5 mg daily', '2024-08-15', '2025-02-15'),
(9, 4, '75 mg daily', '2024-09-15', '2025-03-15'),
(10, 5, '15 mg daily', '2024-10-15', '2025-04-15');
