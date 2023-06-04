from typing import List
from model.Doctor import Doctor


class Department:
    def __init__(self, name: str, doctors: List[Doctor]):
        self.name = name
        self.doctors = doctors

    def __repr__(self):
        return f'\nDepartment Name: {self.name}\n' \
               f'Doctors: {str(self.doctors)}\n'
