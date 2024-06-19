from datetime import datetime
from exceptions import AuthorizationError
from exceptions import RegistrationError
import os.path

file_path = os.path.dirname(os.path.abspath(__file__))+"/auth.txt"


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
            auth_data = file.readlines()
        self.login = auth_data[0].replace("\n", "")
        self._password = auth_data[1].replace("\n", "")
        self.last_success_login_at = datetime.fromisoformat(
            auth_data[2].replace("\n", ""))
        self.errors_count = int(auth_data[3])

    def _update_auth_file(self):
        with open(file_path, "w") as file:
            file.writelines([str(self.login), "\n",
                            str(self._password), "\n",
                            str(self.last_success_login_at), "\n",
                            str(self.errors_count)])

    def authorize(self, login, password):
        if self.login == None:
            raise AuthorizationError("Authorization error")
        try:
            if self.login != login and self._password != password:
                raise AuthorizationError("Incorrect auth data!")
            self.errors_count = 0
            self.last_success_login_at = datetime.now()
            self._update_auth_file()
            print("successful login")
        except AuthorizationError:
            self.errors_count += 1
            self._update_auth_file()

    def registrate(self, login, password):
        if self._is_auth_file_exist():
            raise RegistrationError("Registration error")
        else:
            if self.login == None:
                self.login = login
                self._password = password
                self.last_success_login_at = datetime.now()
                self._update_auth_file()
            else:
                raise RegistrationError("Registration error")
