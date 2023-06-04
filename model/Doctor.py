from datetime import datetime
from typing import List
from model.Language import Language
from model.Qualification import Qualification


class Doctor:
    def __init__(self, name: str, gender: str, qualifications: List[Qualification], languages: List[Language]):
        self.name = name
        self.gender = gender
        self.qualifications = qualifications
        self.languages = languages
        self.available_time_slots = []

    def add_available_time_slot(self, date_time_from: datetime, date_time_to: datetime):
        self.available_time_slots.append(AvailableTimeSlot(self, date_time_from, date_time_to))

    def remove_available_time_slot(self, available_time_slot):
        self.available_time_slots.remove(available_time_slot)

    def get_conditions(self):
        conditions = []
        for qualification in self.qualifications:
            for condition in qualification.related_conditions:
                conditions.append(condition)
        return conditions

    def __repr__(self):
        return f'\nDr. {self.name} ({self.gender})\n' \
               f'Qualifications: {self.qualifications}\n' \
               f'Spoken Languages: {self.languages}\n' \
               f'Available Time Slots: {self.available_time_slots}'


class AvailableTimeSlot:
    def __init__(self, doctor: Doctor, date_time_from: datetime, date_time_to: datetime):
        self.doctor = doctor
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to

    def __repr__(self):
        return f'\nDr. {self.doctor.name} is available from {self.date_time_from} to {self.date_time_to}'
