from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        email_text = request.form["email"]

        suspicious_words = [
            "urgent",
            "click here",
            "verify",
            "password",
            "bank",
            "account suspended"
        ]

        for word in suspicious_words:
            if word.lower() in email_text.lower():
                result = "⚠️ Phishing Email Detected"
                break

        if result == "":
            result = "✅ Legitimate Email"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)