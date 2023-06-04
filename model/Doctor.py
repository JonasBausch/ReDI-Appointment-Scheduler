from typing import List
from model.AvailableTimeSlot import AvailableTimeSlot
from model.Language import Language
from model.Qualification import Qualification


class Doctor:
    def __init__(self, name: str, gender: str, qualifications: List[Qualification], languages: List[Language],
                 available_time_slots: List[AvailableTimeSlot]):
        self.name = name
        self.gender = gender
        self.qualifications = qualifications
        self.languages = languages
        self.available_time_slots = available_time_slots

    def __repr__(self):
        return f'Dr. {self.name} ({self.gender})\n' \
               f'Qualifications: {self.qualifications}\n' \
               f'Spoken Languages: {self.languages}\n' \
               f'Available Time Slots: {self.available_time_slots}\n'
