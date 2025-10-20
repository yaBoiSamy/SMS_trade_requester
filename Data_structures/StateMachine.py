

class StateMachine:
    def __init__(self, state_changer, output_map, init_state, final_states):
        self.state_changer = state_changer
        self.output_map = output_map
        self.init_state = init_state
        self.final_states = final_states
        self.current_state = self.init_state

    def next_state(self, transition_input):
        self.current_state = self.state_changer(transition_input)

    def reset(self):
        self.current_state = self.init_state

    def get_output(self):
        return self.output_map[self.current_state]

    def can_exit(self):
        return self.current_state in self.final_states


