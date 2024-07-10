from database.models.History import HistoryModel
from database.models.Diagnosis import DiagnosisModel
from database.models.Patient import PatientModel
from database.models.Hospital import HospitalModel
from database.models.Insurance import InsuranceModel

class Generate_Database:
    def __init__(self):
        self.history = HistoryModel()
        self.diagnosis = DiagnosisModel()
        self.patient = PatientModel()
        self.hospital = HospitalModel()
        self.insurance = InsuranceModel()

    def create_tables(self):
        self.hospital.create_table()
        self.patient.create_table()
        self.insurance.create_table()
        self.history.create_table()
        self.diagnosis.create_table()