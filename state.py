from __future__ import annotations


class State:
    def __init__(self, state_id: str, state_map: {str, str}, accepting) -> None:
        self.state_id = state_id
        self.state_map = state_map
        self.accepting = accepting

    def getNextStateID(self, ch: str) -> State:
        """Return the ID of the state that ch transitions to.
        """
        return self.state_map[ch]

    def isAccepting(self) -> bool:
        """Return true iff this is an accepting state.
        """
        return self.accepting

    def __eq__(self, other: State):
        return self.state_id == other.state_id

    def __str__(self):
        return "ID: " + self.state_id + "\nAccepting: " + str(self.accepting)
