from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class Invoker:

    def executeCommand(self, command: Command):
        return command.execute()


class HistoryCommands:

    def __init__(self):
        self.commands = []

    def set_command(self, player, x, y):
        self.commands.append(dict(player=player, x=x, y=y))

    def undo_command(self):
        self.commands.pop()

    def get_last_command(self):
        if len(self.commands) > 0:
            return self.commands[len(self.commands)-1]
        else:
            return False

class Receiver:

    def __init__(self):
        self.history_commands = HistoryCommands()

        self.possible_players = ["X", "Y"]
        # it needs be changed
        self.current_player = "X"
        self.field = [[None, None, None], [None, None, None], [None, None, None]]

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "Y"
        else:
            self.current_player = "X"

    def print_field(self):
        for i in self.field:
            print(i)

    def do_step(self, x, y):
        try:
            if self.field[x][y] is None:
                self.history_commands.set_command(self.current_player, x, y)
                print("It's", self.current_player, "move")
                self.field[x][y] = self.current_player
                self.change_player()
                self.print_field()
                return True
            else:
                print("Current cell is not available to step\n")
                return False
        except:
            print("not correct step\n")
            return False

    def undo_step(self):
        if self.history_commands.get_last_command():
            last_command = self.history_commands.get_last_command()
            self.field[last_command['x']][last_command['y']] = None

            self.history_commands.undo_command()
            self.current_player = last_command['player']
            self.print_field()
            return True
        else:
            print("impossible undo steps")
            return False

    def check_empty_cells(self):
        for i in self.field:
            if None in i:
                return True

        return False

    def check_winner(self):
        for i in range(len(self.field)):
            if self.field[0][i] is not None:
                if self.field[0][i] == self.field[1][i] and self.field[1][i] == self.field[2][i]:
                    winner = self.field[0][i]
                    return winner

        for i in range(len(self.field)):
            if self.field[i][0] is not None:
                if self.field[i][0] == self.field[i][1] and self.field[i][1] == self.field[i][2]:
                    winner = self.field[i][0]
                    return winner

        if self.field[1][1] is not None:
            if self.field[0][0] == self.field[1][1] and self.field[1][1] == self.field[2][2]:
                winner = self.field[0][0]
                return winner

            if self.field[0][2] == self.field[1][1] and self.field[1][1] == self.field[2][0]:
                winner = self.field[0][2]
                return winner

        return False


class MakeStepCommand(Command):

    def __init__(self, receiver: Receiver, x, y):
        self.receiver = receiver
        self.x = int(x)
        self.y = int(y)

    def execute(self):
        status = self.receiver.do_step(self.x, self.y)
        print("Make Step Status", status, '\n')

class UndoStepCommand(Command):

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        status = self.receiver.undo_step()
        print("Undo Step Status", status, '\n')

class CheckEmptyFieldCellCommand(Command):

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        status = self.receiver.check_empty_cells()
        return status

class CheckWinnerCommand(Command):

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        status = self.receiver.check_winner()
        return status

if __name__ == '__main__':
    invoker = Invoker()
    receiver = Receiver()

    print("Enter one of this commands")
    print("print 'step x y' or 'undo'\n")

    while True:
        user_input = input()
        if user_input == "undo":
            invoker.executeCommand(UndoStepCommand(receiver))
        else:
            x, y = user_input.split(' ')[1:]
            invoker.executeCommand(MakeStepCommand(receiver, x, y))

        if invoker.executeCommand(CheckWinnerCommand(receiver)):
            break
        if not invoker.executeCommand(CheckEmptyFieldCellCommand(receiver)):
            break

    result_winner = invoker.executeCommand(CheckWinnerCommand(receiver))
    result_draw = invoker.executeCommand(CheckEmptyFieldCellCommand(receiver))

    if result_winner:
        print(result_winner, "wins")
    else:
        print("Draw")
