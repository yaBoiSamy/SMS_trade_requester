from enum import Enum

from Commands.Base.BaseCommand import Command
from Data_structures.StateMachine import StateMachine
from Commands.LOGIN import LoginResponses as br
from Private_Constants import PASSWORD
import Global_Variables


class LoginCommand(Command):
    MAX_AUTHORIZED_ATTEMPTS = 5

    class LoginStates(Enum):
        INIT = 0
        INVALID_PASSWORD = 1
        LOCKED_OUT = 2
        VALID_PASSWORD = 3

    def __init__(self):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = LoginCommand.LoginStates.INIT
        final_states = {
            LoginCommand.LoginStates.VALID_PASSWORD,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, False)
        self.remaining_login_attempts = LoginCommand.MAX_AUTHORIZED_ATTEMPTS

    def parse_user_input(self, user_input):
        match self.state_machine.current_state:
            case LoginCommand.LoginStates.INIT: return self.validate_password(user_input)
            case LoginCommand.LoginStates.INVALID_PASSWORD: return self.validate_password(user_input)
            case LoginCommand.LoginStates.LOCKED_OUT: return LoginCommand.LoginStates.LOCKED_OUT

    def perform_response(self):
        match self.state_machine.current_state:
            case LoginCommand.LoginStates.INIT: return br.INTRO
            case LoginCommand.LoginStates.INVALID_PASSWORD: return br.INVALID_PASSWORD(self.remaining_login_attempts)
            case LoginCommand.LoginStates.LOCKED_OUT: return br.LOCKED_OUT
            case LoginCommand.LoginStates.VALID_PASSWORD: return br.VALID_PASSWORD

    def validate_password(self, user_password):
        if user_password == PASSWORD:
            self.remaining_login_attempts = LoginCommand.MAX_AUTHORIZED_ATTEMPTS
            Global_Variables.logged_in = True
            return LoginCommand.LoginStates.VALID_PASSWORD
        self.remaining_login_attempts -= 1
        if self.remaining_login_attempts <= 0:
            return LoginCommand.LoginStates.LOCKED_OUT
        return LoginCommand.LoginStates.INVALID_PASSWORD


