from utils.employee import check_permissions
from models import Contract


class ContractView:
    def display_menu(self):
        allowed_actions = check_permissions()
        menu_options = ["\n1 - Voir la liste des contrats"]
        if "READ" in allowed_actions:
            menu_options.append("2 - Chercher un contrat")
        if "CREATE" in allowed_actions:
            menu_options.append("3 - Créer un contrat")
        if "UPDATE" in allowed_actions:
            menu_options.append("4 - Mettre à jour un contrat")
        if "DELETE" in allowed_actions:
            menu_options.append("5 - Effacer un contrat")
        menu_options.append("6 - Retour\n")
        return input("\n".join(menu_options))

    def display_contract(self, contract: Contract):
        return print(
            f"\Contrat ID : {contract.id}\n"
            f"Client ID : {contract.client_id}\n"
            f"Créé le : {contract.created_on}\n"
            f"Montant total : {contract.total_amount}"
            f"Montant restant : {contract.left_amount}"
            f"Statut : {contract.status}"
            f"ID commercial : {contract.sales_employee_id}"
            f"ID gestion : {contract.management_employee_id}"
        )

    def find_contract(self):
        return input("\nVeuillez entrer le numéro ID du contrat: ")

    def contract_not_found(self):
        return print("contrat non trouvé.")

    def edit_contract(self):
        client_id = input("\nID Client : ")
        status = input("Statut : ")
        total_amount = input("Montant total : ")
        left_amount = input("Montant restant : ")
        sales_employee_id = input("ID Commercial : ")
        management_employee_id = input("ID Gestion")
        return (
            client_id,
            status,
            total_amount,
            left_amount,
            sales_employee_id,
            management_employee_id,
        )

    def create_contract_success(self):
        return print("Contrat créé !")
    
    def edit_contract_error(self):
        return print("Erreur, veuillez vérifier les champs et réessayer.")

    def update_contract_success(self):
        return print("Contrat mis à jour !")

    def delete_contract_confirm(self):
        return input(
            "\nSouhaitez-vous supprimer ce Contrat ?" "\n1 - Oui" "\n2 - Non\n"
        )

    def delete_contract_success(self):
        return print("Contrat supprimé !")
