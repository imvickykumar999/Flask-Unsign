
from flask import (
    Flask, 
    session, 
    render_template
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
users = ["blue", "yellow"]

@app.route('/')
def index():
    # You are logged in as yellow!
    session = {'username': users[1]}

    if "username" in session and session["username"] in users:
        return render_template('index.html', session=session)
    else:
        return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

r'''
>>> flask-unsign --sign --cookie "{'logged_in': True}" --secret 'CHANGEME'
eyJsb2dnZWRfaW4iOnRydWV9.ZS6bkA.kcqX2EloNzojpudt8OVjYi0NGi8

>>> flask-unsign --decode --cookie 'eyJsb2dnZWRfaW4iOnRydWV9.ZS6bkA.kcqX2EloNzojpudt8OVjYi0NGi8'
{'logged_in': True}
'''
