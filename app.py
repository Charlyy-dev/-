import sqlite3

from flask import Flask, request, jsonify
app = Flask(__name__)

# Подключение к базе данных (например, SQLite)
db = sqlite3.connect("comments.db")


@app.route("/comment", methods=["POST"])
def add_comment():
    comment_text = request.json["comment"]
    # Вставьте комментарий в базу данных
    db.execute("INSERT INTO comments (text) VALUES (?)", (comment_text,))
    db.commit()
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)

