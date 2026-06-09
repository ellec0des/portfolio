import flask
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Overfishing & CO₂ Dashboard",
        "description": "Interactive map showing overfishing and carbon emissions."
    },
    {
        "title": "Florida Freshwater Loss",
        "description": "Analysis of freshwater decline and environmental impacts."
    },
    {
        "title": "Clicks vs Bricks",
        "description": "E-commerce growth versus traditional retail."
    },
    {
        "title": "Haiti Agriculture Analysis",
        "description": "Data exploration of agriculture, food imports, and famine."
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects.html")
def project_page():
    return render_template("projects.html", projects=projects)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)