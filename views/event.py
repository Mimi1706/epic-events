from utils.employee import check_permissions
from models import Event
from datetime import datetime


class EventView:
    def display_menu(self):
        allowed_actions = check_permissions("EVENT")
        menu_options = ["\n1 - Voir la liste des évènements"]
        if "READ" in allowed_actions:
            menu_options.append("2 - Chercher un évènement")
        if "CREATE" in allowed_actions:
            menu_options.append("3 - Créer un évènement")
        if "UPDATE" in allowed_actions:
            menu_options.append("4 - Mettre à jour un évènement")
        if "DELETE" in allowed_actions:
            menu_options.append("5 - Effacer un évènement")
        if "UPDATE" in allowed_actions:
            menu_options.append("6 - Filtrer par employé")
        menu_options.append("7 - Retour\n")
        return input("\n".join(menu_options))

    def display_event(self, event: Event):
        return print(
            f"\nID Évènement : {event.id}\n"
            f"ID Contrat : {event.contract_id}\n"
            f"Intitulé : {event.name}\n"
            f"Date de début : {datetime.strftime(event.start_date, '%d/%m/%Y')}\n"
            f"Date de fin : {datetime.strftime(event.end_date, '%d/%m/%Y')}\n"
            f"Emplacement : {event.location}\n"
            f"Nombre de participants : {event.attendees}\n"
            f"Notes : {event.notes}\n"
            f"ID gestion : {event.management_employee_id}\n"
            f"ID support : {event.support_employee_id}"
        )

    def find_event(self):
        return input("\nVeuillez entrer le numéro ID de l'évènement : ")

    def filter_event(self):
        return input("Veuillez entrer l'ID de l'employee : ")

    def filter_event_not_found(self):
        return print("Aucun évènement n'est lié à cet employé.")
    
    def filter_event_employee_not_found(self):
        return print("Erreur, employé non trouvé.")

    def event_not_found(self):
        return print("Évènement non trouvé.")

    def edit_event(self):
        contract_id = input("\nID Contrat : ")
        name = input("Intitulé : ")
        start_date = input("Date de début (DD/MM/YYYY) : ")
        end_date = input("Date de fin (DD/MM/YYYY) : ")
        location = input("Emplacement : ")
        attendees = input("Nombre de participants : ")
        notes = input("Notes : ")
        management_employee_id = input("ID gestion : ")
        support_employee_id = input("ID support : ")
        return (
            contract_id,
            name,
            start_date,
            end_date,
            location,
            attendees,
            notes,
            management_employee_id,
            support_employee_id,
        )

    def create_event_success(self):
        return print("Évènement créé !")

    def edit_event_error(self):
        return print("Erreur, veuillez vérifier les champs et réessayer.")

    def update_event_success(self):
        return print("Évènement mis à jour !")

    def delete_event_confirm(self):
        return input(
            "\nSouhaitez-vous supprimer cet évènement ?" "\n1 - Oui" "\n2 - Non\n"
        )

    def delete_event_success(self):
        return print("Évènement supprimé !")
