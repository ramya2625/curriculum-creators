from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generator", methods=["GET", "POST"])
def generator():
    curriculum = None

    if request.method == "POST":
        skill = request.form.get("skill")
        level = request.form.get("level")
        weeks = request.form.get("weeks")

        curriculum = f"""
        📘 Curriculum for {skill}

        Level: {level}
        Duration: {weeks} Weeks

        Week 1-4: Basics & Fundamentals
        Week 4-8: Core Concepts
        Week 8-12: Advanced Topics
        Final Week: Project & Assessment
        """

    return render_template("generator.html", curriculum=curriculum)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)