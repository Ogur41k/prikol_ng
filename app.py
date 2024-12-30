from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/commands.json')
def commands():
    return send_from_directory('templates', 'commands.json')


@app.route('/2000.mp3')
def send_audio():
    return send_from_directory('.', '2000.mp3')
@app.route('/1.jpg')
def send_jpg():
    return send_from_directory('.', '1.jpg')



@app.route('/submit', methods=['POST'])
def submit_answer():
    answer = request.form['answer']
    if answer == "9750":
        return redirect(url_for('victory'))
    else:
        flash('Неправильный ответ. Попробуйте снова.')
        return redirect(url_for('home'))


@app.route('/hny')
def victory():
    return render_template('hny.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
