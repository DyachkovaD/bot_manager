import logging
import asyncio
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from token_data import TOKEN
from handlers import router, Order

dp = Dispatcher()
dp.include_router(router)


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    kb = [
        [InlineKeyboardButton(text='Посмотреть наши проекты', callback_data='project_view')],
        [InlineKeyboardButton(text='Цены на услуги', callback_data='price_list')],
        [InlineKeyboardButton(text='Оставить заявку на работу', callback_data='order')],
        [InlineKeyboardButton(text='Что включает в себя проект ИЖС?', callback_data='project_explain')]
    ]
    inline_kb = InlineKeyboardMarkup(inline_keyboard=kb)

    await message.answer(f'Здравствуйте! Мы предоставляем услуги: \n'
                         f'- 3D проектирования зданий 🏠 \n'
                         f'- кровли \n'
                         f'- отдельных деталей сооружений \n'
                         f'- расчёт объемов материала по вашим эскизам, проектам \n'
                         f'- создание видео презентаций \n'
                         f'- и многое другое. \n\n'
                         f'К каждoму клиенту cвoй пoдхoд: видeo и обычныe '
                         f'конференции в удобноe для вас вpeмя, кoнсультация пo любым вoпросaм. '
                         f'Oнлайн кoнферeнции в pабочей мoдели для экoномии вaшeгo времени, расстановка мебели и не только. \n\n'
                         f'Опытный коллектив со стажем более 5 лет быстро и качественно выполнит Ваш заказ.'
                         
                         f'\n\nВыберете в меню 👇 интересующие вас вопросы или оставьте '
                         f'заявку на работу.',
                         reply_markup=inline_kb)
    return


async def main() -> None:
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



