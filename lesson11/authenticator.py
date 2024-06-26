from datetime import datetime
from exceptions import AuthorizationError, RegistrationError, ValidationError
from validator import Validator
import os.path
import json

file_path = os.path.dirname(os.path.abspath(__file__))+"/auth.json"


class Authenticator:

    def __init__(self):
        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0
        if self._is_auth_file_exist():
            self._read_auth_file()

    def _is_auth_file_exist(self) -> bool:
        return os.path.exists(file_path)

    def _read_auth_file(self):
        with open(file_path, "r") as file:
            auth_data = json.load(file)
        self.login = auth_data.get('login')
        self._password = auth_data.get('_password')
        self.last_success_login_at = datetime.fromisoformat(
            auth_data.get('last_success_login_at'))
        self.errors_count = int(auth_data.get('errors_count'))

    def _update_auth_file(self):
        with open(file_path, "w") as file:
            json.dump({
                'login': self.login,
                '_password': self._password,
                'last_success_login_at': self.last_success_login_at,
                'errors_count': self.errors_count
            }, file, indent=4, sort_keys=True, default=str)

    def authorize(self, login, password):
        if self.login == None:
            raise AuthorizationError("Authorization error!")
        try:
            if self.login != login and self._password != password:
                raise AuthorizationError("Incorrect auth data")
            self.errors_count = 0
            self.last_success_login_at = datetime.now()
            self._update_auth_file()
            print("successful login")
        except AuthorizationError:
            self.errors_count += 1
            self._update_auth_file()

    def registrate(self, login, password):
        validator = Validator()
        if self._is_auth_file_exist():
            raise RegistrationError
        validator.validate_password(password)
        if self.login == None:
            self.login = login
            self._password = password
            self.last_success_login_at = datetime.now()
            self._update_auth_file()
        else:
            raise RegistrationError
