import sys
import heapq

"""
Advent of Code Day 7 Solution
"""

__author__ = "James Plante (jwplante)"
__license__ = "MIT"


class Directory:
    def __init__(self, parent, name):
        self.dotdot = parent
        self.name = name
        self.children = {}
    
    def is_dir(self):
        return True

    def du(self):
        size = sum([child.du() for child in self.children.values()])
        return size

    def mkdir(self, name):
        if name not in self.children:
            print(f"Creating directory {name}")
            self.children[name] = Directory(self, name)
        else:
            raise Exception("File/Directory already exists!")
    
    def new_file(self, name, size):
        if name not in self.children:
            self.children[name] = File(self, name, size)
        else:
            raise Exception("File/Directory already exists!")
    
    def get_path(self):
        if self is self.dotdot:
            return '/'
        else:
            return self.dotdot.get_path() + f"{self.name}/"


class File:
    def __init__(self, parent, name, size):
        self.parent_dir = parent
        self.name = name
        self.size = size
    
    def is_dir(self):
        return False

    def du(self):
        return self.size

    def mkdir(self, name):
        raise Exception("You cannot create a directory in a file!")
    
    def get_path(self):
        return self.dotdot.get_path() + self.name


class CommandLine:
    def __init__(self):
        # Create the rootdir
        self.root = Directory('root', None)
        self.root.dotdot = self.root
        self.cwd = self.root
    
    def ls(self, output):
        for line in output:
            tok1, tok2 = line
            if tok1 == 'dir':
                self.cwd.mkdir(tok2)
            else:
                self.cwd.new_file(tok2, int(tok1))
    
    def cd(self, new_dir):
        # Special case for rootdir
        if new_dir == '/':
            self.cwd = self.root
        elif new_dir == '..':
            print(f"Change directory: {self.cwd.dotdot.get_path()}")
            self.cwd = self.cwd.dotdot
        else:
            move_to = self.cwd.children[new_dir]
            print(f"Change directory: {move_to.get_path()}")
            self.cwd = move_to
    
    def parse_command(self, command_text):
        all_lines = command_text.split('\n')
        command = all_lines[0].strip()
        output = [line.strip() for line in all_lines[1:]]

        print(f"Execute command: '{command}'")
        tokenized_command = command.split(' ')
        if tokenized_command[0] == 'cd':
            newdir = tokenized_command[1]
            self.cd(newdir)
        elif tokenized_command[0] == 'ls':
            output_tokens = [line.split() for line in output if line != '']
            self.ls(output_tokens)
        else:
            raise Exception(f"{command[0]}: Command not found!")



def part_one(input_str: str):

    def sum_small_folders(file):
        size = file.du()
        if not file.is_dir():
            return 0
        else:
            to_add = size if size < 100000 else 0
            return to_add + sum([sum_small_folders(f) for f in file.children.values()])
        
    commands = input_str.strip().split("$")[1:]
    # First just run all the commands
    cli = CommandLine()
    for command in commands:
        cli.parse_command(command)
    
    filesystem = cli.root
    print(f"Solution for Part 1: {sum_small_folders(filesystem)}")


def part_two(input_str: str):

    def size_of_smallest_file_to_delete(file, space_to_free):
        def traverse(current_file):
            size = current_file.du()
            if not current_file.is_dir():
                pass
            elif size >= space_to_free:
                heapq.heappush(heap, (size, current_file))
                for child in current_file.children.values():
                    traverse(child)
        
        heap = []
        traverse(file)
        minimum = heapq.heappop(heap)
        return minimum[0]
    
    commands = input_str.strip().split("$")[1:]
    # First just run all the commands
    cli = CommandLine()
    for command in commands:
        cli.parse_command(command)
    
    DISK_SIZE = 70000000
    NEEDED_SPACE = 30000000
    filesystem = cli.root
    current_disk_usage = filesystem.du()

    space_to_free = abs(NEEDED_SPACE - (DISK_SIZE - current_disk_usage))

    print(f"Solution for Part 2: {size_of_smallest_file_to_delete(filesystem, space_to_free)}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        with open(filename) as f:
            contents = f.read()

        part_one(contents) 
        part_two(contents)