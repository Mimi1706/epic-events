from models import Employee
from permissions import EMPLOYEE_PERMISSIONS

class EmployeeView:
    def display_menu(self, employee: Employee):
        role_permissions = EMPLOYEE_PERMISSIONS.get(employee.department, {})
        allowed_actions = [action for action, allowed in role_permissions.items() if allowed]
        menu_options = ["\n1 - Voir la liste des utilisateurs"]

        if 'READ' in allowed_actions:
            menu_options.append("2 - Chercher un utilisateur")

        if 'CREATE' in allowed_actions:
            menu_options.append("3 - Créer un utilisateur")

        if 'UPDATE' in allowed_actions:
            menu_options.append("4 - Mettre à jour un utilisateur")

        if 'DELETE' in allowed_actions:
            menu_options.append("5 - Effacer un utilisateur")

        menu_options.append("6 - Retour\n")

        return input("\n".join(menu_options))

