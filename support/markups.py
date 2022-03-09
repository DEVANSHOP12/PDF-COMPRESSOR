from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('join US FOR MORE ', url='t.me/TEAM_SILENT_KING'),
            InlineKeyboardButton('Source', url='github.com/Dvansh20055')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/TEAM_SILNET_KING'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
