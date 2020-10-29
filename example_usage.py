from dfa import DFA

filepath = input("Enter path to DFA JSON file: ")
dfa = DFA(filepath)
running = True
while (running):
    user_input = input("Enter input string (or \exit): ")
    if (user_input == "\exit"):
        running = False
        break
    if dfa.testInput(user_input):
        print("Input PASSED")
    else:
        print("Input FAILED")
