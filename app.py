
from flask import Flask, render_template
import os

app = Flask(
    __name__,
    static_folder=r"C:\rps website\static",
    template_folder=r"C:\rps website\templates"
)

print("Static folder:", app.static_folder)
print(
    "Games file exists:",
    os.path.isfile(r"C:\rps website\static\games.js")
)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)