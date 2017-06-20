from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])
def add_info():
    # look inside the request to figure out what the user typed
    new_user = request.form['username']
    pass1 = request.form['password']
    pass2 = request.form['password2']

    # if the user leaves a field empty tell them the error
    if new_user == '' or pass1 == '' or pass2 == '':
        error = "Invalid input. Please do not use a space."
        return redirect("/?error=" + error)

    # if the user uses an invalid username tell them the error
    if len(new_user) < 4 or len(new_user) > 20 or ' ' in new_user:
        error = "Invalid username. Must be between 4 and 20 characters."
        return redirect("/?error=" + error)

    # if the user typed an invalid passowrd tell them the error
    if len(pass1) < 4 or len(pass1) > 20 or ' ' in pass1:
        error = "Invlaid password. Must be between 4 and 20 characters."
        return redirect("/?error=" + error)

    # if the user typed different passowrds tell them the error
    if pass1 != pass2:
        error = "You typed two different passwords."
        return redirect("/?error=" + error)

    return render_template('welcome.html', username=new_user)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
