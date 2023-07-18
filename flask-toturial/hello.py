from flask import Flask

app = Flask(__name__)


@app.route('/')
def hell():
    return "Hello Flask!"

'''Typical flask project directory

- flaskr/, a Python package containing your application code and files.
- tests/, a directory containing test modules.
- .venv/, a Python virtual environment where Flask and other dependencies are installed.
- Installation files telling Python how to install your project.
- Version control config, such as git. You should make a habit of using some type of version control for all your projects, no matter the size.
- Any other project files you might add in the future.

'''