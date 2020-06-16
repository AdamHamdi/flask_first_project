from flask import Flask, render_template

app = Flask(__name__)

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
    }
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

