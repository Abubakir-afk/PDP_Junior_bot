import os

from aiogram import Router, types
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup
from .keyboards import start_buttons

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    text = "Assalomu aleykum PDP Junior botiga xush kelibsiz"
    await message.answer_photo(photo=img, caption=text, reply_markup=start_buttons)