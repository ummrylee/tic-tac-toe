class Board:
      def __init__(self):
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            self.winner = ""
      def get_size(self): 
            return self.size
      def get_winner(self):
            return self.winner
      def set(self, cell, sign):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            if self.board[valid_choices.index(cell)] == " ":
                  return True
            return False
            
      def isdone(self):
            done = False
            for i in range(0,7,3):
                  if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                        done = True
                        self.winner = self.board[i]
            for i in range(0,3):
                  if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                        done = True
                        self.winner = self.board[i]
            if (self.board[0] == self.board[4] == self.board[8] != " ") or (self.board[2] == self.board[4] == self.board[6] != " "):
                  done = True
                  self.winner = self.board[4]
            if " " not in self.board:
                  done = True
                  return True
            if done:
                  return True
            return False
      
      def show(self):
            print('   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')

               
