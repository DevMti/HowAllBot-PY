# Imports for source
import logging
import random

# Imports from aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

# Bot token
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher and dp
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# For /start x or y
@dp.message_handler(regexp="/start ch")
async def starts(message: types.Message):

    # Chat reaction
    await message.answer_chat_action(action='typing')

    # Keyboard and awnser
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(types.InlineKeyboardButton("📢 Our Channel", url="https://t.me/OnTopTM"))
    await message.answer(
        text='Thanks for your support🙏',
        reply_markup=keyboard_markup
    )


# Start and help section
@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):

    # Chat reaction
    await message.answer_chat_action(action='upload_photo')

    # Keyboard and awnser
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(types.InlineKeyboardButton("🤝 share any thing!", switch_inline_query=""))
    await message.answer_photo(
        'https://on-top.ml/assets/start.jpg',
        caption='👋 Hi!\n\n💡 To use this bot, simply type \"@HowAllBot\" into your text box and click one of the results or click the button attached to this message (Share any thing).\n\n💬 To notice about new things in this bot please join in our Channel:\n📣 @OnTopTM',
        reply_markup=keyboard_markup
    )


# Send ads prices
@dp.message_handler(commands='ads')
async def send_ads(message: types.Message):

    # Chat reaction
    await message.answer_chat_action(action='typing')

    # Keyboard and awnser user with prices
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(types.InlineKeyboardButton("👉 Order Here 👈", url="https://t.me/DevMti"))
    await message.answer(
        "💬 Prices list\n\n1️⃣ Inline ads: Negotiable\n\n2️⃣ Ads on the channel: Negotiable\n\nTo order, send a message to the ID below with #ads\n** Spammers will be blocked **\n📣 @OnTopTM",
        reply_markup=keyboard_markup
    )


# Send inline result
@dp.inline_handler()
async def send_tests(inline_query: InlineQuery):

    # Just little set
    items = []
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(types.InlineKeyboardButton("🤝 share any thing!", switch_inline_query=""))

    # Show result for users, who is ready to send self tests
    if inline_query.query == "":

        items.append(InlineQueryResultArticle(
            id=1,
            title="❤️‍🔥 How horny are you?",
            description="Send Your Current Hornyess To This Chat.",
            input_message_content=InputTextMessageContent(f"❤️‍🔥 I am {random.randint(0,200)}% horny!"),
            reply_markup=keyboard_markup
        ))

    # Show tests for user, who is ready to send others result
    else:

        items.append(InlineQueryResultArticle(
            id=1,
            title=f"❤️‍🔥 How horny is {inline_query.query}?",
            description=f"Send {inline_query.query}'s Hornyess To This Chat.",
            input_message_content=InputTextMessageContent(f"❤️‍🔥 {inline_query.query} is {random.randint(0,200)}% horny!"),
            reply_markup=keyboard_markup
        ))

    items.append(InlineQueryResultArticle(
        id='help',
        title="🤝 Help",
        description="Send The Usage Guidelines To This Chat.",
        input_message_content=InputTextMessageContent("💡 Either press the button attached to this message and select the chat you would like to post in or simply enter \"@HowAllBot\" into your text box.\n\n💬 To notice about new things in this bot please join in our Channel:\n📣 @OnTopTM"),
        reply_markup=keyboard_markup
    ))

    # Show tests
    await bot.answer_inline_query(
        inline_query.id,
        cache_time=120,
        is_personal=True,
        switch_pm_text="💬 Support us by subscribing to the channel",
        switch_pm_parameter="ch",
        results=items
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
