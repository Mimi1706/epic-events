from pytest_mock import MockerFixture
from models.event import Event
from models.contract import Contract
from models.employee import Employee
from controllers.event import EventController
from io import StringIO


def test_find_event(mocker: MockerFixture, mock_event: Event):
    mocker.patch("builtins.input", return_value=mock_event.id)
    found_event = EventController().find_event()
    assert found_event is not None
    assert found_event.id == mock_event.id
    assert found_event.name == mock_event.name


def test_create_event(
    mocker: MockerFixture, mock_contract: Contract, mock_employee: Employee
):
    event_data = Event(
        contract_id=mock_contract.id,
        name="Anniversaire surprise",
        start_date="17/06/2025",
        end_date="17/06/2025",
        location="Paris",
        attendees="10",
        notes="Apporter un gâteau au chocolat et des ballons",
        management_employee_id=mock_employee.id,
        support_employee_id=mock_employee.id,
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            event_data.contract_id,
            event_data.name,
            event_data.start_date,
            event_data.end_date,
            event_data.location,
            event_data.attendees,
            event_data.notes,
            event_data.management_employee_id,
            event_data.support_employee_id,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EventController().create_event()
    assert mock_print.getvalue().strip() == "Évènement créé !"


def test_update_event(mocker: MockerFixture, mock_event: Event):
    mocker.patch(
        "builtins.input",
        side_effect=[
            mock_event.id,
            mock_event.contract_id,
            mock_event.name,
            "18/06/2025",
            "18/06/2025",
            mock_event.location,
            "10",
            "Apporter un gâteau à la fraise et une pinata",
            mock_event.management_employee_id,
            mock_event.support_employee_id,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EventController().update_event()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Évènement mis à jour !"


def test_delete_event(mocker: MockerFixture, mock_event: Event):
    mocker.patch("builtins.input", side_effect=[mock_event.id, "1"])
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EventController().delete_event()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Évènement supprimé !"
