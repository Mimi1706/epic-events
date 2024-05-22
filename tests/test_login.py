from controllers.login import Login
from pytest import MonkeyPatch
from io import StringIO

monkeypatch = MonkeyPatch()

def test_login():
    user_input = StringIO("test@test.fr\n1\n") 
    monkeypatch.setattr('sys.stdin', user_input)
    login = Login().log_in()
    assert login.full_name == "John"
    monkeypatch.undo()
