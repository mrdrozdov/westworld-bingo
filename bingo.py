import argparse
import collections
import os
import random
import hashlib


def safe_iterator(f):
    # Guarantees last line is always empty.
    for line in f:
        yield line
    yield ''


class TemplateManager(object):
    POINTS = 5

    def __init__(self):
        self.templates = None

    def validate_template(self, template):
        pass

    def score(self, template, board):
        h, w = board.h, board.w

        def iterator():
            for i in range(h):
                for j in range(w):
                    yield i, j

        for i, j in iterator():
            idx = i * w + j
            x, y = template[i][j], board.linear_grid[idx]
            is_x = x == 'X'
            if not is_x:
                continue

            is_chosen = y in board.chosen_o or (i, j) in board.free
            if not is_chosen:
                return False

        return True

    def score_all(self, board):
        score = {}
        score['found'] = []
        score['score'] = 0
        for k, v in self.templates.items():
            if self.score(v, board):
                score['found'].append(k)
                score['score'] += self.POINTS
        return score

    def read(self, path):
        assert self.templates is None
        templates = collections.OrderedDict()

        def reader(path):
            t = None

            with open(path) as f:
                for line in safe_iterator(f):
                    line = line.strip()
                    if not line:
                        if t is not None:
                            yield t['name'], t['template']
                        t = None
                        continue
                    if t is None:
                        t = dict(name=None, template=[])
                    if t['name'] is None:
                        t['name'] = line
                    else:
                        t['template'].append(line)

        for name, template in reader(path):
            assert name not in templates, "Duplicate name {}.".format(name)
            self.validate_template(template)
            templates[name] = template

        self.templates = templates

    def print(self):
        for k, v in self.templates.items():
            print(k)
            print('\n'.join(v))
            print('')


class Board(object):
    TOKEN_FREE = 'ⓦ '
    TOKEN_CHOSEN = 'X'

    def __init__(self, global_o, player_n=None, board_n=None):
        self.h = 5
        self.w = 5
        self.player_n = player_n
        self.board_n = board_n
        self.free = [(2, 2)]
        self.o = None
        self.chosen_o = None
        self.global_o = global_o
        self.linear_grid = None

    def read(self, path):
        assert self.o is None
        o = []
        with open(path) as f:
            for line in f:
                local_o = int(line.strip())
                assert local_o < len(self.global_o)
                o.append(local_o)
        assert len(o) == self.player_n
        self.o = o

    def add(self, chosen_o):
        self.chosen_o = chosen_o

    def make_grid(self):
        assert self.linear_grid is None
        # Select player options.
        o = self.o[:]
        random.shuffle(o)
        o = o[:self.board_n]

        # Select random options.
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

    def tostring(self):
        log = ''
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
            log += row_str + '\n'

        return log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', default=149, type=int)
    parser.add_argument('--player_n', default=20, type=int, help='Number of options each player should choose.')
    parser.add_argument('--board_n', default=15, type=int, help='Number of options kept. The rest are random.')
    parser.add_argument('--players', default='./players', type=str)
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--template', default='./templates/standard.txt', type=str)
    parser.add_argument('--options', default='./options.txt', type=str, help='A file containing all options.')
    parser.add_argument('--chosen', default='./chosen/_empty.txt', type=str, help='A file containing all options that were chosen.')
    options = parser.parse_args()

    if options.test:
        options.seed = 149
        options.player_n = 20
        options.board_n = 15
        options.players = './players'
        options.template = './templates/standard.txt'
        options.chosen = './chosen/_test.txt'

    tm = TemplateManager()
    tm.read(options.template)
    # tm.print()

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

    if len(chosen_o) > 0:
        print('Found:')
        for i in chosen_o:
            print('{:>3}. {}'.format(i, global_o[i]))
        print('')

    player_info = collections.OrderedDict()
    for path in sorted(os.listdir(options.players)):
        name = os.path.basename(path).split('.')[0]
        local_seed = int(hashlib.sha1(name.encode()).hexdigest(), 16) % (10 ** 6)
        random.seed(options.seed + local_seed)
        path = os.path.join(options.players, path)
        board = Board(global_o, player_n=options.player_n, board_n=options.board_n)
        board.read(path)
        board.add(chosen_o)
        board.make_grid()
        score = tm.score_all(board)

        info = collections.OrderedDict()
        info['name'] = name
        info['seed'] = local_seed
        info['board'] = board.tostring()
        info['score'] = score
        player_info[name] = info

    for info in player_info.values():
        print('{} ({})'.format(info['name'], info['seed']))
        print(info['board'])

        if len(chosen_o) > 0:
            log = 'Score = {}'.format(info['score']['score'])
            if len(info['score']['found']) > 0:
                log += ', Found = {}'.format(info['score']['found'])
            else:
                log += ', You got lost in the maze!'
            print(log)
            print('')

    if options.test:
        assert player_info['caleb']['score']['score'] == 0
        assert player_info['charlotte']['score']['score'] == 5
        assert player_info['dolores']['score']['score'] == 10


if __name__ == '__main__':
    main()
