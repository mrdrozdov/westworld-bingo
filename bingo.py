import argparse
import os
import random
import hashlib


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

    def print(self):
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
        board.print()


if __name__ == '__main__':
    main()
