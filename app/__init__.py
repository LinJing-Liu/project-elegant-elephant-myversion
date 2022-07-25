import os
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import *
from pymysql import *
import re

from .static.content.index_content import *
from .static.content.prof_content import *
from .static.content.hobby_content import *
from .static.content.about_content import *
from .static.content.base_content import *

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
	print("Running in test mode")
	mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    print("Running in standard mode")
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    		user=os.getenv("MYSQL_USER"),
    		password=os.getenv("MYSQL_PASSWORD"),
    		host=os.getenv("MYSQL_HOST"),
    		port=3306
	)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)

@app.route('/')
def index():
    return render_template('index.html', title="Home", url=os.getenv("URL"), base=base_info, content=info, header=header, identity=identity_info, connect=connect_info)

@app.route('/professionalinfo')
def professionalInfo():
    return render_template('prof.html', title="Education/Experience", url=os.getenv("URL"), base=base_info, education=education_info, skills=skills_info, experience=experience_info, links=links_info)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), base=base_info, hobby=hobby_info)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), base=base_info, )

@app.route('/about')
def about():
    return render_template('about.html', title="About This Site", url=os.getenv("URL"), base=base_info, state_links=statement_links, resource_links=resource_links)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        invalidName = Response("Invalid name")
        invalidName.status_code = 400
        name = request.form['name']
        if name == "":
            return invalidName
    except KeyError:
        return invalidName

    try:
        invalidContent = Response("Invalid content")
        invalidContent.status_code = 400
        content = request.form['content']
        if content == "":
            return invalidContent
    except KeyError:
        return invalidContent

    try:
        invalidEmail = Response("Invalid email")
        invalidEmail.status_code = 400
        email = request.form['email']
        if email == "" or (not checkEmail(email)):
            return invalidEmail
    except KeyError:
        return invalidEmail

    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_posts():
    id = request.form['id']
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM Timelinepost WHERE id = " + id)
    mydb.commit()
    output = str(mycursor.rowcount) + ", records(s) deleted \n"
    return output

@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('not_found.html', title="404 Error", url=os.getenv("URL")), 404