from flask import Flask, render_template
from severanceDavidTypeSound import typeSoundDavid
from threading import Thread
import time
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("myfleshbleedsacidgrey.html")
def run_flask():
    app.run(debug=False, use_reloader=False)
def main():
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    time.sleep(5)
    typeSoundDavid("Hello? Is anyone out there? It's so cold")
    time.sleep(50)
if __name__ == "__main__":
    main()