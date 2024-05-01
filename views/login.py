class LoginView:
    def get_username(self):
        return input("\nVeuillez entrer votre identifiant\n")

    def get_password(self):
        return input("\nVeuillez entrer votre mot de passe\n")

    def wrong_credentials_msg(self):
        return print("\nNom d'utilisateur et/ou mot de passe erroné.")

    def expired_session_msg(self):
        return print("Votre session a expiré, veuillez vous reconnecter.")

    def error_msg(self):
        return print(
            "Erreur de session, veuillez réessayer. Si l'erreur persiste, veuillez contacter le service support."
        )
