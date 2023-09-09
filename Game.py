import os
from random import randint

class Player:
    def __init__(self, name: str, board: list, tiles: list):
        self.name = name
        self.board = board
        self.tiles = tiles

    def addrandomtiles(self, bag: list, num: int):
        for i in range(num):
            if bag:
                random_tile_index = randint(0, len(bag) - 1)
                self.tiles.append(bag.pop(random_tile_index))

    def playtile(self, tile, row, col):
        if tile in self.tiles and self.board[col][row] == " ":
            self.board[col][row] = tile
            self.tiles.remove(tile)
            return True
        return False

    def getname(self):
        return self.name

    def getboard(self):
        return self.board

    def gettiles(self):
        return self.tiles

    def gettile(self, index):
        if 0 <= index < len(self.tiles):
            return self.tiles[index]
        return None

    def getnumtiles(self):
        return len(self.tiles)

class Bag:
    def __init__(self, name, tiles: list):
        self.tiles = tiles
        self.name = name

    def mixtiles(self):
        for i in range(len(self.tiles)):
            random_tile_index = randint(0, len(self.tiles) - 1)
            self.tiles[i], self.tiles[random_tile_index] = self.tiles[random_tile_index], self.tiles[i]

    def gettiles(self):
        return self.tiles

    def getnumtiles(self):
        return len(self.tiles)

class Main:
    @staticmethod
    def startgame():
        while True:
            try:
                num_players = int(input("How many players? "))
                if num_players > 0:
                    break
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Please enter a number.")

        players = []

        for i in range(num_players):
            name = input(f"What is player {i+1}'s name? ")
            board = [[" " for i in range(15)] for i in range(15)]
            tiles = []
            
            # Create a Player object and append it to the 'players' list
            player = Player(name, board, tiles)
            players.append(player)

        amtofeachtile = [(("j", "k", "q", "x", "z"), 2), (("b", "c", "f", "h", "m", "p", "v", "w", "y"), 3), (("g",), 4), (("l", "s", "u", "d"), 5), (("n", "r", "t"), 6), (("o",), 11), (("a", "i"), 13), (("e",), 18)]
        bag = []

        for group, count in amtofeachtile:
            for letter in group:
                bag.extend([letter] * count)

        random_bag = Bag("Bag", bag)
        random_bag.mixtiles()
        
        print("Tiles in bag:", random_bag.gettiles())
        print("Number of tiles in bag:", random_bag.getnumtiles())
        print("Game Setup Complete!")

        for player in players:
            player.addrandomtiles(random_bag.gettiles(), 7)

        # Game Loop

        while True:
            for player in players:
                
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")

                print(f"{player.getname()}'s turn!")
                print("Tiles:", player.gettiles())
                print("Board:")
                for row in player.getboard():
                    print(row)

                while True:
                    try:

                        print("Enter a tile to play ((tile),(row),(col)), 'pass' to pass, or swap to swap 1 tile for 3 new tiles tiles.")
                        user_command = input("Command: ")

                        if user_command == "pass":
                            break
                        elif user_command == "swap":
                            if player.getnumtiles() > 0:

                                print("Enter the tile you want to swap.")
                                tile = input("Tile: ")
                                if tile in player.gettiles():

                                    player.gettiles().remove(tile)
                                    random_bag.gettiles().append(tile)
                                    player.addrandomtiles(random_bag.gettiles(), 3)
                                    print("Tiles:", player.gettiles())
                                    break
                                else:
                                    print("You don't have that tile.")
                            else:
                                print("You don't have any tiles to swap.")
                        elif user_command == "quit":
                            return
                        else:
                            tile, row, col = user_command.split(",")
                            if player.playtile(tile, int(row), int(col)):
                                break
                            else:
                                print("Invalid move.")
                    except ValueError:
                        print("Invalid move. get good")

Main.startgame()