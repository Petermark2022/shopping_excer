from flask import Flask, render_template, request
from faker import Faker

app = Flask(__name__)

#flask use decorator 'route' to build URL to a function

@app.route("/")
def story():
    # mystory = """I am a student"
    # " Do give me the platform"
    # " Its up to me to "
    # " what can I do help you"  
    # " No dulling. """

    fake = Faker()

#    mystory = (

#     f"<html><body><p>In a(n) {fake.company()}"

#     f" a young {fake.language_name()} stumbles across a(n) "

#     f"{fake.domain_word()} which spurs him into conflict with " 

#     f"{fake.name()} an {fake.catch_phrase()}"

#     f" with the help of a(n) {fake.job()} "

#     f" and her {fake.file_name()} culminating in a struggle in "

#     f"{fake.company()} where someone shouts: '{fake.sentence()}' </p></body></html>"
#    )

   

    mystory = "In a(n) " + fake.company()

    mystory = mystory + " a young "

    mystory = mystory + fake.language_name()

    mystory = mystory + " stumbles across a(n) "

    mystory = mystory + fake.domain_word()

    mystory = mystory + " which spurs him into conflict with " 

    mystory = mystory + fake.name()

    mystory = mystory + " an " + fake.catch_phrase()

    mystory = mystory + " with the help of a(n) " 

    mystory = mystory + fake.job()

    mystory = mystory + " and her "

    mystory = mystory + fake.file_name()

    mystory = mystory + " culminating in a struggle in "

    mystory = mystory + fake.company()

    mystory = mystory + " where someone shouts: "

    mystory = mystory + fake.bs() 
    

    return mystory

@app.route('/')
def index():
    mystory = story()
    return render_template("index.html", story=mystory)