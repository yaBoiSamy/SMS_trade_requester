from enum import Enum
from Data_structures.StateMachine import StateMachine
from Commands.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
import Commands.HELP.HelpResponses as br


class HelpCommand(Command, metaclass=Singleton):
    class HelpStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = None
        response_map = self.perform_response
        init_state = HelpCommand.HelpStates.INIT
        final_states = {HelpCommand.HelpStates.INIT}
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, False)

    def perform_response(self):
        match self.state_machine.current_state:
            case HelpCommand.HelpStates.INIT: return br.INTRO
