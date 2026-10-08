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
GATE_TITLE = "Chukki... this is for you from your data scientist"
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
    "Happy birthday to the best sister in the world, my Chukki. ❤️",
    "I don't think words will ever be enough to explain how grateful I am to have you as my sister.",
    "From all our little fights and silly moments to all the memories we've made together, every moment with you is something I'll always treasure.",
    "You have grown from the little girl I knew into an amazing woman, and I couldn't be more proud of you.",
    "Thank you for every laugh, every conversation, every little moment, and for always being a part of my life.",
    "No matter how old we get or where life takes us, you'll always be my Chukki. ❤️",
    "I hope this birthday brings you all the happiness, love, and success you deserve.",
    "Keep smiling, keep shining, and never forget how much you mean to me.",
    "Happy Birthday, Chukki. ❤️🎂",
    "Love you always."
]

# ---------- Photo chapters -------------------------------------------------
# Each chapter has a title, a short line, and its photos (file name + caption).
# Reorder, rename, or delete anything. To add a photo: put it in photos/ and add a line.
CHAPTERS = [
    {
        "title": "Little you",
        "blurb": "Punchi yalu sangame.",
        "photos": [
            ("little-01-vintage-family.jpg", "Fontaine's"),
            ("little-02.jpg", "Us being us"),
            ("little-03.jpg", "imanka imanka"),
            ("little-04.jpg", "Hichchi Kale"),
            ("little-05.jpg", ""),
            ("little-06.jpg", "Love"),
            ("little-07.jpg", ""),
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
        "blurb": "Thank you for always being there.",
        "photos": [
            ("us-01.jpg", "Mirror selfies, early days"),
            ("us-02-photobooth.jpg", "Kathai"),
            ("us-03.jpg", "Still taking mirror selfies"),
            ("us-04.jpg", "Muwah"),
            ("us-05.jpg", ""),
            ("us-06.jpg", "Cheek kisses"),
            ("us-07.jpg", ""),
            ("us-08.jpg", "Flowers"),
        ],
    },
    {
        "title": "Your Chapter",
        "blurb": "The day I couldn't stop smiling.(Crying)",
        "photos": [
            ("wedding-01.jpg", "MY Couple"),
            ("wedding-02.jpg", "The bride"),
        ],
    },
    {
        "title": "Chloeeeee",
        "blurb": "And then your whole world got bigger.",
        "photos": [
            ("baby-01-snow.jpg", "Three of you"),
            ("baby-02-newborn.jpg", "Hello, little one"),
            ("baby-03-park.jpg", ""),
            ("baby-04-family.jpg", ""),
        ],
    },
    {
        "title": "Family, laughter and cake",
        "blurb": "Surrounded by people who love you and who you love.",
        "photos": [
            ("family-01-birthday.jpg", "Cake, balloons and the people who love you"),
            ("family-02-graduation.jpg", ""),
            ("family-03-butterflies.jpg", ""),
            ("family-04.jpg", "Always a full house"),
            ("family-05.jpg", ""),
            ("family-06.jpg", "Cozy at home"),
            ("family-07.jpg", ""),
            ("family-08.jpg", "Little hugs"),
            ("family-09-stairs.jpg", "Aula"),
            ("family-10.jpg", "Adventures"),
        ],
    },
]

# ---------- "Surprise me" button: random messages shown with a random photo
RANDOM_MESSAGES = [
    "No matter how much we fight, you'll always be my favourite person to annoy. 😂",
    "Growing up with you gave me some of my best memories.",
    "You may be my sister, but sometimes you feel like my best friend too. ❤️",
    "We've shared countless laughs, arguments, secrets, and memories.",
    "Life wouldn't be the same without my Chukki. 🫶🏻",
    "From being annoying little kids to growing up together, look how far we've come.",
    "I'll always be there for you, even when you don't want me to be. 😂",
    "You deserve all the happiness in the world, Chukki.",
    "Some people get a sister. I got a lifetime best friend.",
    "No matter where life takes us, you'll always have your brother. ❤️",
    "Thank you for being one of the most important parts of my life.",
    "Our bond may come with fights, but the love behind it will always be stronger.",
    "Just a little reminder that your brother loves you more than he says. ❤️",
    "Forever my little sister, forever my Chukki. 🎂"
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
