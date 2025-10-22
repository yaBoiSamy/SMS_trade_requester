from abc import ABC, abstractmethod

import Global_Variables
from Data_structures.StateMachine import StateMachine


class Command(ABC, ):
    def __init__(self, behaviour: StateMachine, login_required, on_termination=None):
        self.isActive = False
        self.LOGIN_REQUIRED = login_required
        self.state_machine = behaviour
        self.on_termination = on_termination

    def called(self):  # Hands control of messaging to the command
        if self.LOGIN_REQUIRED and not Global_Variables.logged_in:
            print("Login required")
            return
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
        if self.on_termination is not None:
            self.on_termination()
        self.state_machine.reset()
        self.isActive = False
        print("Command terminated")
