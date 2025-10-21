from enum import Enum

from Commands.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Data_structures.Logger import Logger


class LogsCommand(Command, metaclass=Singleton):
    class LogsStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = None
        response_map = self.perform_response
        init_state = LogsCommand.LogsStates.INIT
        final_states = {
            LogsCommand.LogsStates.INIT,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True)

    def perform_response(self):
        match self.state_machine.current_state:
            case LogsCommand.LogsStates.INIT: return Logger().get_logs()
