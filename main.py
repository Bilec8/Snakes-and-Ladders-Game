import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps):
        """Move the player by the number of steps."""
        self.position += steps

    def has_won(self):
        """Check if the player has won."""
        return self.position == 100
    
    def throw_dice(self):
        """Simulate throwing a dice."""
        total = 0

        while True:
            steps = random.randint(1, 6)
            total += steps
            if steps != 6:
                print(f"{self.name} rolled a {steps}.")
                break
            print(f"{self.name} rolled a {steps}!. Rolling again...")

        return total
    
    def print_moves(self, steps):
        """Print the number of steps taken."""
        print(f"{self.name} moved from {self.position} to {self.position + steps}.")

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = players

    def resolve_collisions(self, player):
        """Check if any other player is on the same position."""
        if player.position == 1:
            return

        for p in self.players:
            if p != player and p.position == player.position:
                print(f"{player.name} has landed on the same position as {p.name}.")
                p.position -= 1
                print(f"{p.name} moved back from {p.position + 1} to {p.position}.")
                self.resolve_collisions(p)

    def check_snake_ladder(self, player):
        """Check if the player has landed on a snake or ladder."""
        if player.position in self.board.snakes:
            print(f"Oh no! {player.name} landed on a snake!  From {player.position} to {self.board.snakes[player.position]} :(")
            player.position = self.board.snakes[player.position]
            self.resolve_collisions(player)
        
        elif player.position in self.board.ladders:
            print(f"Yay! {player.name} climbed a ladder! From {player.position} to {self.board.ladders[player.position]} :)")
            player.position = self.board.ladders[player.position]
            self.resolve_collisions(player)

    def print_all_positions(self):
        """Print all players' positions."""
        print("Current positions:")
        for player in self.players:
            print(f"{player.name}: {player.position}")

        print("\n " + "-" * 50 + "\n")


    def play(self):
        """Start the game."""
        while True:
            for player in self.players:
                input(f"{player.name}'s turn. Press Enter to roll the dice.")
                
                steps = player.throw_dice()

                if player.position + steps > self.board.board_size:
                    print(f"{player.name} rolled too high! You need {game.board.board_size - player.position}.")
                else:
                    player.print_moves(steps)
                    player.move(steps)

                if player.has_won():
                    print(f"Congratulations {player.name}, you have won the game!")
                    return
                
                while player.position in self.board.snakes or player.position in self.board.ladders:
                    self.check_snake_ladder(player)

                self.print_all_positions()
                
class Board:
    def __init__(self):
        self.board_size = 100
        self.snakes =  {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

if __name__ == "__main__":
    print("Welcome to Snakes and Ladders!")
    print("How many players are there?")
    num_players = int(input("Enter number of players: "))

    players = []
    name = None

    for i in range(num_players):
        while name is None or name in [pl.name for pl in players]:
            name = input(f"Enter name for player {i + 1}: ")

            if name in [pl.name for pl in players]:
                print("Player name already exists. Please enter a different name.")
                name = None
        
        players.append(Player(name))

    game = Game(players)
    game.play()