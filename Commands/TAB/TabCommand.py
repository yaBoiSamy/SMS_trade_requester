from enum import Enum

from Commands.Base.BaseCommand import Command
from Data_structures.StateMachine import StateMachine
from Commands.TAB import TabResponses as br


class TabCommand(Command):
    class TabStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = TabCommand.TabStates.INIT
        final_states = {
            TabCommand.TabStates.INIT,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True)

    def parse_user_input(self, user_input):
        # match self.state_machine.current_state:
        #     case TabCommand.TabStates.INIT:
        pass

    def perform_response(self):
        match self.state_machine.current_state:
            case TabCommand.TabStates.INIT: return br.INTRO

