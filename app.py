from flask import Flask

app = Flask(__name__)

users = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "doej@abc.com"
    },
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "doej1@abc.com"
    }
]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users")
def get_users() -> list:
    return users


@app.route('/user/<first_name>')
def get_user(first_name: str) -> dict:
    for item in users:
        if item.get("first_name") == first_name:
            return item

    return {}


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
