import argparse
import collections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='./chosen/ep1-outline.txt', type=str)
    parser.add_argument('--verbose', action='store_true')
    options = parser.parse_args()

    gauge = collections.Counter()
    with open(options.path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            found, desc = line.split(' ', 1)
            is_found = found == 'YES'
            gauge[found] += 1
            if options.verbose:
                print(i, is_found, found, desc)
            else:
                if is_found:
                    print(i)
    if options.verbose:
        print(gauge)


if __name__ == '__main__':
    main()
