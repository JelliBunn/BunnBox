from flask import Flask, render_template, url_for, request
import random
import requests
import os
import subprocess

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1353568921760038962/2B_6f4GJ0dsPh0eFi6xxRzsff_WsZBRhEoHbSb2j2lUIBbd5Pg3YDwwIYUfmGxfx-BLh" # rogue surveilance

@app.before_request
def log_to_discord():
    # Exclude static file requests
    if request.path.startswith("/static"):
        return

    ip = request.remote_addr
    path = request.path

    payload = {
        "content": f"Visitor from `{ip}` accessed `{path}`"
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except Exception as e:
        print("Failed to send Discord message:", e)

@app.route("/bunnbox/mods")
def mods():
    images = ["bee.gif", "fox.gif", "blahaj.gif", "whitefox.gif"]
    weights = [33, 33, 33, 1]
    
    selected_image = random.choices(images, weights=weights, k=1)[0]
    image_url = url_for("static", filename=f"media/{selected_image}")
    return render_template("mods.html", background=image_url)

@app.route('/restart-bunnbox')
def restart_bunnbox():
    result = subprocess.run(
        ["sudo", "-u", "amp", "ampinstmgr", "restartinstance", "BunnBox01"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return "BunnBox01 restarted successfully", 200
    else:
        return f"Restart failed:\n{result.stderr}", 500


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("lost.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)

# this comment will appear if it's in the thing 