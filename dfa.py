from state import State
import json


class DFA:
    def __init__(self, filename: str) -> None:
        """
        Create a DFA.

        Keyword arguments:
        filename -- the file path to the machine's JSON file
        """
        file = open(filename, "r")
        states_dictionary = json.loads(file.read())
        file.close()
        states = {}
        for element in states_dictionary["states"]:
            state = State(
                element['id'], element['transition_functions'], element['accepting'])
            states[element["id"]] = state)

        self.states=states
        self.initial_state=self.states[states_dictionary["initial_state"]]

    def getFinalState(self, input: str) -> State:
        """Return the final state of the DFA after reading through the input.

        Keyword arguments:
        input -- the string input to run through
        """
        current_state=self.initial_state
        for ch in input:
            current_state=self.states[current_state.getNextStateID(
                ch)]
        return current_state

    def testInput(self, input: str) -> bool:
        """Return true iff the input causes the DFA to finish in
        an accepting state.

        Keyword arguments:
        input -- the string input to run through
        """
        return self.getFinalState(input).isAccepting()
