import re
from exceptions import ValidationError


class Validator:

    def __init__(self):
        self.regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

    def validate_password(self, password):
        if re.match(self.regex, password) is None:
            raise ValidationError("Incorrect password format")
