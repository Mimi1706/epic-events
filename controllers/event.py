from views.event import EventView
from utils.employee import check_permissions
from utils.queries import get_employee, get_contract
from models import Event
from typing import List
from database import session
from datetime import datetime


class EventController:
    def __init__(self):
        self.view = EventView()

    def display_menu(self):
        allowed_actions = check_permissions()
        while True:
            user_input = self.view.display_menu()
            if user_input == "1" and "READ" in allowed_actions:
                self.read_events()
            elif user_input == "2" and "READ" in allowed_actions:
                self.find_event()
            elif user_input == "3" and "CREATE" in allowed_actions:
                self.create_event()
            elif user_input == "4" and "UPDATE" in allowed_actions:
                self.update_event()
            elif user_input == "5" and "DELETE" in allowed_actions:
                self.delete_event()
            elif user_input == "6":
                break

    def read_events(self):
        events: List[Event] = session.query(Event).all()
        for event in events:
            self.view.display_event(event)

    def find_event(self):
        user_input = self.view.find_event()
        event = session.query(Event).filter(Event.id == user_input).first()
        if event:
            self.view.display_event(event)
            return event
        else:
            self.view.event_not_found()

    def create_event(self):
        try:
            (
                contract_id,
                name,
                start_date,
                end_date,
                location,
                attendees,
                notes,
                management_employee_id,
                support_employee_id,
            ) = self.view.edit_event()

            if (
                get_contract(contract_id)
                and get_employee(management_employee_id)
                and get_employee(support_employee_id)
            ):
                event = Event(
                contract_id=contract_id,
                name=name,
                start_date=datetime.strptime(start_date, "%d/%m/%Y"),
                end_date=datetime.strptime(end_date, "%d/%m/%Y"),
                location=location,
                attendees=attendees if attendees.isdigit() else 0,
                notes=notes,
                management_employee_id=management_employee_id,
                support_employee_id=support_employee_id,
                )
                session.add(event)
                session.commit()
                self.view.create_event_success()
            else:
                self.view.edit_event_error()
        except:
            self.view.edit_event_error()

    def update_event(self):
        event = self.find_event()
        if event:
            try:
                (
                    contract_id,
                    name,
                    start_date,
                    end_date,
                    location,
                    attendees,
                    notes,
                    management_employee_id,
                    support_employee_id,
                ) = self.view.edit_event()

                if (
                    get_contract(contract_id)
                    and get_employee(management_employee_id)
                    and get_employee(support_employee_id)
                ):
                    print("helloooooooo1")
                    event.name=name
                    event.contract_id = contract_id
                    event.start_date= datetime.strptime(start_date, "%d/%m/%Y")
                    event.end_date = datetime.strptime(end_date, "%d/%m/%Y")
                    event.location = location
                    event.attendees = attendees if attendees.isdigit() else 0
                    event.notes = notes
                    event.management_employee_id = management_employee_id
                    event.support_employee_id = support_employee_id
                    print("helloooooooo")
                    session.commit()
                    self.view.create_event_success()
                else:
                    self.view.edit_event_error()
            except:
                self.view.edit_event_error()

    def delete_event(self):
        event = self.find_event()
        if event:
            confirm_input = self.view.delete_event_confirm()
            if confirm_input == "1":
                session.delete(event)
                session.commit()
                self.view.delete_event_success()
