from flask import Flask, render_template, request
import database

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route("/admin")
def page_data():
    datatabelberita = database.getTabelBerita()
    # for i in datatabelberita:
        # print(i[1])
    # return render_template("admin.html", value=datatabelberita)
    return render_template("data.html", data=datatabelberita)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)