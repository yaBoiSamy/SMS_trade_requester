from enum import Enum

from Commands.Base.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Commands.STATUS import StatusResponses as br


class StatusCommand(Command):
    class StatusStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = StatusCommand.StatusStates.INIT
        final_states = {
            StatusCommand.StatusStates.INIT,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True)

    def parse_user_input(self, user_input):
        # match self.state_machine.current_state:
        #     case StatusCommand.StatusStates.INIT:
        pass

    def perform_response(self):
        match self.state_machine.current_state:
            case StatusCommand.StatusStates.INIT: return br.INTRO

