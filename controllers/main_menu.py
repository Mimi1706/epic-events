from views.main_menu import MainMenuView
from controllers.login import Login

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                Login().display_menu()
            if user_input == "2":
                self.view.custom_print("À bientôt !\n")
                quit()
            else:
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide")
                self.display_menu()