# Birthday surprise site

## Run it on your computer
    pip install -r requirements.txt
    streamlit run app.py

## Change any text
Open `content.py`, edit the words between the quotes, save. (Name, letter, captions, wishes, button labels, number of candles.)

## Change photos / music
- Photos are in `photos/`. To add one: drop the file in, then add a line to a chapter in `content.py`.
- Music is `music/happy_birthday.mp3`. Replace the file (keep the name, or change `MUSIC_FILE` in `content.py`).

## Put it online (free) with Streamlit Community Cloud
1. Create a GitHub repo and upload everything in this folder (app.py, content.py, site_template.html, requirements.txt, .streamlit/, photos/, music/).
   Keep the repo PRIVATE if you like; Streamlit can still deploy it.
2. Go to share.streamlit.io, sign in with GitHub, click "Create app", pick the repo, main file = app.py, Deploy.
3. Copy the link it gives you and send it to her. Test it on your phone first.
Tip: in the app's Settings you can pick a short custom subdomain, e.g. happybirthday-yourname.streamlit.app

Changing text later: edit content.py on GitHub, commit, and the live site updates in a minute.
