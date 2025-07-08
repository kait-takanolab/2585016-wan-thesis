from flask import Flask, request, render_template
import whisper
import os
from utils.scorer import calculate_score_only

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

model = whisper.load_model("base")

@app.route("/", methods=["GET", "POST"])
def index():
    targets = [
        "私は学校に行きます",
        "昨日は天気が良かったです",
        "明日は図書館で勉強します"
    ]

    if request.method == "POST":
        target = request.form.get("target")
        audio_file = request.files.get("audio")
        path = os.path.join(app.config["UPLOAD_FOLDER"], "user_audio.wav")
        audio_file.save(path)

        result = model.transcribe(path, language="ja")
        recognized = result.get("text", "")

        score, feedback = calculate_score_only(recognized, target)

        return render_template(
            "index.html",
            targets=targets,
            target=target,
            recognized=recognized,
            score=score,
            feedback=feedback
        )

    return render_template(
        "index.html",
        targets=targets,
        target=None,
        recognized=None,
        score=None,
        feedback=None
    )

if __name__ == "__main__":
    app.run(debug=True)