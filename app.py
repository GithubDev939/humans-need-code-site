from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTB3rYQg8EcMrdTimkZfAb'

class ProposalForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()], description="Enter Name")
    email = EmailField("What is your email?", validators=[DataRequired(), Email()], description= "Enter Email")
    nonprofit = StringField("What is the name of your nonprofit?", validators=[DataRequired()], description = "Enter Nonprofit Name")
    nonprofit_position = StringField("What position do you hold in your nonprofit?", validators=[DataRequired()], description="Enter Nonprofit Position")
    location = StringField("Where is your nonprofit located?", validators=[DataRequired()], description="Enter Nonprofit Location")
    org_email = EmailField("What is your nonprofit's email?", validators=[DataRequired(), Email()], description = "Enter Nonprofit Email")
    links = StringField("Any links or resources to learn more about your nonprofit's mission?", description = "Enter Related Links")
    project_proposal = StringField("What software would you like to propose we create?", validators=[DataRequired()], description = "Enter Software Proposal", widget=TextArea(), render_kw={"rows": 7})
    ideas_elaboration = StringField("Any elaboration?", description="Enter Elaboration", widget=TextArea(), render_kw={"rows": 7})
    other = StringField("Other notes (e.g. timeline, team, etc.)", description = "Enter Other Notes", widget=TextArea(), render_kw={"rows": 7})
    submit = SubmitField("Submit", description="")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project_proposal", methods=["POST", "GET"])
def proposal_form():
    form = ProposalForm()
    if form.validate_on_submit():
        print(form.data)
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template("proposal_handler.html", form=form)