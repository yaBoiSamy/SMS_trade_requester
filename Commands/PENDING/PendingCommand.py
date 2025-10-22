from enum import Enum

from Commands.Base.BaseCommand import Command
from Data_structures.StateMachine import StateMachine
from Commands.PENDING import PendingResponses as br


class PendingCommand(Command):
    class PendingStates(Enum):
        INIT = 0

    def __init__(self):
        transitions = None
        response_map = self.perform_response
        init_state = PendingCommand.PendingStates.INIT
        final_states = {
            PendingCommand.PendingStates.INIT
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True)

    def perform_response(self):
        match self.state_machine.current_state:
            case PendingCommand.PendingStates.INIT: return br.INTRO
