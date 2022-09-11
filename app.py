from flask import Flask, render_template, url_for, redirect
import git

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project_proposal", methods=["POST", "GET"])
def proposal_form():
    return render_template("proposal_handler.html", form=form)

app = Flask(__name__)
@app.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('https://github.com/GithubDev939/humans-need-code-site')
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400
