
import logging
import string
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.types.message import ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from data import msgs
from utils import get_initial_state, ask_question, get_test_questions, get_test_list_markup, print_result
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
logging.basicConfig(level=logging.INFO)

# Config


TOKEN = '1993000522:AAHyDAquMqjnqc4KvT6y94tDRkZbF9dvjCk'

# Bot
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

global_state = {}






# States
class Form(StatesGroup):
    name = State() 
    age = State()       
    address = State()  
    gender = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Начатие разговора    
    """
    await Form.name.set()

    await message.reply("Assalomu aleykum! Ismingizni kiriting:\n Здравствуйте, введите ваше имя:")


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Отмена любого state
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # отмена стейта и оповещение юзера об отмене 
    await state.finish()
    # удаляем кнопку (если есть)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Обработка имени
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("Yoshingiz nechchida?\n Сколько вам лет?")


# age.isdigit()
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    """
    если возраст не число
    """
    return await message.reply("Возраст должен быть в цифрах.\nСколько вам лет? (только цифры)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # обновляем state и data
    await Form.next()
    await state.update_data(age=int(message.text))
    await message.reply("Siz ishlaydigan joyning manzilini kiriting.\nВведите место вашего филиала!")




@dp.message_handler(state=Form.address)
async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text

    await Form.next()

    # настройка ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Мужской", "Женский")
    markup.add("Другой")
    await message.reply("Jinsingizni kiriting.\nВыберите ваш пол", reply_markup=markup)



@dp.message_handler(lambda message: message.text not in ["Мужской", "Женский", "Другой"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    Пол должен быть одним из в списке
    """
    return await message.reply("Неправильный пол. Выберите из клавиатуры.")


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        # Remove keyboard
        markup = types.ReplyKeyboardRemove()   
        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Привет! Рад знакомству,', data['name']),
                md.text('Возраст:', data['age']),
                md.text('Пол:', data['gender']),
                md.text('Адрес:', data['address']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    # конец разговора
    await state.finish()








# Actions
@dp.message_handler(commands=['go'])
async def start(msg: Message):
  await msg.answer(msgs['welcome'])
  await msg.answer(msgs['start'], reply_markup=get_test_list_markup())

@dp.message_handler(commands=['help'])
async def help(msg: Message):
  await msg.answer(msgs['help'], parse_mode=ParseMode.MARKDOWN_V2)

@dp.message_handler(content_types=ContentType.ANY)
async def default_reply(msg: Message):
  await msg.delete()


async def question_player(msg: Message, state):
  cid = msg.chat.id
  global_state[cid] = state

  await ask_question(msg, global_state[cid])


async def answer_question(msg: Message, option):
  cid = msg.chat.id
  state = global_state[cid]

  is_right = option[2] in 'right'

  # hilight the right answer
  question = get_test_questions(state['test_name'])[
    state['current_question']]

  alphabet = list(string.ascii_uppercase)

  question_msg = f"*№{state['current_question'] + 1} {question['content']}*\n\n"

  for i, question_option in enumerate(question['options']):
    if alphabet[i] == option[1]:
      question_msg += f"*{alphabet[i]}: {question_option['content']}* {'✅' if is_right else '❌'}\n"
    else:
      question_msg += f"*{alphabet[i]}:* {question_option['content']} {'✅' if question_option['is_right'] else ''}\n"

  await msg.edit_text(question_msg, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=None)

  # manage state
  state['current_question'] += 1
  if is_right:
    state['score'] += 1

  if state['current_question'] == len(get_test_questions(state['test_name'])):
    del global_state[cid]
    await print_result(msg, state)
    await msg.answer(msgs['select'], reply_markup=get_test_list_markup())
    return

  global_state[cid] = state

  # continue test
  await question_player(msg, global_state[cid])

# Handlers
@dp.callback_query_handler()
async def btn_handler(query: CallbackQuery):
  cid = query.message.chat.id

  if 'create_test' in query.data:
    await query.message.edit_reply_markup()  # clear btn
    await question_player(query.message, get_initial_state(query.data.split('_')[2]))
    await query.answer(msgs['begin'])

  elif 'wrong' in query.data or 'right' in query.data:
    # [№, char, 'wrong' | 'right']
    await answer_question(query.message, query.data.split('_'))
    await query.answer(msgs[query.data.split('_')[2]])

  else:
    await bot.send_message(cid, msgs['error'])

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
