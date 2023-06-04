from datetime import datetime

from model.Condition import Condition
from model.Department import Department
from model.Doctor import Doctor
from model.Hospital import Hospital
from model.Language import Language
from model.Qualification import Qualification


def create_test_hospital():
    headache = Condition("headache")
    back_pain = Condition("back pain")
    copd = Condition("copd")
    conditions = [headache, back_pain, copd]
    languages = [Language.ENGLISH, Language.GERMAN]
    qualification1 = Qualification("someCertificate", conditions)
    doctor1 = Doctor("John Doe", "male", [qualification1], languages)
    doctor1.add_available_time_slot(datetime(2023, 6, 4, 8, 30), datetime(2023, 6, 6, 9, 0))
    department1 = Department("Geriatrics", [doctor1])
    return Hospital("Isarkrankenhaus", [department1])

def create_test_patients(hospital_service):
    headache = Condition("headache")
    back_pain = Condition("back pain")
    copd = Condition("copd")
    existing_conditions = [headache, back_pain, copd]
    languages = [Language.ENGLISH, Language.GERMAN]
    hospital_service.add_client("Jonas Bausch", datetime(1988, 5, 22), existing_conditions, languages)
    hospital_service.add_client("Homer Simpson", datetime(1988, 5, 22), existing_conditions, languages)
