from flask import Flask, render_template,url_for


app = Flask(__name__)
app.config['SECRET_Key']='5a921e1a22298afd89aec51bc29ea688'
posts=[
    {
        'author':'Corey Schfer',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Adam Hamdi',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'June 14,2020'
    },
    {
        'author':'Gbby Daniel',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'April 20,2019'
    },
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == "__main__":
    app.run(debug=True)


