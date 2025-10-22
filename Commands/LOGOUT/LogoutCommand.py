from enum import Enum

from Commands.Base.BaseCommand import Command
from Data_structures.StateMachine import StateMachine
from Commands.LOGOUT import LogoutResponses as br
import Global_Variables


class LogoutCommand(Command):
    class LogoutStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = None
        response_map = self.perform_response
        init_state = LogoutCommand.LogoutStates.INIT
        final_states = {
            LogoutCommand.LogoutStates.INIT: br.INTRO
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, False)

    def perform_response(self):
        match self.state_machine.current_state:
            case LogoutCommand.LogoutStates.INIT:
                Global_Variables.logged_in = False
                return br.INTRO
