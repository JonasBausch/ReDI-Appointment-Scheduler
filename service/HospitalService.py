from datetime import datetime

from model.AppointmentRequest import AppointmentRequest
from model.Client import Client
from model.Doctor import AvailableTimeSlot
from model.Hospital import Hospital


class HospitalService:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.clients = []
        self.appointment_requests = []

    def add_client(self, name: str, date_of_birth: datetime, existing_conditions: list, languages: list):
        client = Client(name, date_of_birth, existing_conditions, languages)
        self.clients.append(client)

    def get_hospital_information(self):
        return f'{self.hospital}'

    def book_appointment(self, client: Client, available_time_slot: AvailableTimeSlot):
        appointment_request = AppointmentRequest(client, available_time_slot.doctor, available_time_slot.date_time_from,
                                                 available_time_slot.date_time_to)
        self.appointment_requests.append(appointment_request)
        available_time_slot.doctor.remove_available_time_slot(available_time_slot)
        print(f'Created new appointment request {appointment_request}')

    def get_available_slots(self, client: Client, date_time_from: datetime, date_time_to: datetime):
        matching_slots = []
        other_slots = []
        for department in self.hospital.departments:
            for doctor in department.doctors:
                if self.has_common_element(doctor.languages, client.languages):
                    for available_time_slot in doctor.available_time_slots:
                        if self.is_within_range(available_time_slot, date_time_from, date_time_to):
                            if self.has_common_element(doctor.get_conditions(), client.existing_conditions):
                                matching_slots.append(available_time_slot)
                            else:
                                other_slots.append(available_time_slot)
        return matching_slots + other_slots

    @staticmethod
    def is_within_range(available_time_slot, date_time_from, date_time_to):
        return available_time_slot.date_time_from <= date_time_from <= date_time_to <= available_time_slot.date_time_to

    @staticmethod
    def has_common_element(list1, list2):
        result = False
        for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
        return result
