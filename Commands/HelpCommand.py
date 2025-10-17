from enum import Enum
from Data_structures.StateMachine import StateMachine
from Commands.Command import Command
from Data_structures.SingletonPattern import Singleton
import BotResponses as br


class HelpCommand(Command, metaclass=Singleton):
    class HelpStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = {}
        response_map = {
            HelpCommand.HelpStates.INIT : br.HELP_INTRO
        }
        init_state = HelpCommand.HelpStates.INIT
        final_states = {HelpCommand.HelpStates.INIT}
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm)

    def parse_user_input_to_state_machine_input(self, user_input: str):
        pass # This command immediately terminates after first message
