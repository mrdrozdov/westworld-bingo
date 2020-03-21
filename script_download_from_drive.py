# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# Don't forget to add service account email as collaborator explicitly in the doc.
import io
import pickle
import os.path
import sys

from oauth2client.service_account import ServiceAccountCredentials
import gspread



def main():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.readonly',
        ]

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    if os.path.exists('form.txt'):
        with open('form.txt') as f:
            form_id = f.read().strip()
        print('Found form id: {}'.format(form_id))
    else:
        print('No form id found.')
        sys.exit()

    item = client.open_by_key(form_id)
    sheet = item.sheet1

    names = sheet.col_values(2)[1:]
    usernames = sheet.col_values(3)[1:]
    choices = sheet.col_values(4)[1:]

    line2idx = {}
    with open('options.txt') as f:
        for i, line in enumerate(f):
            line = line.strip()
            line2idx[line] = i

    for n, u, lst in zip(names, usernames, choices):
        u = u.lower()
        print(n, u)
        path = './watchparty/{}.txt'.format(u)
        f = open(path, 'w')
        for line in lst.split('.,'):
            line = line.strip()
            if not line.endswith('.'):
                line = line + '.'
            idx = line2idx[line]
            print(idx, line)
            f.write('{}\n'.format(idx))


if __name__ == '__main__':
    main()
