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
    
    def find_employee(self):
        return input("\nVeuillez entrer le numéro ID de l'utilisateur: ")
    
    def display_employee_header(self):
        min_widths = [3, 4, 12]
        employee_header = f"\nID{min_widths[0]*" "} | Département{min_widths[1]*" "} | Nom{min_widths[2]*" "} | Email{min_widths[2]*" "}"
        print(employee_header)
        print("-" * len(employee_header))
    
    def display_employee(self, employee: Employee) -> None:
        min_widths = [5, 15]
        print(f"{employee.id:<{min_widths[0]}} | {employee.department:<{min_widths[1]}} | {employee.full_name:<{min_widths[1]}} | {employee.email}")

    def employee_not_found(self):
        return print("Utilisateur non trouvé")

