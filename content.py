"""
=====================================================================
  EDIT THIS FILE TO CHANGE ANY TEXT ON THE WEBSITE
  (names, letter, captions, wishes). Save it, and the site updates.
  Photos live in the  photos/  folder. Music is  music/happy_birthday.mp3
=====================================================================
"""

# ---------- Basics ---------------------------------------------------------
PAGE_TITLE = "Something special for you"      # browser tab title

NAME = "CHUKKI"                 # <- her name / nickname, shown in big letters
SUBTITLE = "Today the whole world gets to celebrate you."
SIGNED_BY = "Yours, always"      # sign-off at the bottom of the letter
FROM_NAME = "MALLI"                   # <- your name (optional), shown after the sign-off

# ---------- Opening gift screen -------------------------------------------
GATE_TITLE = "Psst... this is for you"
GATE_TEXT = "Turn your sound on, then open your gift."
GATE_BUTTON = "Open your gift"

# ---------- Music ---------------------------------------------------------
# Path to the background music (relative to this folder).
# Want the real song? Drop your own mp3 into the music/ folder and change this.
MUSIC_FILE = "music/happy_birthday.mp3"

# ---------- Hero photo (the big arch photo at the top) --------------------
HERO_PHOTO = "wedding-02.jpg"    # any file name from the photos/ folder
HERO_HINT = "Tap me!"            # little hint under the photo

# ---------- The letter ----------------------------------------------------
LETTER_TITLE = "A little note for you"
LETTER = [
    "Happy birthday, my love.",
    "I put this together because words alone were never going to be enough. "
    "Scroll down and you'll find the little girl who started it all, the girl who grew up and "
    "lit up every room she walked into, and the woman who turned my life into something I'm "
    "so proud of.",
    "Thank you for every laugh, every quiet moment, every time you chose us. "
    "You make ordinary days feel like celebrations.",
    "Now go on, take your time with these memories. Every photo here is a reason I'm grateful for you.",
]

# ---------- Photo chapters -------------------------------------------------
# Each chapter has a title, a short line, and its photos (file name + caption).
# Reorder, rename, or delete anything. To add a photo: put it in photos/ and add a line.
CHAPTERS = [
    {
        "title": "Little you",
        "blurb": "Before I knew you, you were already wonderful.",
        "photos": [
            ("little-01-vintage-family.jpg", "Where it all began"),
            ("little-02.jpg", "Always up to something"),
            ("little-03.jpg", "Ready for the show"),
            ("little-04.jpg", "A day out"),
            ("little-05.jpg", "Party time"),
            ("little-06.jpg", "Stealing the show"),
            ("little-07.jpg", "A proud day"),
        ],
    },
    {
        "title": "Growing up, glowing up",
        "blurb": "Somehow every year, you got even more you.",
        "photos": [
            ("growing-01.jpg", "Effortlessly you"),
            ("growing-02.jpg", "Garden walls and good light"),
            ("growing-03.jpg", "Sunshine in the garden"),
            ("growing-04.jpg", "Saree o'clock"),
        ],
    },
    {
        "title": "Us",
        "blurb": "The best part of my story is the part with you in it.",
        "photos": [
            ("us-01.jpg", "Mirror selfies, early days"),
            ("us-02-photobooth.jpg", "Photo booth giggles"),
            ("us-03.jpg", "Still taking mirror selfies"),
            ("us-04.jpg", "A kiss for the camera"),
            ("us-05.jpg", "Just us"),
            ("us-06.jpg", "Cheek kisses"),
            ("us-07.jpg", "Sweet moments"),
            ("us-08.jpg", "Flowers for you"),
        ],
    },
    {
        "title": "Our big day",
        "blurb": "The day I couldn't stop smiling.",
        "photos": [
            ("wedding-01.jpg", "Forever starts here"),
            ("wedding-02.jpg", "The bride in red"),
        ],
    },
    {
        "title": "Our little miracle",
        "blurb": "And then our whole world got bigger.",
        "photos": [
            ("baby-01-snow.jpg", "Three of us, almost"),
            ("baby-02-newborn.jpg", "Hello, little one"),
            ("baby-03-park.jpg", "Mama and her little one"),
            ("baby-04-family.jpg", "Our little family"),
        ],
    },
    {
        "title": "Family, laughter and cake",
        "blurb": "Surrounded by people who love you.",
        "photos": [
            ("family-01-birthday.jpg", "Cake, balloons and the people who love you"),
            ("family-02-graduation.jpg", "Proud moments"),
            ("family-03-butterflies.jpg", "Butterflies and good company"),
            ("family-04.jpg", "Always a full house"),
            ("family-05.jpg", "Family selfie, mandatory"),
            ("family-06.jpg", "Cozy at home"),
            ("family-07.jpg", "Everyone squeezed in"),
            ("family-08.jpg", "Little hugs"),
            ("family-09-stairs.jpg", "The staircase gang"),
            ("family-10.jpg", "Adventures together"),
        ],
    },
]

# ---------- "Surprise me" button: random messages shown with a random photo
RANDOM_MESSAGES = [
    "You make ordinary days feel like celebrations.",
    "Look how far we've come.",
    "This smile is my favourite thing in the world.",
    "Proof that you've always been this wonderful.",
    "Some memories you keep. This one keeps you.",
    "Thank you for being you.",
    "Just look at that. Pure magic.",
]
RANDOM_BUTTON = "Surprise me"

# ---------- Make-a-wish cake ----------------------------------------------
CAKE_TITLE = "Make a wish"
CAKE_TEXT = "Close your eyes, think of your wish, then tap each flame to blow it out."
CAKE_DONE_TITLE = "It's going to come true."
CANDLES = 5                      # how many candles on the cake (1 to 9)
WISHES = [
    "May this year hold everything you've been quietly hoping for.",
    "May every day feel as special as today.",
    "May you always know how loved you are.",
]
CAKE_AGAIN_BUTTON = "Make another wish"

# ---------- Footer --------------------------------------------------------
FOOTER_TEXT = "Happy birthday. I love you."
REPLAY_BUTTON = "Play the song again"
