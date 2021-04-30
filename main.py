import uuid
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.session = uuid.uuid4()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_session(self):
        return self.session


@app.route("/debug")
def debug():
    c = User('Krzysztof', 'Krawczyk')
    session_hash = c.session
    return f'Your session is {session_hash}'


if __name__ == '__main__':
    app.run()
