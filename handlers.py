from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types
from aiogram.types import FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


class Order(StatesGroup):
    name = State()


@router.callback_query(F.data == 'order')
async def order(callback: types.CallbackQuery):
    kb = [
        [InlineKeyboardButton(text='для ИЖС', url='https://forms.gle/mbdWoboKUU8KqcvX8')],
        [InlineKeyboardButton(text='другие работы (беседки, бани, кровля и др.)', url='https://forms.gle/aWtkXRZ4JWqQx8jNA')],
    ]
    inline_kb = InlineKeyboardMarkup(inline_keyboard=kb)

    await callback.message.answer(
        "Чтобы оставить заявку, заполните, пожалуйста, форму заказчика:",
        reply_markup=inline_kb
    )
    return


@router.callback_query(F.data == 'price_list')
async def price_list(callback: types.CallbackQuery):
    await callback.message.answer(
        "Актуальные цены и предложения: "
    )
    doc = FSInputFile('price_list.pdf', filename='price_list.pdf')
    await callback.message.answer_document(doc)
    return


@router.callback_query(F.data == 'project_explain')
async def project_explain(callback: types.CallbackQuery):
    await callback.message.answer(
        """
        Стандартный проект Ижс включает в себя :
    1. Образмеренные поэтажные планы
    2. Планы с площадями и обозначении комнат
    3. 4 cтороны фасада в цвете
    4. Характерные разрезы
    5. Планы перекрытия этажей
    6. Кровельный план
    7. Спецификации материалов
    8. Узлы сложных конструктивных моментов
    9. 3Д визуализация
        """
    )
    return


@router.callback_query(F.data == 'project_view')
async def order(callback: types.CallbackQuery):
    await callback.message.answer(
        "Вот примеры наших работ для ознакомления:"
    )
    doc = FSInputFile('preview.pdf', filename='preview.pdf')
    await callback.message.answer_document(doc)
    return



# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
# client = gspread.authorize(creds)
#
# sheet_id = "1l9TpwxswfgbGkx7O9Iz89JZntsEPkf7KCPHTBKXUI3A"
# workbook = client.open_by_key(sheet_id)
#
# sheets = workbook.worksheets()
# print(sheets)