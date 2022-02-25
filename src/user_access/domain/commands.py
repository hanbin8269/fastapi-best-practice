from dataclasses import dataclass


class Command:
    pass


@dataclass
class LoginOrSignUp(Command):
    code: str
