class LoginView:
    def get_username(self):
        return input("\nVeuillez entrer votre identifiant\n")
    
    def get_password(self):
        return input("\nVeuillez entrer votre mot de passe\n")
    
    def expired_session_msg(self):
        return print("Votre session a expiré, veuillez quitter et vous reconnecter.")
    
    def error_msg(self):
        return print("Erreur de session, veuillez contacter le service support.")