#!./venv/bin/python

class Assembly:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.index = 0

    # obx
    def write_box(self, box):
        print(box, end = '')

    # ostr
    def write_string(self, string):
        print(string, end = '')

    # nl
    def new_line(self):
        print('\n')

    # lbx
    def load_box(self, box):
        if box == 'A':
            self.A = int(input())

        if box == 'B':
            self.B = int(input())

        if box == 'C':
            self.C = int(input())

        if box == 'D':
            self.D = int(input())

    # sbx
    def set_box(self, box, value):
        if box == 'A':
            self.A = value

        if box == 'B':
            self.B = value

        if box == 'C':
            self.C = value

        if box == 'D':
            self.D = value

    # ibx
    def increase_box(self, box, value):
        if box == 'A':
            self.A += value

        if box == 'B':
            self.B += value

        if box == 'C':
            self.C += value

        if box == 'D':
            self.D += value

    # dbx
    def decrease_box(self, box, value):
        if box == 'A':
            self.A -= value

        if box == 'B':
            self.B -= value

        if box == 'C':
            self.C -= value

        if box == 'D':
            self.D -= value

    # if
    def condition(self, condition, jump_a, jump_b):
        if condition:
            self.jump(jump_a)

        else:
            self.jump(jump_b)

    # jmp
    def jump(self, line):
        self.index = line - 1

    # when something goes wrong
    def error(self):
        print("Error occurred! Check that all commands are spelled correctly.")

    # run the program
    def run(self, filepath):
        with open(filepath, 'r') as f:
            file = f.read()

        code = file.split(';')

        for self.index in code:
            self.run_command(code[self.index])

    # execute the command
    def run_command(self, command):
        command = command.replace(' ', '')

        if command[0:4] == 'obx:':
            if command[4:5] == 'A':
                self.write_box(self.A)

            elif command[4:5] == 'B':
                self.write_box(self.B)

            elif command[4:5] == 'C':
                self.write_box(self.C)

            elif command[4:5] == 'D':
                self.write_box(self.D)

            else:
                self.error()

        elif command[0:5] == 'ostr:':
            if (command[5:6] == '"' and command[-1:] == '"') or (command[5:6] == '\'' and command[-1:] == '\''):
                self.write_string(command[6:-1])

            else:
                self.error()

        elif command == 'nl':
            self.new_line()

        elif command[0:4] == 'lbx:':
            if command[4:5] == 'A':
                self.load_box('A')

            elif command[4:5] == 'B':
                self.load_box('B')

            elif command[4:5] == 'C':
                self.load_box('C')

            elif command[4:5] == 'D':
                self.load_box('D')

            else:
                self.error()

        elif command[0:4] == 'sbx:':
            if command[4:5] == 'A' and command[5:6] == ',':
                value = command[6:]
                self.set_box('A', int(value))

            elif command[4:5] == 'B' and command[5:6] == ',':
                value = command[6:]
                self.set_box('B', int(value))

            elif command[4:5] == 'C' and command[5:6] == ',':
                value = command[6:]
                self.set_box('C', int(value))

            elif command[4:5] == 'D' and command[5:6] == ',':
                value = command[6:]
                self.set_box('D', int(value))

            else:
                self.error()

        elif command[0:4] == 'ibx:':
            if command[4:5] == 'A' and command[5:6] == ',':
                value = command[6:]
                self.increase_box('A', int(value))

            elif command[4:5] == 'B' and command[5:6] == ',':
                value = command[6:]
                self.increase_box('B', int(value))

            elif command[4:5] == 'C' and command[5:6] == ',':
                value = command[6:]
                self.increase_box('C', int(value))

            elif command[4:5] == 'D' and command[5:6] == ',':
                value = command[6:]
                self.increase_box('D', int(value))

            else:
                self.error()

        elif command[0:4] == 'dbx:':
            if command[4:5] == 'A' and command[5:6] == ',':
                value = command[6:]
                self.decrease_box('A', int(value))

            elif command[4:5] == 'B' and command[5:6] == ',':
                value = command[6:]
                self.decrease_box('B', int(value))

            elif command[4:5] == 'C' and command[5:6] == ',':
                value = command[6:]
                self.decrease_box('C', int(value))

            elif command[4:5] == 'D' and command[5:6] == ',':
                value = command[6:]
                self.decrease_box('D', int(value))

            else:
                self.error()

        elif command[0:3] == 'if:':
            pass

        elif command[0:4] == 'jmp:':
            self.jump(int(command[4:]))

        else:
            self.error()

asm = Assembly()

if __name__ == '__main__':
    command = ''

    while command.lower() != 'quit':
        command = input('>>> ')

        if command.lower() != 'quit':
            asm.run_command(command)
