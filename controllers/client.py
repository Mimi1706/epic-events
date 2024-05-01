from views.client import ClientView
from utils.employee import check_permissions, retrieve_payload_session
from utils.queries import get_employee
from typing import List
from models import Client
from database import session
from datetime import datetime


class ClientController:
    def __init__(self):
        self.view = ClientView()
        self.payload = retrieve_payload_session()

    def display_menu(self):
        allowed_actions = check_permissions()
        while True:
            user_input = self.view.display_menu()
            if user_input == "1" and "READ" in allowed_actions:
                self.read_clients()
            elif user_input == "2" and "READ" in allowed_actions:
                self.find_client()
            elif user_input == "3" and "CREATE" in allowed_actions:
                self.create_client()
            elif user_input == "4" and "UPDATE" in allowed_actions:
                self.update_client()
            elif user_input == "5" and "DELETE" in allowed_actions:
                self.delete_client()
            elif user_input == "6":
                break

    def read_clients(self):
        clients: List[Client] = session.query(Client).all()
        sorted_clients: List[Client] = sorted(
            clients, key=lambda client: client.company_name
        )
        for client in sorted_clients:
            self.view.display_client(client)

    def find_client(self):
        user_input = self.view.find_client()
        client = session.query(Client).filter(Client.id == user_input).first()
        if client:
            self.view.display_client(client)
            return client
        else:
            self.view.client_not_found()

    def create_client(self):
        (
            company_name,
            full_name,
            email,
            phone_number,
            sales_employee_id,
        ) = self.view.edit_client()
        client = Client(
            company_name=company_name,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            sales_employee_id=sales_employee_id,
            created_on=datetime.now(),
            updated_on=datetime.now(),
        )
        if get_employee(sales_employee_id) and client:
            session.add(client)
            session.commit()
            self.view.create_client_success()
        else:
            self.view.edit_client_error()

    def update_client(self):
        client = self.find_client()
        if client:
            (
                company_name,
                full_name,
                email,
                phone_number,
                sales_employee_id,
            ) = self.view.edit_client()

            if get_employee(sales_employee_id):
                client.company_name = company_name
                client.full_name = full_name
                client.email = email
                client.phone_number = phone_number
                client.sales_employee_id = sales_employee_id
                session.commit()
                self.view.update_client_success()
            else:
                self.view.edit_client_error()

    def delete_client(self):
        client = self.find_client()
        if client:
            confirm_input = self.view.delete_client_confirm()
            if confirm_input == "1":
                session.delete(client)
                session.commit()
                self.view.delete_client_success()
