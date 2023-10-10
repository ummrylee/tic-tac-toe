
from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name 
            self.sign = sign  
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                  if cell in valid_choices and board.isempty(cell):
                        board.set(cell, self.sign)
                        return
                  else:
                        print("You did not choose correctly.")
class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
            self.board = board
            
      def choose(self, board):
            print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end="")
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            possible_moves = [valid_choices[i] for i in range(9) if board.board[i] == ' ']
            move = choice(possible_moves)
            print(move)
            board.set(move, self.sign)
            return move

class miniMax(AI):
      
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = miniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)
      
      def minimax(self, board, player, start):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            available_moves = [valid_choices[i] for i in range(9) if board.board[i] == ' ']
            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1
                  elif board.get_winner() == "":
                        return 0
                  else:
                        return -1
                  
            max_score = -9999999999
            min_score = 9999999999
            best_cell = None
            for cell in available_moves:
                  if player:
                        board.set(cell, self.sign)
                  else:
                        board.set(cell, ("O" if self.sign == "X" else "X"))
                  score = self.minimax(board, not player, False)
                  if score > max_score:
                        max_score = score
                        best_cell = cell
                  if score < min_score:
                        min_score = score
                  board.set(cell, " ")
                  board.winner = ""
            if start:
                  return best_cell
            elif player:
                  return max_score
            else:
                  return min_score