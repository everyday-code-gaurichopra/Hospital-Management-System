from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.fields import DateTimeField
from package.doctor import Doctors, Doctor
from package.patient import Patients, Patient
from package.physiopatient import PhysioPatients, PhysioPatient
from package.exportpatient import ExportPatients, ExportPatient
from package.other import Others, Other
from package.medicine import Medicines, Medicine
from package.common import Common
import json
import os


with open('config.json') as data_file:
    config = json.load(data_file)
    
file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)

api = Api(app)

api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(PhysioPatients, '/physiopatient')
api.add_resource(PhysioPatient, '/physiopatient/<int:id>')
api.add_resource(ExportPatients, '/exportpatient')
api.add_resource(ExportPatient, '/exportpatient/<int:id>')
api.add_resource(Others, '/other')
api.add_resource(Other, '/other/<int:id>')
api.add_resource(Medicines, '/medicine')
api.add_resource(Medicine, '/medicine/<int:id>')
api.add_resource(Common, '/common')


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ =="__main__":
    app.run(debug=True,port=5000)