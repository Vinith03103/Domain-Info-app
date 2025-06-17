from flask import Flask, render_template, request
import whois

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    info = {}
    if request.method == "POST":
        domain = request.form["domain"]
        try:
            domain_info = whois.whois(domain)
            for key, value in domain_info.items():
                info[key] = str(value)
        except:
            info["Error"] = "Invalid or unavailable domain."

    return render_template("index.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)
