class MainMenuView:
    def user_choice(self):
        return input(
            "\nBienvenue sur le logiciel CRM de Epic Events, que souhaitez vous faire ?\n"
            "1 - Se connecter\n"
            "2 - Quitter\n"
        )

    def custom_input(self, message):
        return input(message)

    def custom_print(self, message):
        return print(message)