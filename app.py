from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def load():
    return render_template('load.html')


# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/space_invaders', methods=['GET', 'POST'])
# def space_invaders():
#     return render_template('space_invaders.html')

# @app.route('/run_space_invaders', methods=['GET', 'POST'])
# def run_space_invaders():
#     subprocess.Popen(['python', 'games/Space Invaders/main.py'])
#     return ''

# @app.route('/pac_man', methods=['GET', 'POST'])
# def pac_man():
#     return render_template('pac_man.html')

@app.route('/snake', methods=['GET', 'POST'])
def snake():
    return render_template('snake.html')

if __name__ == '__main__':
    app.run()