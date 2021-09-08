# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

max_depth = 4;
class Move:
    x: float

class State:
    def next_state(self, move):
        pass


# struct Move {
#
# };
# struct State {
#     State next_state(Move move);
#     long double winning_probability();
#     vector<Move>possible_moves;
# };
def min_max( state, depth):
    if depth == max_depth:
        return state.winning_probability()
    result = 0
    for(move: state.possible_moves):
            result = max(result, 1 - min_max(state.next_state(move), depth + 1))
    return  result
