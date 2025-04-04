import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

# Something similar to a truth table is needed to determine the winner.
# Rreturns True if a wins against be, otherwise False.


def who_wins(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Here a Class to introduce the RealPlayer, it allows interaction.
# If 'quit' is typed as move, the program ends.
# This is needed to exit before the number of turn is reached.


class AllRockPlayer(Player):

    def move(self):
        return 'rock'


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

# This is a challanging one because it tries to use their.move
# before it is initialised.
# The idea is to use super __init__ to initialize it as soon
# as it is launched and it will avoid crashes.


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.their_move = random.choice(moves)


class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.last_move_index = -1

    def move(self):
        self.last_move_index = (self.last_move_index + 1) % len(moves)
        return moves[self.last_move_index]


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Inserisci la tua mossa\
                          (rock, paper, scissors o\
                          'quit' per uscire): ").strip().lower()
            if move == 'quit':
                print("Hai scelto di uscire dal gioco.")
                exit()
            if move in moves:
                return move
            print("Mossa non valida. Riprova.")


# This Class manages the game logic. Players have a
# move each turn and after each turn the score gets updated.
# A the end of the game the total score is displayed


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if who_wins(move1, move2):
            self.p1.score += 1
            print("Player 1 wins this round!")
        elif who_wins(move2, move1):
            self.p2.score += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        print(f"Score -> Player 1: {self.p1.score}, Player 2: {self.p2.score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Final Score -> Player 1: {self.p1.score},\
               Player 2: {self.p2.score}")


# Adding condition that allows to use the script directly
# or to import it without executing (or that's what I understood...)
if __name__ == '__main__':
    players = {
        '1': AllRockPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }
    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")
    while (p1 := input("Choose player 1: ")) not in players.keys():
        print("Invalid choice, please select player 1 from the list.")
    while (p2 := input("Choose player 2: ")) not in players.keys():
        print("Invalid choice, please select player 2 from the list.")

    game = Game(players[p1](), players[p2]())
    game.play_game()
