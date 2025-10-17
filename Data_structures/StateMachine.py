

class StateMachine:
    def __init__(self, transitions: dict, output_map: dict, init_state, final_states):
        self.transitions = transitions
        self.output_map = output_map
        self.init_state = init_state
        self.final_states = final_states
        self.current_state = self.init_state

    def next_state(self, transition_input):
        next_possible_states = self.transitions[self.current_state]
        if transition_input is None: # Moore machine => only one next possible state
            self.current_state = next_possible_states
        else: # Mealy machine => many possible states, decided from input
            self.current_state = next_possible_states[transition_input]

    def reset(self):
        self.current_state = self.init_state

    def get_output(self):
        return self.output_map[self.current_state]

    def can_exit(self):
        return self.current_state in self.final_states


