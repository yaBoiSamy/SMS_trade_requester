from abc import ABC, abstractmethod

from Data_structures.StateMachine import StateMachine


class Command(ABC):
    def __init__(self, behaviour: StateMachine):
        self.isActive = False
        self.state_machine = behaviour

    def called(self): # Hands control of messaging to the command
        self.isActive = True
        print(self.state_machine.get_output())
        self.attempt_termination()
        self.poll()

    @abstractmethod
    def parse_user_input_to_state_machine_input(self, user_input: str):
        pass

    def respond(self, user_input: str):
        state_machine_input = self.parse_user_input_to_state_machine_input(user_input)
        self.state_machine.next_state(state_machine_input)
        print(self.state_machine.get_output())
        self.attempt_termination()

    def attempt_termination(self):
        if self.state_machine.can_exit():
            self.terminate()

    def terminate(self): # Hands control of messaging back to main
        self.state_machine.reset()
        self.isActive = False
        print("Command terminated")

    def poll(self):
        while self.isActive:
            self.respond(input())


