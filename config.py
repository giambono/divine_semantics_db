import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT_DIR, 'divine_semantics_db')

DB_FILE = os.path.join(APP_DIR, 'database', 'divine_comedy.db')
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

if __name__ == '__main__':
    print(ROOT_DIR)
    print(APP_DIR)
    print(DB_FILE)

