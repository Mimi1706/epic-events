from views.contract import ContractView
from models import Contract
from typing import List
from database import session
from utils.employee import check_permissions
from utils.queries import get_employee, get_client
from datetime import datetime


class ContractController:
    def __init__(self):
        self.view = ContractView()

    def display_menu(self):
        allowed_actions = check_permissions()
        while True:
            user_input = self.view.display_menu()
            if user_input == "1" and "READ" in allowed_actions:
                self.read_contracts()
            elif user_input == "2" and "READ" in allowed_actions:
                self.find_contract()
            elif user_input == "3" and "CREATE" in allowed_actions:
                self.create_contract()
            elif user_input == "4" and "UPDATE" in allowed_actions:
                self.update_client()
            elif user_input == "5" and "DELETE" in allowed_actions:
                self.delete_contract()
            elif user_input == "6":
                break

    def read_contracts(self):
        contracts: List[Contract] = session.query(Contract).all()
        for contract in contracts:
            self.view.display_contract(contract)

    def find_contract(self):
        user_input = self.view.find_contract()
        contract = session.query(Contract).filter(Contract.id == user_input).first()
        if contract:
            self.view.display_contract(contract)
            return contract
        else:
            self.view.contract_not_found()

    def get_status_from_input(self, input_value):
        status = {"1": "validé", "2": "en attente", "3": "annulé"}
        return status[input_value]

    def create_contract(self):
        try:
            (
                client_id,
                status,
                total_amount,
                left_amount,
                sales_employee_id,
                management_employee_id,
            ) = self.view.edit_contract()

            if (
                get_employee(sales_employee_id)
                and get_employee(sales_employee_id)
                and get_client(client_id)
                and status in {"1", "2", "3"}
            ):
                contract = Contract(
                client_id=client_id,
                status=self.get_status_from_input(status),
                total_amount=total_amount,
                left_amount=left_amount,
                sales_employee_id=sales_employee_id,
                management_employee_id=management_employee_id,
                created_on=datetime.now(),
                )

                session.add(contract)
                session.commit()
                self.view.create_contract_success()
            else:
                self.view.edit_contract_error()
        except:
            self.view.edit_contract_error()

    def update_client(self):
        contract = self.find_contract()
        if contract:
            try:
                (
                    client_id,
                    status,
                    total_amount,
                    left_amount,
                    sales_employee_id,
                    management_employee_id,
                ) = self.view.edit_contract()

                if (
                    get_employee(sales_employee_id)
                    and get_employee(management_employee_id)
                    and get_client(client_id) and status in {"1", "2", "3"}
                ):
                    contract.client_id = client_id
                    contract.status = status
                    contract.total_amount = total_amount
                    contract.left_amount = left_amount
                    contract.sales_employee_id = sales_employee_id
                    contract.management_employee_id = management_employee_id
                    session.commit()
                    self.view.update_contract_success()
                else:
                    self.view.edit_contract_error()
            except:
                self.view.edit_contract_error()

    def delete_contract(self):
        contract = self.find_contract()
        if contract:
            confirm_input = self.view.delete_contract_confirm()
            if confirm_input == "1":
                session.delete(contract)
                session.commit()
                self.view.delete_contract_success()
