from dataclasses import dataclass

@dataclass(frozen=True)
class Emoji:
    # Smileys & Emotion
    SMILE = "\U0001F600"  # 😀
    GRIN = "\U0001F603"  # 😃
    JOY = "\U0001F602"  # 😂
    HEART_EYES = "\U0001F60D"  # 😍
    SUNGLASSES = "\U0001F60E"  # 😎
    THINKING = "\U0001F914"  # 🤔
    HUG = "\U0001F917"  # 🤗

    # Events & Celebration
    PARTY = "\U0001F389"  # 🎉
    CONFETTI = "\U0001F38A"  # 🎊
    TROPHY = "\U0001F3C6"  # 🏆
    GOLD_MEDAL = "\U0001F947"  # 🥇

    # Nature & Weather
    EARTH = "\U0001F30D"  # 🌍
    SUN = "\U00002600"  # ☀️
    MOON = "\U0001F31C"  # 🌜
    STAR = "\U00002B50"  # ⭐
    SNOWMAN = "\U00002603"  # ⛄

    # Objects & Symbols
    LIGHT_BULB = "\U0001F4A1"  # 💡
    FIRE = "\U0001F525"  # 🔥
    CHECK_MARK = "\U00002705"  # ✅
    CROSS_MARK = "\U0000274C"  # ❌
    HOURGLASS = "\U000023F3"  # ⏳
    STOP_SIGN = "\U0001F6D1"  # 🛑
    SPEAKER = "\U0001F4E2"  # 📢

    # Food & Drink
    PIZZA = "\U0001F355"  # 🍕
    BURGER = "\U0001F354"  # 🍔
    FRIES = "\U0001F35F"  # 🍟
    APPLE = "\U0001F34E"  # 🍎
    WATERMELON = "\U0001F349"  # 🍉
    DONUT = "\U0001F369"  # 🍩
    COFFEE = "\U00002615"  # ☕

    # Music & Announcements
    MUSIC_NOTE = "\U0001F3B5"  # 🎵
    HEADPHONES = "\U0001F3A7"  # 🎧
    MICROPHONE = "\U0001F3A4"  # 🎤
    MEGAPHONE = "\U0001F4E3"  # 📣
    BELL = "\U0001F514"  # 🔔

    # Video
    VIDEO_CAMERA = "\U0001F3A5"  # 🎥
    FILM_FRAMES = "\U0001F39E"  # 🎞️
    CLAPPER_BOARD = "\U0001F3AC"  # 🎬

    # Pictures
    CAMERA = "\U0001F4F7"  # 📷
    CAMERA_WITH_FLASH = "\U0001F4F8"  # 📸
    FRAME_WITH_PICTURE = "\U0001F5BC" # 🖼️

    # Mail and letters
    MAIL_BOX = "\U0001F4EB"  # 📫
    POST_BOX= "\U0001F4EE" # 📮
    ENVELOPE = "\U00002709"  # ✉️
    EMAIL = "\U0001F4E7"  # 📧 (Envelope with an "@" symbol)
    INCOMING_ENVELOPE = "\U0001F4E8"  # 📨 (Incoming mail)
    OUTBOX_TRAY = "\U0001F4E4"  # 📤 (Outbox tray)
    INBOX_TRAY = "\U0001F4E5"  # 📥 (Inbox tray)

    # Hearts (All Colors)
    RED_HEART = "\U00002764"  # ❤
    BLUE_HEART = "\U0001F499"  # 💙
    GREEN_HEART = "\U0001F49A"  # 💚
    YELLOW_HEART = "\U0001F49B"  # 💛
    PURPLE_HEART = "\U0001F49C"  # 💜
    BLACK_HEART = "\U0001F5A4"  # 🖤
    WHITE_HEART = "\U0001F90D"  # 🤍
    ORANGE_HEART = "\U0001F9E1"  # 🧡
    BROWN_HEART = "\U0001F90E"  # 🤎

    # Animals
    CAT = "\U0001F408"  # 🐈
    DOG = "\U0001F415"  # 🐕
    PANDA = "\U0001F43C"  # 🐼
    RABBIT = "\U0001F407"  # 🐇
    TIGER = "\U0001F405"  # 🐅
    UNICORN = "\U0001F984"  # 🦄

    @classmethod
    def list_all(cls):
        """Returns all emoji mappings."""
        return {attr: getattr(cls, attr) for attr in dir(cls) if not attr.startswith("_") and attr.isupper()}
