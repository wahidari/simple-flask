from flask import Flask, render_template, request
import database

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route("/users")
def page_users():
    datatabelusers = database.getTabelUsers()
    # for i in datatabelberita:
        # print(i[1])
    # return render_template("admin.html", value=datatabelberita)
    return render_template("users.html", data=datatabelusers)

@app.route("/users/new")
def create_users():
    return render_template("create_user.html")

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)