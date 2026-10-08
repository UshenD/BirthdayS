"""Birthday surprise website. Run locally:  streamlit run app.py
All text lives in content.py. Photos in photos/, music in music/.
"""
import base64, importlib, json, mimetypes
from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

import content

ROOT = Path(__file__).parent


def data_uri(path: Path, max_mb: float = 12) -> str | None:
    if not path.exists() or path.stat().st_size > max_mb * 1024 * 1024:
        return None
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


@st.cache_data(show_spinner=False)
def build_page(content_stamp: float) -> str:
    importlib.reload(content)
    c = content
    photos, chapters = {}, []
    for ch in c.CHAPTERS:
        items = []
        for fname, caption in ch["photos"]:
            uri = photos.get(fname) or data_uri(ROOT / "photos" / fname)
            if uri:                       # silently skip missing photos
                photos[fname] = uri
                with Image.open(ROOT / "photos" / fname) as im:
                    ratio = round(im.width / im.height, 3)
                items.append({"f": fname, "c": caption, "r": ratio})
        if items:
            chapters.append({"title": ch["title"], "blurb": ch.get("blurb", ""), "photos": items})
    hero = c.HERO_PHOTO
    if hero not in photos:
        uri = data_uri(ROOT / "photos" / hero)
        if uri:
            photos[hero] = uri
    data = {
        "title": c.PAGE_TITLE, "name": c.NAME, "subtitle": c.SUBTITLE,
        "signedBy": c.SIGNED_BY, "fromName": c.FROM_NAME,
        "gateTitle": c.GATE_TITLE, "gateText": c.GATE_TEXT, "gateButton": c.GATE_BUTTON,
        "music": data_uri(ROOT / c.MUSIC_FILE, 15),
        "hero": hero if hero in photos else None, "heroHint": c.HERO_HINT,
        "letterTitle": c.LETTER_TITLE, "letter": c.LETTER,
        "chapters": chapters, "photos": photos,
        "messages": c.RANDOM_MESSAGES, "randomButton": c.RANDOM_BUTTON,
        "cakeTitle": c.CAKE_TITLE, "cakeText": c.CAKE_TEXT, "cakeDone": c.CAKE_DONE_TITLE,
        "candles": max(1, min(9, int(getattr(c, "CANDLES", 5)))),
        "wishes": c.WISHES, "cakeAgain": c.CAKE_AGAIN_BUTTON,
        "footer": c.FOOTER_TEXT, "replay": c.REPLAY_BUTTON,
    }
    html = (ROOT / "site_template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return html.replace("/*__DATA__*/null", payload)


st.set_page_config(page_title=content.PAGE_TITLE, page_icon="🎂", layout="wide",
                   initial_sidebar_state="collapsed")

# Make the page fill the whole screen with no Streamlit chrome.
st.markdown(
    """
<style>
header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], [data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none !important}
html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"] {background:#1D0814 !important; overflow:hidden !important}
.block-container, [data-testid="stMainBlockContainer"] {padding:0 !important; max-width:100% !important}
[data-testid="stVerticalBlock"] {gap:0 !important}
iframe {position:fixed !important; inset:0; width:100vw !important; height:100dvh !important; border:0 !important; z-index:999}
</style>
""",
    unsafe_allow_html=True,
)

stamp = max(
    [(ROOT / f).stat().st_mtime for f in ("content.py", "site_template.html")]
    + [q.stat().st_mtime for q in (ROOT / "photos").glob("*")]
    + [q.stat().st_mtime for q in (ROOT / "music").glob("*")]
)
page = build_page(stamp)
if hasattr(st, "iframe"):                    # newer Streamlit
    st.iframe(page, height=900)
else:                                        # older Streamlit
    components.html(page, height=900, scrolling=True)
