from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_company = KeyboardButton(text="Kompaniya haqida")
mentorlar = KeyboardButton(text="Bizning Mentorlar")
kurslar = KeyboardButton(text="Kurslarimiz")
contact = KeyboardButton(text="Kontaktlar/Manzil")
language = KeyboardButton(text="Uzb/Eng Tili")

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [about_company, mentorlar],
        [kurslar],
        [contact, language]
    ],resize_keyboard=True
)
python_junior = KeyboardButton(text="Python Junior")
frontend_junior = KeyboardButton(text="Frontend Junior")
robototexnika = KeyboardButton(text="Robototexnika")
scratch = KeyboardButton(text="Scratch")
back = KeyboardButton(text="Ortga🔙")
kurslarimiz = ReplyKeyboardMarkup(
    keyboard=[
        [python_junior, frontend_junior],
        [robototexnika, scratch],
        [back]
    ]
)
Uzb = KeyboardButton(text="Uzbek tili")
Eng = KeyboardButton(text="English")
Back = KeyboardButton(text="Ortga🔙")
tillar = ReplyKeyboardMarkup(
    keyboard=[
        [Uzb, Eng],
        [Back]
    ], resize_keyboard=True
)
About_Company = KeyboardButton(text="About Company")
Our_mentors = KeyboardButton(text="Our mentors")
Our_courses = KeyboardButton(text="Our courses")
Contact_address = KeyboardButton(text="Contact/address")
Languages = KeyboardButton(text="Uzb/Eng languages")

english_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [About_Company, Our_mentors],
        [Our_courses],
        [Contact_address, Languages]
    ],resize_keyboard=True
)