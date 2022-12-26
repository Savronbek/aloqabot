msgs = {
  "welcome": "Добро пожаловать! Вас приветствует бот. ",
  "start": "Ну что ж, начнем. Удачи",
  "begin": "Начинаем тест",
  "finish": "Конец! Ваш результат:",
  "select": "Выберите доступный тест",
  "wrong": "✖️",
  "right": "✔️",
  "is_ready": "Готовы?",
  "help": "Бот\-викторина по банкингу, Этот бот проверит ваши знания по банковской сфере\.\n\n Бот был создан при поддержке *«Billy\'s boys & Йожик»*\n\n работников банка 'Алокабанк' В\. В\.\nКостюченко А\. В\.",
  "error": "Эх жаль, случилась ошибка, попробуйте еще раз"
}

test1_questions = [
  {
    "content": "Выделите основную функцию ЦБ:",
    "options": [
      { "content": "срочные вклады;", "is_right": False },
      { "content": "предоставление кредитов;", "is_right": False },
      { "content": "эмиссия денег", "is_right": True },
      { "content": " оплата чеков;", "is_right": False },
      { "content": " финансирование государственных экономических программ;", "is_right": False },
    ]
  },
  {
    "content": "Коммерческие банки:",
    "options": [
      { "content": "осуществляют контроль над денежной массой в стране;", "is_right": False },
      { "content": " привлекают свободные денежные средства и размещают их в форме ссуд;", "is_right": True },
      { "content": " используют средства пенсионных фондов", "is_right": False },
      { "content": "занимаются эмиссией денег  ", "is_right": False },
    ]
  },
  {
    "content": "Кредит – это:",
    "options": [
      { "content": " финансирование государственных экономических программ;", "is_right": False },
      { "content": "ссуды на условиях возвратности и платности;", "is_right": True },
      { "content": "доверие кредитора заемщику;", "is_right": False },
      { "content": "привлечение денежных средств банками;", "is_right": False },
    ]
  },
  {
    "content": "Вклады, которые снимаются целиком в оговоренный срок:",
    "options": [
      { "content": "текущие;", "is_right": False },
      { "content": "до востребования;", "is_right": False },
      { "content": " срочные;", "is_right": True },
      { "content": "чековые;", "is_right": False },
    ]
  },
  {
    "content": "Прибыль банка – это:",
    "options": [
      { "content": "процент по депозитам;", "is_right": False },
      { "content": "процент по кредитам;", "is_right": False },
      { "content": " разница всех доходов и расходов;", "is_right": False },
      { "content": "разница между ставками процента по кредитам и депозитам;", "is_right": True },
    ]
  },
  {
    "content": "К пассивным операциям относится:",
    "options": [
      { "content": "предоставление ссуд;", "is_right": False },
      { "content": " сделки с недвижимостью;", "is_right": False },
      { "content": "прием вкладов;", "is_right": True },
      { "content": "операции с ценными бумагами;", "is_right": False },
    ]
  },
  {
    "content": "К активным операциям банка относится:",
    "options": [
      { "content": "выдача кредитов;", "is_right": True },
      { "content": "прием вкладов;", "is_right": False },
      { "content": "накопление прибыли;", "is_right": False },
      { "content": " создание резервов;", "is_right": False },
    ]
  },
  {
    "content": "Уменьшение учётной ставки ЦБ, скорее всего, приведёт:",
    "options": [
      { "content": "к снижению процентов по кредитам;", "is_right": True },
      { "content": "к увеличению процентов по кредитам;", "is_right": False },
      { "content": "никак не скажется на ссудном проценте;", "is_right": False },
    ]
  },
  {
    "content": "Процентная ставка, под которую ЦБ выдает кредит коммерческим банкам:",
    "options": [
      { "content": "норма обязательных резервов;", "is_right": False },
      { "content": "разность между процентными ставками по кредиту и депозиту;", "is_right": False },
      { "content": "депозитарный процент;", "is_right": False },
      { "content": "учетная ставка ЦБ;", "is_right": True },
    ]
  },
  {
    "content": " В банковскую систему входят:",
    "options": [
      { "content": "страховые компании, банки, инвестиционные фирмы;", "is_right": False },
      { "content": "коммерческие банки;", "is_right": False },
      { "content": "Центральный эмиссионный банк и сеть коммерческих банков;", "is_right": True },
      { "content": "Народный банк и государственные специализированные банки", "is_right": False },
    ]
  }
]

test2_questions = [
  {
    "content": "Центральный банк:",
    "options": [
      { "content": "собирает налоги;", "is_right": False },
      { "content": "хранит все наличные деньги;", "is_right": False },
      { "content": "обеспечивает устойчивость сума;", "is_right": True },
    ]
  },
  {
    "content": "Ниже приведён перечень функций, выполняемых банками\. Все они, за исключением двух, относятся к сфере деятельности коммерческих банков",
    "options": [
      { "content": "открытие и обслуживание пластиковых карт;", "is_right": False },
      { "content": "покупка и продажа валюты;", "is_right": False },
      { "content": "выдача кредитов гражданам;", "is_right": False },
      { "content": "обслуживание счетов фирм;", "is_right": False },
      { "content": "назначение учётной ставки;", "is_right": True },
      { "content": "эмиссия денег;", "is_right": True },
    ]
  },
  {
    "content": "Сергей решил открыть своё дело и обратился в банк за предоставлением кредита на приобретение материалов\. Какие ещё функции выполняют коммерческие банки? Выберите из приведённого списка нужные позиции и запишите цифры, под которыми они указаны: ",
    "options": [
      { "content": " осуществление расчётов и платежей", "is_right": True },
      { "content": " предоставление страховых услуг", "is_right": False },
      { "content": "приём вкладов", "is_right": True },
      { "content": "регулирование денежного обращения", "is_right": False },
      { "content": "денежная эмиссия", "is_right": False },
      { "content": " поддержка курса национальной валюты", "is_right": False },
    ]
  },
  {
    "content": "Укажите основные условия выдачи кредита: ",
    "options": [
      { "content": "срочность", "is_right": True },
      { "content": " выгодность", "is_right": False },
      { "content": "безвозмездность", "is_right": False },
      { "content": "бессрочность", "is_right": False },
      { "content": "платность", "is_right": True },
      { "content": "возвратность", "is_right": True },
    ]
  },
  {
    "content": "Ссудный процент \– это: ",
    "options": [
      { "content": "долг заемщика кредитору;", "is_right": False },
      { "content": "сумма кредита, которую заемщик обязан вернуть кредитору;", "is_right": False },
      { "content": "плата за кредит;", "is_right": False },
      { "content": "прибыль банка;", "is_right": True },
    ]
  },
  {
    "content": "Главной формой отчетности центрального банка является: ",
    "options": [
      { "content": "отчет о прибылях и убытках", "is_right": False },
      { "content": "платежный баланс", "is_right": False },
      { "content": "баланс", "is_right": True },
      { "content": "годовой отчет", "is_right": False },
    ]
  },
  # {
  #   "content": "Золотовалютными резервами Великобритании управляет: ",
  #   "options": [
  #     { "content": "и владеет Королевский двор", "is_right": False; },
  #     { "content": "ЕЦБ", "is_right": False; },
  #     { "content": "Банк Англии от имени Казначейства", "is_right": True },
  #     { "content": "Европейский Экономический и Валютный Союз", "is_right": False },
  #   ]
  # },
  {
    "content": "Где расположена штаб-квартира Совета по исламским финансовым услугам(IFSB):",
    "options": [
      { "content": " Турция", "is_right": False },
      { "content": " Бахрейн", "is_right": False },
      { "content": " Саудовская Аравия", "is_right": False },
      { "content": " Малайзия", "is_right": True },
    ]
  },
  {
    "content": "Банковская система, свойственная административно-командной экономике и полностью зависящая от указаний правительства",
    "options": [
      { "content": "децентрализованная банковская система", "is_right": False },
      { "content": "банковская система с линейно-штабной структурой управления", "is_right": False },
      { "content": "централизованная банковская система", "is_right": False },
      { "content": "распределительная банковская система", "is_right": True },
    ]
  },
  {
    "content": "Развитие вторичного рынка исламских ценных бумаг и разработка новых финансовых инструментов для исламского финансового рынка является функционалом",
    "options": [
      { "content": "Council for Islamic Banks and Financial Institutions (CIBAFI)", "is_right": False },
      { "content": "The Islamic Finance Service Board»(IFSB)", "is_right": False },
      { "content": "Международного центра по управлению ликвидностью", "is_right": True },
      { "content": "The International Islamic Financial Market", "is_right": False },
    ]
  }
]

tests = [
  {
    "name": "Тест №1",
    "questions": test1_questions
  },
  {
    "name": "Тест №2",
    "questions": test2_questions
  }
]
