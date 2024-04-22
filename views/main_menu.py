class MainMenuView:
    def unlogged_user_choice(self):
        return input(
            "\nBienvenue sur le logiciel CRM de Epic Events, que souhaitez vous faire ?\n"
            "1 - Se connecter\n"
            "2 - Quitter\n"
        )

    def logged_user_choice(self, employee_full_name):
        return input(
            f"\nBienvenue {employee_full_name}, que souhaitez-vous faire ?\n"
            "1 - Gérer les utilisateurs\n"
            "2 - Gérer les clients\n"
            "3 - Gérer les contrats\n"
            "4 - Gérer les évènements\n"
            "5 - Quitter\n"
        )

    def selection_error_msg(self):
        print("Erreur de sélection, veuillez sélectionner une option valide.")

    def goodbye_msg(self):
        print("À bientôt !\n")

    def failed_login_msg(self):
        print("Nom d'utilisateur et/ou mot de passe erroné.")

    def unauthorized_msg(self):
        print("Accès non autorisé.")
