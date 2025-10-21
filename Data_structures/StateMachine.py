

class StateMachine:
    def __init__(self, state_changer, output_actor, init_state, final_states):
        self.state_changer = state_changer
        self.output_actor = output_actor
        self.init_state = init_state
        self.final_states = final_states
        self.current_state = self.init_state

    def next_state(self, transition_input):
        self.current_state = self.state_changer(transition_input)

    def reset(self):
        self.current_state = self.init_state

    def get_output(self):
        return self.output_actor()

    def can_exit(self):
        return self.current_state in self.final_states


