from views.client import ClientView
from utils.employee import check_permissions

class ClientController:
    def __init__(self):
        self.view = ClientView()

    def display_menu(self):
        allowed_actions = check_permissions()
        while True:
            user_input = self.view.display_menu()
            if user_input == "1" and 'READ' in allowed_actions:
                pass
            elif user_input == "2" and 'READ' in allowed_actions:
                pass
            elif user_input == "3" and 'CREATE' in allowed_actions:
                pass
            elif user_input == "4" and 'UPDATE' in allowed_actions:
                pass
            elif user_input == "5" and 'DELETE' in allowed_actions:
                pass
            elif user_input == "6":
                break

