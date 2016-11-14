from flask import Flask, request, render_template, url_for, redirect, abort, session, escape

app = Flask(__name__)

message = 'hello world'

@app.route('/')
def index():
    if 'username' in session:
        return 'Loggd in as {}'.format(escape(session['username']))
    return 'You are not loggd in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=login>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/error')
def err():
    abort(401)
    return 'error'

@app.errorhandler(404)
def page_not_found(error):
    return 'page not found'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User {}'.format(username)

@app.route('/message')
def messaging():
    message = 'text'
    return message

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
