import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT_DIR, 'divine_semantics_db')

DB_PATH = os.path.join(APP_DIR, 'data', 'divine_comedy.db')


if __name__ == '__main__':
    print(ROOT_DIR)
    print(APP_DIR)
    print(DB_PATH)

