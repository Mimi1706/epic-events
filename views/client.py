from utils.employee import check_permissions

class ClientView:
    def display_menu(self):
        allowed_actions = check_permissions()
        menu_options = ["\n1 - Voir la liste des clients"]
        if 'READ' in allowed_actions:
            menu_options.append("2 - Chercher un client")
        if 'CREATE' in allowed_actions:
            menu_options.append("3 - Créer un client")
        if 'UPDATE' in allowed_actions:
            menu_options.append("4 - Mettre à jour un client")
        if 'DELETE' in allowed_actions:
            menu_options.append("5 - Effacer un client")
        menu_options.append("6 - Retour\n")
        return input("\n".join(menu_options))