import os
from multiprocessing.connection import answer_challenge

from aiogram import types, Router, F
from aiogram.types import FSInputFile

from handlers.keyboards import kurslarimiz, start_buttons, tillar, english_buttons

router = Router()

@router.message(F.text == "Kompaniya haqida")
async def get_about_company(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    text = "8 yillik tajribaga, 2000dan ortiq o'quvchilar va tajribali mentorlarga ega!"
    await msg.answer_photo(photo=company_image, caption=text)

@router.message(F.text == "Bizning Mentorlar")
async def get_mentorlar(msg: types.Message):
    img1 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    img2 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    img3 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    mentorlar = [
        [img1, "Habibulla Nuridinov"],
        [img2, "Abrorjon Abdusaidov"],
        [img3, "Shohruh Abdurahmonov"],
    ]
    for mentor in mentorlar:
        await msg.answer_photo(photo=mentor[0], caption=mentor[1])

@router.message(F.text == "Kurslarimiz")
async def get_kurslarimiz(msg: types.Message):
    await msg.answer(text="Bizning kurslarimiz", reply_markup=kurslarimiz)

@router.message(F.text == "Python Junior")
async def get_python_junior(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    text = "Python - Mantiqiy fikrlash va dasturlash asoslari"
    await msg.answer_photo(photo=img, caption=text)

@router.message(F.text == "Frontend Junior")
async def get_frontend_junior(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_6.png"))
    text = "Frontend in Development / board infinity"
    await msg.answer_photo(photo=img, caption=text)

@router.message(F.text == "Robototexnika")
async def get_robototexnika(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_7.png"))
    text = "Robototexnika va dasturlash"
    await msg.answer_photo(photo=img, caption=text)

@router.message(F.text == "Scratch")
async def get_scratch(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_8.png"))
    text = "Scratch va dasturlash"
    await msg.answer_photo(photo=img, caption=text)

@router.message(F.text == "Ortga🔙")
async def get_ortga(msg: types.Message):
    await msg.answer(text="Ortga", reply_markup=start_buttons)

@router.message(F.text == "Kontaktlar/Manzil")
async def get_contact(msg: types.Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_9.png"))
    text = "Bu yerda siz manzil tanlab olishingiz mumkin"
    await msg.answer_photo(photo=img, caption=text)

@router.message(F.text == "Uzb/Eng Tili")
async def get_languages(msg: types.Message):
    await msg.answer(text="Tillardan birini tanlang", reply_markup=tillar)

@router.message(F.text == "Uzbek tili")
async def get_uzb(msg: types.Message):
    await msg.answer(text="Siz Uzbek tilini tanladingiz!", reply_markup=start_buttons)

@router.message(F.text == "English")
async def get_english(msg: types.Message):
    await msg.answer(text="You have chosen English!", reply_markup=english_buttons)