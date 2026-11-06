
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from rag import ingest_pdf, ingest_website, answer_question

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    sources = []
    message = None
    question = ""

    if request.method == "POST":
        action = request.form.get("action")

        try:
            if action == "upload":
                file = request.files.get("pdf_file")

                if not file or not file.filename:
                    raise ValueError("Please select a PDF file.")

                if not file.filename.lower().endswith(".pdf"):
                    raise ValueError("Only PDF files are allowed.")

                filename = secure_filename(file.filename)
                path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(path)

                count = ingest_pdf(path)
                message = f"PDF processed successfully! Stored {count} text chunks."

            elif action == "website":
                url = request.form.get("url", "").strip()

                if not url:
                    raise ValueError("Please enter a website URL.")

                count = ingest_website(url)
                message = f"Website processed successfully! Stored {count} text chunks."

            elif action == "ask":
                question = request.form.get("question", "").strip()
                answer, sources = answer_question(question)

        except Exception as error:
            message = f"Error: {error}"

    return render_template(
        "index.html",
        answer=answer,
        sources=sources,
        message=message,
        question=question
    )


if __name__ == "__main__":
    app.run(debug=True)
