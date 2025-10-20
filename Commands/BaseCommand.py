from abc import ABC, abstractmethod

from Data_structures.StateMachine import StateMachine


class Command(ABC):
    def __init__(self, behaviour: StateMachine):
        self.isActive = False
        self.state_machine = behaviour

    def called(self):  # Hands control of messaging to the command
        self.isActive = True
        self.attempt_termination()
        while self.isActive:
            self.ask(self.state_machine.get_output())
            self.attempt_termination()

    def ask(self, question):
        self.state_machine.next_state(input(question))

    def attempt_termination(self):
        if self.state_machine.can_exit():
            self.terminate()

    def terminate(self):  # Hands control of messaging back to main
        print(self.state_machine.get_output())
        self.state_machine.reset()
        self.isActive = False
        print("Command terminated")
