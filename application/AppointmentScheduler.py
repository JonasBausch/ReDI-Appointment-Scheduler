from datetime import datetime

from application.AppointmentSchedulerAction import AppointmentSchedulerAction
from model.AvailableTimeSlot import AvailableTimeSlot
from service.HospitalService import HospitalService
from model.Client import Client
from model.Condition import Condition
from model.Department import Department
from model.Doctor import Doctor
from model.Hospital import Hospital
from model.Language import Language
from model.Qualification import Qualification


class AppointmentScheduler:
    def __init__(self):
        self.clients = []
        hospital = self.seed_test_data()
        self.hospital_service = HospitalService(hospital)
        self.start_application()

    def start_application(self):
        selected_action = self.list_actions()
        while selected_action:
            if selected_action == 1:
                pass
            elif selected_action == 2:
                self.add_client()
            elif selected_action == 3:
                self.list_clients()
            elif selected_action == 4:
                self.book_appointment()
            elif selected_action == 5:
                self.print_hospital_information()
            elif selected_action == 6:
                print('Exiting...')
                quit()
            else:
                print(f'Action {selected_action} is not supported')
            selected_action = self.list_actions()

    @staticmethod
    def list_actions():
        print('***********************')
        print('** Available Actions **')
        print('***********************')
        print(f'{[action for action in AppointmentSchedulerAction]}')
        return int(input('Please select an action by entering the corresponding number\n'))

    def add_client(self):
        name = input('Please enter the client\'s name: ')
        date_of_birth = input('Please enter the client\'s date of birth: ')
        existing_conditions = input('Please enter the client\'s existing conditions (comma separated): ')
        languages = input('Please enter the client\'s languages (comma separated): ')
        client = Client(name, self.parse_date(date_of_birth), self.parse_conditions(existing_conditions),
                        self.parse_languages(languages))
        self.clients.append(client)

    @staticmethod
    def parse_conditions(to_parse: str):
        raw_conditions = to_parse.split(',')
        conditions = []
        for raw_condition in raw_conditions:
            conditions.append(Condition(raw_condition))
        return conditions

    @staticmethod
    def parse_languages(to_parse: str):
        raw_languages = to_parse.split(',')
        languages = []
        for raw_language in raw_languages:
            languages.append(Language[raw_language])
        return languages

    @staticmethod
    def parse_date(to_parse: str):
        return datetime.strptime(to_parse, '%d-%m-%Y')

    def list_clients(self):
        if self.clients:
            print(str(self.clients))
        else:
            print('No clients registered yet')

    def book_appointment(self):
        self.hospital_service.book_appointment()

    def print_hospital_information(self):
        print(self.hospital_service.get_hospital_information())

    def seed_test_data(self):
        headache = Condition("headache")
        back_pain = Condition("back pain")
        copd = Condition("copd")
        existing_conditions = [headache, back_pain, copd]
        languages = [Language.ENGLISH, Language.GERMAN]
        client = Client("Jonas Bausch", datetime(1988, 5, 22), existing_conditions, languages)
        self.clients.append(client)
        qualification1 = Qualification("someCertificate", [headache])
        available_time_slot1 = AvailableTimeSlot(datetime(2023, 6, 5, 8, 30), datetime(2023, 6, 5, 9, 0))
        doctor1 = Doctor("John Doe", "male", [qualification1], languages, [available_time_slot1])
        department1 = Department("Geriatrics", [doctor1])
        return Hospital("Isarkrankenhaus", [department1])

