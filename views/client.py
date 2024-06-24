from utils.employee import check_permissions
from models import Client


class ClientView:
    def display_menu(self):
        allowed_actions = check_permissions("CLIENT")
        menu_options = ["\n1 - Voir la liste des clients"]
        if "READ" in allowed_actions:
            menu_options.append("2 - Chercher un client")
        if "CREATE" in allowed_actions:
            menu_options.append("3 - Créer un client")
        if "UPDATE" in allowed_actions:
            menu_options.append("4 - Mettre à jour un client")
        if "DELETE" in allowed_actions:
            menu_options.append("5 - Effacer un client")
        menu_options.append("6 - Retour\n")
        return input("\n".join(menu_options))

    def display_client(self, client: Client):
        return print(
            f"\nID Client : {client.id}\n"
            f"Compagnie : {client.company_name}\n"
            f"Nom/Prénom : {client.full_name}\n"
            f"Email : {client.email}\n"
            f"Tél. : {client.phone_number}\n"
            f"ID commercial : {client.sales_employee_id}"
        )

    def find_client(self):
        return input("\nVeuillez entrer le numéro ID du client: ")

    def client_not_found(self):
        return print("Client non trouvé.")

    def edit_client(self):
        company_name = input("\nNom de la compagnie : ")
        full_name = input("Nom/Prénom du client : ")
        email = input("Email : ")
        phone_number = input("Numéro de téléphone : ")
        sales_employee_id = input("Numéro de l'employé (commercial) : ")
        return company_name, full_name, email, phone_number, sales_employee_id

    def create_client_success(self):
        return print("Client créé !")

    def edit_client_error(self):
        return print("Erreur, veuillez vérifier les champs et réessayer.")

    def update_client_success(self):
        return print("Client mis à jour !")

    def delete_client_confirm(self):
        return input("\nSouhaitez-vous supprimer ce client ?" "\n1 - Oui" "\n2 - Non\n")

    def delete_client_success(self):
        return print("Client supprimé !")
