class LoginView:
    def get_username(self):
        return input(
            "\nVeuillez entrer votre identifiant\n"
        )
    
    def get_password(self):
        return input("\nVeuillez entrer votre mot de passe\n")

    def custom_input(self, message):
        return input(message)

    def custom_print(self, message):
        return print(message)