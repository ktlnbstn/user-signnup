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

    # if the user uses an invalid username tell them the error
    if len(new_user) < 4 or len(new_user) > 20 or ' ' in new_user:
        error = "Invalid username. Must be 4-20 characters without spaces."
        return redirect("/?error=" + error)

    # if the user typed an invalid passowrd tell them the error
    if len(pass1) < 4 or len(pass1) > 20 or ' ' in pass1:
        error2 = "Invlaid password. Must be 4-20 characters without spaces."
        return redirect("/?error=" + error2)

    # if the user typed different passowrds tell them the error
    if pass1 != pass2:
        error3 = "You typed two different passwords."
        return redirect("/?error=" + error3)

    return render_template('welcome.html', username=new_user)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
