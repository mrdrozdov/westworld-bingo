# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# Don't forget to add service account email as collaborator explicitly in the doc.
import argparse
import collections
import io
import pickle
import os.path
import sys

import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import gspread


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--group', default='watchparty', type=str)
    options = parser.parse_args()

    form_path = './form-{}.txt'.format(options.group)
    group_path = './{}'.format(options.group)

    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.readonly',
        ]

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    if os.path.exists(form_path):
        with open(form_path) as f:
            form_id = f.read().strip()
        print('Found form id: {}'.format(form_id))
    else:
        print('No form id found.')
        sys.exit()

    item = client.open_by_key(form_id)
    sheet = item.sheet1


    col_name = None
    col_username = None
    col_choices = None
    for i in range(10):
        try:
            header = sheet.col_values(i)[0]
            if header == "What's your name?":
                col_name = i
            if header == "What username would you like?":
                col_username = i
            if header == "Choose 20 of the following options.":
                col_choices = i
        except:
            print('skip', i)

    names = sheet.col_values(col_name)[1:]
    usernames = sheet.col_values(col_username)[1:]
    choices = sheet.col_values(col_choices)[1:]

    line2idx = collections.OrderedDict()
    with open('options.txt') as f:
        for i, line in enumerate(f):
            line = line.strip()
            line2idx[line] = i

    grid = np.zeros((len(line2idx), len(usernames)), dtype=np.int32)

    for j, (n, u, lst) in enumerate(zip(names, usernames, choices)):
        u = u.lower()
        print(n, u)
        path = os.path.join(group_path, '{}.txt'.format(u))
        f = open(path, 'w')
        for line in lst.split('.,'):
            line = line.strip()
            if not line.endswith('.'):
                line = line + '.'
            idx = line2idx[line]
            print(idx, line)
            f.write('{}\n'.format(idx))

            grid[idx, j] += 1
    print('')

    for j, u in enumerate(usernames):
        print(j, u)
    print('')

    dist = collections.Counter()
    for i, desc in enumerate(line2idx.keys()):
        individual = ' '.join(['{}'.format(grid[i, j]) for j in range(len(usernames))])
        total = grid[i].sum()
        print('{:>3}. {:<40} : {} : {}'.format(i, desc[:40], individual, total))
        dist[total] += 1

    print(sorted(dist.items(), key=lambda x: x[0]))


if __name__ == '__main__':
    main()
