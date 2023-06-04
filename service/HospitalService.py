from model.Hospital import Hospital


class HospitalService:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.appointment_requests = []

    def get_hospital_information(self):
        return f'Hospital Information:\n' \
               f'{self.hospital}'

    def book_appointment(self):
        print("TODO: implement")

