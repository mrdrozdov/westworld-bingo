import argparse
import os
import random
import hashlib

from valid_templates import TEMPLATES

def temp2list(template):
    return [1 if letter == "X" else 0 for row in template for letter in row]

def check(marked, template):
    template_marked = [x - y for x, y in zip(marked, template)]
    return min(template_marked) == 0

class Board(object):
    TOKEN_FREE = 'ⓦ '
    TOKEN_CHOSEN = 'X'

    def __init__(self, global_o, limit=10):
        self.h = 5
        self.w = 5
        self.limit = limit
        self.free = [(2, 2)]
        self.permutation = None
        self.o = None
        self.chosen_o = None
        self.global_o = global_o

    def read(self, path):
        assert self.o is None
        o = []
        with open(path) as f:
            for line in f:
                local_o = int(line.strip())
                assert local_o < len(self.global_o)
                o.append(local_o)
        assert len(o) == self.limit
        self.o = o

    def add(self, chosen_o):
        self.chosen_o = chosen_o

    def make_grid(self):
        o = self.o[:]
        if self.permutation is not None:
            # TODO: Change order.
            pass

        n = self.h * self.w
        missing = n - len(o)
        new_o = random.sample(range(len(self.global_o)), missing + len(o))
        for i in new_o:
            if len(o) == n:
                break
            if i not in o:
                o.append(i)

        assert len(o) == n

        random.shuffle(o)
        self.linear_grid = o

    def print(self):
        o = self.linear_grid
        for i in range(self.h):
            found = []
            row = []
            for j in range(self.w):
                idx = i * self.w + j
                this_o = o[idx]
                if (i, j) in self.free:
                    this_o = self.TOKEN_FREE
                elif self.chosen_o is not None and this_o in self.chosen_o:
                    found.append(this_o)
                    this_o = self.TOKEN_CHOSEN
                row.append(' {:>3} '.format(this_o))
            row_str = '|' + '|'.join(row) + '|'
            if len(found) > 0:
                row_str = row_str + ' Found: {}'.format(' '.join([str(s) for s in found]))
            print(row_str)

        print('')

    def score(self):
        free_ids = [x[0] * self.w + x[1] for x in self.free]
        checked_str = [
            1 if self.linear_grid[i] in self.chosen_o or i in free_ids else 0
            for i in range(self.h * self.w)
        ]
        found = []
        for temp_name, template in TEMPLATES.items():
            temp_list = temp2list(template)
            if check(checked_str, temp_list):
                found.append(temp_name)
        found.sort()
        return found

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', default=149, type=int)
    parser.add_argument('--limit', default=10, type=int, help='Number of options each player should choose.')
    parser.add_argument('--players', default='./players', type=str)
    parser.add_argument('--options', default='./options.txt', type=str, help='A file containing all options.')
    parser.add_argument('--chosen', default='./empty.txt', type=str, help='A file containing all options that were chosen.')
    options = parser.parse_args()

    global_o = []
    with open(options.options) as f:
        for line in f:
            global_o.append(line.strip())

    chosen_o = []
    with open(options.chosen) as f:
        for line in f:
            chosen_o.append(int(line.split()[0]))

    print('seed: {}'.format(options.seed))
    print('')

    for path in os.listdir(options.players):
        local_seed = int(hashlib.sha1(path.encode()).hexdigest(), 16) % (10 ** 6)
        random.seed(options.seed + local_seed)
        path = os.path.join(options.players, path)
        print('{} ({})'.format(path, local_seed))
        board = Board(global_o)
        board.read(path)
        board.add(chosen_o)
        board.make_grid()
        board.print()
        found = board.score()
        if len(found) > 0:
            print("Score = {:d} (You found {})\n".format(len(found), ", ".join(found)))
        else:
            print("Score = 0 (You got lost in the maze!)\n")


if __name__ == '__main__':
    main()
