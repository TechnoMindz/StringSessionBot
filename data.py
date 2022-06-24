from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥Start Generating Session🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨SUPPORT✨", url="https://t.me/technomindzchat")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/technomindzbot")],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @TmMainChannel
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Source Code : [Click Here](https://t.me/technomindzbot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : [꧁𓊈𒆜🆁🅰🆅🅸🅽🅰🅽🅳🅰🅽𒆜𓊉꧂](https://t.me/technomindzyt)
    """
