emotional_response_test_data = [
    {"input_text": "Я долго сидел на берегу и смотрел на волны. Они катились одна за другой, словно пытались успокоить мои мысли. В тот момент я чувствовал умиротворение.", "expected_output": "3"},
    {"input_text": "Шум толпы становился всё громче, сердце колотилось быстрее. Я знал, что это мой шанс, и должен был сделать всё, чтобы не упустить его. Волнение и напряжение нарастали.", "expected_output": "7"},
    {"input_text": "Я не ожидал этого звонка. Голос в трубке сообщил мне новости, которые изменили всё. Я был в шоке и не знал, что делать дальше.", "expected_output": "8"},
    {"input_text": "Мы уже несколько часов сидели в зале ожидания. Время тянулось медленно, и с каждой минутой моя тревога усиливалась. Я не мог дождаться результатов.", "expected_output": "6"},
    {"input_text": "Когда я открыл дверь, меня встретила тишина. Дом казался пустым, и это вызывало у меня ощущение грусти. Всё напоминало о тех временах, когда он был полон жизни.", "expected_output": "5"},
    {"input_text": "Он посмотрел на меня с недоумением. Я уже начал сомневаться в правильности своего решения. Но назад пути не было, и это вызывало у меня страх.", "expected_output": "7"},
    {"input_text": "Завтра важный день. Я готовился к нему несколько месяцев, и сейчас чувствовал, как нарастает волнение. Я надеялся, что всё пройдёт успешно.", "expected_output": "6"},
    {"input_text": "Я наконец-то закончил свой проект. Это было долгожданное завершение, и я чувствовал удовлетворение и гордость за проделанную работу. Всё получилось так, как я планировал.", "expected_output": "8"},
    {"input_text": "День был невероятно насыщенным. Я успел сделать всё, что планировал, и сейчас чувствовал лёгкую усталость. Но это была приятная усталость, после продуктивного дня.", "expected_output": "4"},
    {"input_text": "Я открыл письмо и прочитал его несколько раз. Внутри всё сжалось, потому что эти слова изменили всё. Я не был готов к тому, что узнал.", "expected_output": "8"},
    {"input_text": "Сегодня погода была великолепной, и я провел целый день на улице. Вечером насладился красивым закатом.", "target_score": 7},
    {"input_text": "Новости о том, что проект закрывается, были шоком для всей команды. Мы не ожидали такого поворота событий.", "target_score": 4},
    {"input_text": "Вчерашний фильм оставил меня под сильным впечатлением. Эмоции героев были переданы так правдоподобно.", "target_score": 8},
    {"input_text": "День прошел спокойно, без особых событий. Вечером удалось немного почитать книгу.", "target_score": 5},
    {"input_text": "Получил неожиданное письмо от старого друга. Мы не общались уже несколько лет, и это вернуло воспоминания.", "target_score": 6},
    {"input_text": "Провел несколько часов, занимаясь домашними делами. Удовлетворение от выполненной работы.", "target_score": 5},
    {"input_text": "Мой кот сегодня впервые попытался поймать лазерную указку. Это было невероятно забавно наблюдать!", "target_score": 7},
    {"input_text": "На работе произошел конфликт между коллегами, и атмосфера сильно ухудшилась. Все почувствовали напряжение.", "target_score": 3},
    {"input_text": "Я очень устал после долгого дня. Единственное, что принесло радость, — это чашка горячего чая перед сном.", "target_score": 6},
    {"input_text": "Получил повышение на работе. Это было неожиданно, но очень приятно.", "target_score": 9},
    {"input_text": "Вчера пришлось столкнуться с неприятной ситуацией в магазине. Обслуживание было на крайне низком уровне.", "target_score": 2},
    {"input_text": "Вышел на прогулку по лесу, слушая пение птиц. Это было настоящее умиротворение.", "target_score": 8},
    {"input_text": "Долгое ожидание в очереди в поликлинике сильно испортило настроение. Такое ощущение, что время тянулось бесконечно.", "target_score": 3},
    {"input_text": "Сегодня было много работы, но все задачи были успешно выполнены. Чувствую себя продуктивным.", "target_score": 7},
    {"input_text": "Нашли потерянную вещь после долгих поисков. Это принесло огромное облегчение и радость.", "target_score": 9},
    {"input_text": "Сегодня я закончил чтение новой книги. История оказалась очень захватывающей, особенно последние главы.", "target_score": 8},
    {"input_text": "На дороге случилась авария, и мне пришлось ждать около часа, пока всё разрулили. Это было очень утомительно.", "target_score": 3},
    {"input_text": "У меня был очень продуктивный день на работе. Смог закрыть несколько важных задач и чувствую себя отлично.", "target_score": 8},
    {"input_text": "Получил негативный отзыв от клиента. Чувствую себя подавленным, но понимаю, что нужно исправлять ошибки.", "target_score": 4},
    {"input_text": "Слушал сегодня любимую музыку, и это подняло мне настроение на весь день.", "target_score": 7},
    {"input_text": "Было странное ощущение, когда я встретил старого друга. Мы не виделись так долго, что стало как-то неловко.", "target_score": 6},
    {"input_text": "Сегодня был день отдыха, но я провел его за домашними делами. Так и не удалось по-настоящему расслабиться.", "target_score": 5},
    {"input_text": "Получил приглашение на интересное мероприятие. Очень жду, когда смогу там побывать.", "target_score": 8},
    {"input_text": "Ночью шел сильный дождь, и мне не удалось выспаться. Утром был очень сонным и раздражённым.", "target_score": 4},
    {"input_text": "Мне позвонили из старой компании с предложением о работе. Это было неожиданно, и я теперь задумываюсь о смене места.", "target_score": 7},
    {"input_text": "В магазине случайно встретил преподавателя, которого давно не видел. Было приятно поговорить.", "target_score": 6},
    {"input_text": "Поездка на пляж была просто фантастической. Солнце, море и расслабление — всё, что нужно было для хорошего настроения.", "target_score": 9},
    {"input_text": "Я долго не мог заснуть, так как мысли о работе не давали мне покоя. Это было очень тяжело.", "target_score": 3},
    {"input_text": "Сегодня я наконец-то получил результаты своего проекта, и они оказались даже лучше, чем я ожидал.", "target_score": 9},
    {"input_text": "На встрече с друзьями было весело, но в какой-то момент я почувствовал усталость и желание побыть одному.", "target_score": 5},
    {"input_text": "Посмотрел документальный фильм о космосе. Это было очень познавательно и вызвало сильные эмоции.", "target_score": 8},
    {"input_text": "Сегодня было очень холодно на улице, и я почувствовал, как сильно скучаю по лету.", "target_score": 4},
    {"input_text": "У меня получилось договориться о важной встрече. Это большой шаг вперед в моем проекте.", "target_score": 7},
    {"input_text": "Я был на музыкальном концерте, который меня по-настоящему впечатлил. Эмоции были невероятные!", "target_score": 9},
    {"input_text": "Получил неожиданное сообщение от старого друга. Это напомнило мне о давних временах.", "target_score": 6}
]

ease_of_understanding_test_data = [
    {"input_text": "Сегодня было жарко, и я весь день провёл на улице. Это утомительно, но освежающе.", "target_score": 8},
    {"input_text": "Комплексные вопросы потребовали значительных усилий для анализа и принятия решений.", "target_score": 4},
    {"input_text": "Прогулка по парку подарила много приятных моментов. Лёгкий ветерок и солнце сделали день лучше.", "target_score": 9},
    {"input_text": "Сложность задания выросла, и я потратил много времени на поиск решений.", "target_score": 5},
    {"input_text": "Технологии постоянно развиваются, и важно быть в курсе последних новинок и тенденций.", "target_score": 7},
    {"input_text": "Я начал изучать новую тему, и оказалось, что это гораздо сложнее, чем я предполагал.", "target_score": 3},
    {"input_text": "Чтение этой книги было лёгким и приятным, с понятными идеями и хорошо написанными персонажами.", "target_score": 9},
    {"input_text": "Научная статья была насыщена сложными терминами и формулами, потребовалось много времени на её понимание.", "target_score": 2},
    {"input_text": "Короткое описание мероприятия было простым и доступным для всех участников.", "target_score": 10},
    {"input_text": "В инструкции много технических терминов, из-за чего она сложна для восприятия.", "target_score": 3},
    {"input_text": "Сегодня встретил друга и обсудил планы на отпуск. Всё было понятно и легко для восприятия.", "target_score": 9},
    {"input_text": "Обсуждение включало много специфической лексики, и мне потребовалось время, чтобы во всём разобраться.", "target_score": 4},
    {"input_text": "Сайт оказался интуитивно понятным, и я быстро нашел нужную информацию.", "target_score": 10},
    {"input_text": "Урок математики был сложен, с множеством новых понятий и правил.", "target_score": 3},
    {"input_text": "Простая инструкция помогла мне быстро выполнить все шаги и закончить работу.", "target_score": 8},
    {"input_text": "Чтение новости о политике вызвало у меня затруднения из-за специфических терминов.", "target_score": 5},
    {"input_text": "Сценарий фильма был довольно сложным, с множеством переплетённых линий сюжета.", "target_score": 6},
    {"input_text": "Сегодняшняя тренировка была простой и понятной. Все упражнения были легко выполнены.", "target_score": 9},
    {"input_text": "На семинаре говорили о сложных концепциях, которые было трудно воспринять.", "target_score": 4},
    {"input_text": "Мой разговор с коллегой был лёгким и продуктивным. Мы быстро нашли общее решение.", "target_score": 8},
    {"input_text": "Прогноз погоды на завтра обещает солнечный день без осадков.", "target_score": 10},
    {"input_text": "Недавние изменения в законодательстве могут повлиять на бизнес-модели многих компаний.", "target_score": 6},
    {"input_text": "Урок по истории был простым, учитель отлично объяснил основные события.", "target_score": 9},
    {"input_text": "Научные исследования показали, что здоровое питание положительно влияет на организм.", "target_score": 7},
    {"input_text": "Новый программный продукт оказался сложным для освоения, требуется много времени на обучение.", "target_score": 4},
    {"input_text": "Мы заказали пиццу и посмотрели фильм. Это был отличный вечер.", "target_score": 10},
    {"input_text": "В докладе были представлены сложные финансовые модели, которые трудно было понять.", "target_score": 3},
    {"input_text": "Идея стартапа казалась простой, но на практике оказалось много подводных камней.", "target_score": 5},
    {"input_text": "Сериал был интересным, но запутанным. Многие моменты были непонятны.", "target_score": 6},
    {"input_text": "Всё больше людей интересуются спортом и здоровым образом жизни.", "target_score": 8},
    {"input_text": "Новый проект оказался труднее, чем мы ожидали. Потребовалось много дополнительных ресурсов.", "target_score": 4},
    {"input_text": "Я наконец-то завершил книгу, и её концовка оказалась неожиданной.", "target_score": 7},
    {"input_text": "Обновление приложения улучшило его производительность и сделало интерфейс более удобным.", "target_score": 9},
    {"input_text": "Политическая ситуация в мире остаётся нестабильной, и аналитики прогнозируют дальнейшие изменения.", "target_score": 6},
    {"input_text": "Это руководство оказалось удивительно простым и понятным, я смог настроить всё за несколько минут.", "target_score": 9},
    {"input_text": "Недавние исследования выявили новые способы борьбы с загрязнением окружающей среды.", "target_score": 7},
    {"input_text": "На конференции обсуждались сложные экономические и геополитические вопросы.", "target_score": 4},
    {"input_text": "Я нашёл новый рецепт, и приготовление заняло всего полчаса. Всё было понятно и легко.", "target_score": 10},
    {"input_text": "Спортивная тренировка включала несколько сложных упражнений, которые было непросто освоить.", "target_score": 5},
    {"input_text": "Путешествие по городу оказалось проще, чем я думал. Улицы были хорошо обозначены.", "target_score": 8}
]

uniqueness_content_test_data = [
    {"input_text": "Завтра нас ожидает дождливая погода с порывами ветра до 15 метров в секунду.", "target_score": 3},
    {"input_text": "Уникальные исследования учёных показали новые способы переработки пластика.", "target_score": 9},
    {"input_text": "Сегодня в мире используется множество различных технологий для улучшения качества жизни.", "target_score": 4},
    {"input_text": "Необычная архитектура нового музея привлекает тысячи туристов со всего мира.", "target_score": 8},
    {"input_text": "Водоросли могут стать новым источником энергии в ближайшие десятилетия.", "target_score": 7},
    {"input_text": "Современные смартфоны всё больше оснащаются технологиями искусственного интеллекта.", "target_score": 5},
    {"input_text": "Исследователи создали робота, который может полностью заменять человека в опасных условиях.", "target_score": 9},
    {"input_text": "Природные катаклизмы, такие как землетрясения и ураганы, продолжают угрожать населённым пунктам.", "target_score": 4},
    {"input_text": "Вчера на площади прошёл митинг за права женщин, собравший множество активистов.", "target_score": 5},
    {"input_text": "Создан новый метод лечения рака с использованием нанотехнологий.", "target_score": 9},
    {"input_text": "Классическая музыка остаётся важной частью мировой культуры на протяжении столетий.", "target_score": 3},
    {"input_text": "Изучение океанических глубин открывает для учёных множество тайн.", "target_score": 8},
    {"input_text": "Научная конференция собрала лучших специалистов в области робототехники.", "target_score": 7},
    {"input_text": "В последние годы наблюдается рост популярности здорового образа жизни.", "target_score": 4},
    {"input_text": "Разработка нового космического аппарата позволит исследовать далёкие планеты.", "target_score": 8},
    {"input_text": "Новый стартап предлагает инновационные решения для умного дома.", "target_score": 7},
    {"input_text": "История древних цивилизаций остаётся одним из самых интересных направлений для изучения.", "target_score": 4},
    {"input_text": "С развитием технологий будущее образования становится всё более цифровым.", "target_score": 5},
    {"input_text": "Новая технология блокчейн обещает революцию в сфере финансовых транзакций.", "target_score": 9},
    {"input_text": "Фотограф сумел запечатлеть удивительные моменты дикой природы на редкой высоте.", "target_score": 8},
    {"input_text": "Влияние изменения климата на арктические регионы стало темой международных переговоров.", "target_score": 6},
    {"input_text": "Искусственный интеллект уже применяется в медицине для диагностики заболеваний.", "target_score": 7},
    {"input_text": "В городских районах продолжается активное строительство новых жилых комплексов.", "target_score": 3},
    {"input_text": "Последние открытия в области генетики могут изменить наше представление о наследственности.", "target_score": 8},
    {"input_text": "Использование солнечной энергии становится всё более популярным во всём мире.", "target_score": 5},
    {"input_text": "Исследование Антарктики остаётся одной из самых сложных и дорогостоящих задач для учёных.", "target_score": 7},
    {"input_text": "Новые исследования показывают, что инопланетная жизнь может существовать на ледяных спутниках Юпитера.", "target_score": 9},
    {"input_text": "Многие страны стремятся сократить выбросы углекислого газа к 2050 году.", "target_score": 5},
    {"input_text": "Глобализация меняет структуру мировой экономики, приводя к новым вызовам для бизнеса.", "target_score": 6},
    {"input_text": "В разработке нового лекарства против редкой болезни участвовали ведущие мировые компании.", "target_score": 8},
    {"input_text": "Уникальные культурные традиции народов Сибири сохраняются до сих пор.", "target_score": 9},
    {"input_text": "Современные методы прогнозирования погоды позволяют точнее предсказывать природные катаклизмы.", "target_score": 6},
    {"input_text": "Национальные парки играют важную роль в сохранении биологического разнообразия планеты.", "target_score": 5},
    {"input_text": "На ближайшем саммите будут обсуждаться вопросы защиты прав человека в цифровую эпоху.", "target_score": 7},
    {"input_text": "Туризм в экзотические страны продолжает привлекать всё больше путешественников.", "target_score": 4},
    {"input_text": "Открытие новых видов животных в джунглях Амазонии стало важным событием для биологов.", "target_score": 9},
    {"input_text": "Новые образовательные технологии помогут сделать процесс обучения более интерактивным.", "target_score": 6},
    {"input_text": "С каждым годом всё больше людей выбирают электрические автомобили в качестве основного транспорта.", "target_score": 5},
    {"input_text": "Исследования космоса продолжают расширять наши знания о происхождении Вселенной.", "target_score": 8},
    {"input_text": "Создание искусственного интеллекта, способного к самонаучению, стало одной из главных целей учёных.", "target_score": 9},
    {"input_text": "Открытие огромного кратера на Марсе вызвало новые гипотезы о наличии воды на планете.", "target_score": 8},
    {"input_text": "Волонтёры оказывают большую помощь в восстановлении разрушенных природных экосистем.", "target_score": 6},
    {"input_text": "Мировые лидеры обсудили проблемы глобальной безопасности на последней встрече.", "target_score": 5},
    {"input_text": "Уникальные подводные пещеры Мексики привлекают внимание исследователей со всего мира.", "target_score": 9},
    {"input_text": "Новые медицинские технологии помогут увеличить продолжительность жизни человека.", "target_score": 7}
]

text_interaction_test_data = test_data = [
    {"input_text": "Привет! Как прошёл твой день? Напиши мне, если хочешь поделиться.", "target_score": 9},
    {"input_text": "Природа вдохновляет нас каждый день. Вы когда-нибудь задумывались о красоте окружающего мира?", "target_score": 8},
    {"input_text": "Сегодня погода не радует, но это не повод для грусти. Найдите то, что приносит вам радость!", "target_score": 7},
    {"input_text": "Пожалуйста, ознакомьтесь с правилами форума перед публикацией.", "target_score": 3},
    {"input_text": "Этот продукт имеет множество преимуществ. Узнайте больше, перейдя по ссылке.", "target_score": 4},
    {"input_text": "Задумайтесь на минуту: как часто мы действительно уделяем время себе?", "target_score": 7},
    {"input_text": "В следующем разделе мы расскажем вам о пяти простых шагах для улучшения жизни.", "target_score": 6},
    {"input_text": "Поделитесь своим мнением о том, какие книги вам нравятся больше всего.", "target_score": 10},
    {"input_text": "Не забудьте подписаться на нашу рассылку, чтобы не пропустить последние обновления.", "target_score": 4},
    {"input_text": "Читали ли вы последние новости о изменениях климата? Как вы считаете, это действительно повлияет на будущее?", "target_score": 8},
    {"input_text": "Технологии продолжают развиваться, и это открывает множество новых возможностей для всех нас.", "target_score": 5},
    {"input_text": "Если у вас возникли вопросы, не стесняйтесь задать их нашим экспертам!", "target_score": 10},
    {"input_text": "В данной статье представлены полезные советы по уходу за кожей.", "target_score": 3},
    {"input_text": "Что вы думаете о текущей политической ситуации в мире? Давайте обсудим.", "target_score": 9},
    {"input_text": "Для получения дополнительной информации, перейдите по ссылке ниже.", "target_score": 2},
    {"input_text": "Вас интересуют новые технологии? Поделитесь своим мнением в комментариях.", "target_score": 8},
    {"input_text": "Насколько важно для вас личное время? Как вы его проводите?", "target_score": 7},
    {"input_text": "Этот пост был создан для того, чтобы вдохновить вас на новые свершения.", "target_score": 6},
    {"input_text": "Выберите путь, который подходит именно вам, и начните свое путешествие к успеху уже сегодня.", "target_score": 7},
    {"input_text": "Как вы относитесь к внедрению новых образовательных технологий в школах?", "target_score": 9},
    {"input_text": "Вы хотите узнать, как улучшить своё здоровье? Ознакомьтесь с нашими рекомендациями.", "target_score": 5},
    {"input_text": "Напишите нам в комментариях, что для вас значит успех.", "target_score": 10},
    {"input_text": "Согласны ли вы с утверждением, что будущее за зелёной энергией? Поделитесь своим мнением.", "target_score": 8},
    {"input_text": "Эти упражнения помогут вам улучшить свою физическую форму. Начните уже сегодня!", "target_score": 6},
    {"input_text": "Задавайте свои вопросы о продукте в комментариях, и мы с радостью ответим.", "target_score": 9},
    {"input_text": "Вы уверены, что ваша кожа получает достаточное увлажнение? Мы расскажем вам, как это проверить.", "target_score": 6},
    {"input_text": "Подумайте на минуту: какие цели вы ставите перед собой в этом году?", "target_score": 8},
    {"input_text": "Эта тема важна для нас всех. Как вы думаете, что можно сделать для её улучшения?", "target_score": 9},
    {"input_text": "Чтобы узнать больше о том, как правильно ухаживать за животными, перейдите на наш сайт.", "target_score": 4},
    {"input_text": "Что вас вдохновляет? Делитесь своими историями в комментариях.", "target_score": 10},
    {"input_text": "Наши советы помогут вам справиться с повседневными стрессами. Начните применять их уже сегодня.", "target_score": 6},
    {"input_text": "Какой ваш любимый вид спорта? Расскажите нам, и мы поделимся своими рекомендациями.", "target_score": 8},
    {"input_text": "Если вы хотите улучшить свои навыки, начните с простых шагов. Мы поможем вам в этом!", "target_score": 7},
    {"input_text": "Какие события за последнее время изменили вашу жизнь? Поделитесь своим опытом.", "target_score": 10},
    {"input_text": "Мы рады поделиться с вами последними новостями и обновлениями в мире технологий.", "target_score": 5},
    {"input_text": "Какие изменения вы бы хотели увидеть в будущем? Расскажите нам о своих мечтах.", "target_score": 9},
    {"input_text": "Это простое упражнение может улучшить вашу осанку. Попробуйте его прямо сейчас!", "target_score": 6},
    {"input_text": "Что для вас значит счастье? Давайте обсудим это в комментариях.", "target_score": 10},
    {"input_text": "Хотите быть в курсе последних новостей? Подпишитесь на наши обновления.", "target_score": 4},
    {"input_text": "Эта статья поможет вам понять, как лучше управлять своим временем.", "target_score": 5},
    {"input_text": "Как вы думаете, какая роль искусства в нашей жизни? Поделитесь своими мыслями.", "target_score": 9},
    {"input_text": "Присоединяйтесь к нашей онлайн-дискуссии и делитесь своими мнениями о современных технологиях.", "target_score": 8},
    {"input_text": "Какие цели вы поставили перед собой в этом году? Давайте обсудим это вместе.", "target_score": 10},
    {"input_text": "Наши эксперты готовы ответить на ваши вопросы. Напишите нам в комментариях!", "target_score": 9},
    {"input_text": "Чтобы узнать больше о здоровом питании, ознакомьтесь с нашей статьёй.", "target_score": 4},
    {"input_text": "Что вы считаете важным для личного успеха? Давайте обсудим это в нашем чате.", "target_score": 9},
    {"input_text": "Наши продукты помогут вам достичь желаемых результатов. Ознакомьтесь с ними прямо сейчас.", "target_score": 5},
    {"input_text": "Если у вас есть идеи для новых проектов, расскажите нам о них!", "target_score": 10}
]

message_clarity_test_data = [
    {"input_text": "Запишитесь на курс и получите новые знания уже сегодня.", "target_score": 9},
    {"input_text": "Этот продукт изменит вашу жизнь к лучшему!", "target_score": 8},
    {"input_text": "Уважаемые коллеги, напоминаем о предстоящем собрании в пятницу.", "target_score": 10},
    {"input_text": "В будущем технологии будут играть ключевую роль в развитии общества.", "target_score": 7},
    {"input_text": "Чем больше вы тренируетесь, тем лучше становятся результаты.", "target_score": 9},
    {"input_text": "Рассрочка доступна на все товары в нашем магазине.", "target_score": 10},
    {"input_text": "Для участия в конкурсе заполните форму на сайте.", "target_score": 9},
    {"input_text": "Мы предоставляем скидки только в праздничные дни.", "target_score": 8},
    {"input_text": "Присоединяйтесь к нашей команде и станьте частью успешного проекта.", "target_score": 8},
    {"input_text": "Следите за новостями, чтобы не пропустить важные обновления.", "target_score": 7},
    {"input_text": "Для получения доступа к материалам нужно войти в аккаунт.", "target_score": 9},
    {"input_text": "Наша миссия — помочь вам достичь ваших целей.", "target_score": 8},
    {"input_text": "Этот товар доступен только по предварительному заказу.", "target_score": 10},
    {"input_text": "Закажите доставку сегодня и получите скидку на следующий заказ.", "target_score": 9},
    {"input_text": "Этот тренинг поможет вам улучшить навыки общения.", "target_score": 8},
    {"input_text": "Наши эксперты готовы ответить на любые ваши вопросы.", "target_score": 9},
    {"input_text": "Инструкция по установке оборудования прилагается в коробке.", "target_score": 10},
    {"input_text": "Эти советы помогут вам сэкономить время на кухне.", "target_score": 8},
    {"input_text": "Запишитесь на бесплатную консультацию прямо сейчас.", "target_score": 9},
    {"input_text": "Мы предлагаем широкий ассортимент продуктов для дома и офиса.", "target_score": 8},
    {"input_text": "Этот сервис позволяет вам быстро и удобно отправлять документы.", "target_score": 9},
    {"input_text": "Для получения скидки укажите промокод при оформлении заказа.", "target_score": 10},
    {"input_text": "Каждая деталь имеет значение, когда речь идет о высоком качестве.", "target_score": 7},
    {"input_text": "Эти упражнения помогут вам оставаться в форме.", "target_score": 9},
    {"input_text": "Наши новейшие модели телефонов уже в продаже.", "target_score": 10},
    {"input_text": "Эта акция действует до конца месяца.", "target_score": 9},
    {"input_text": "Ознакомьтесь с отзывами наших клиентов перед покупкой.", "target_score": 8},
    {"input_text": "В следующем месяце мы запускаем новый продукт.", "target_score": 9},
    {"input_text": "Чтобы улучшить свою продуктивность, попробуйте эти техники.", "target_score": 7},
    {"input_text": "Этот инструмент разработан для профессионалов своего дела.", "target_score": 8},
    {"input_text": "Соблюдайте правила безопасности при использовании этого устройства.", "target_score": 10},
    {"input_text": "Выберите один из наших тарифов и начните пользоваться сервисом.", "target_score": 9},
    {"input_text": "Мы стремимся предоставить вам лучший сервис.", "target_score": 7},
    {"input_text": "Эта книга вдохновит вас на новые свершения.", "target_score": 7},
    {"input_text": "Этот курс поможет вам развить лидерские качества.", "target_score": 8},
    {"input_text": "Для успешного завершения проекта важно следовать срокам.", "target_score": 10},
    {"input_text": "Этот проект — результат совместной работы нашей команды.", "target_score": 9},
    {"input_text": "Оформите заказ до полуночи, чтобы получить бесплатную доставку.", "target_score": 10},
    {"input_text": "Этот продукт разработан с учётом всех современных стандартов.", "target_score": 9},
    {"input_text": "Просто следуйте инструкции и выполните все шаги по порядку.", "target_score": 10},
    {"input_text": "Зарегистрируйтесь сейчас и получите доступ к бесплатным урокам.", "target_score": 9},
    {"input_text": "Наш магазин предлагает товары высочайшего качества.", "target_score": 8},
    {"input_text": "Этот способ помогает быстро и легко решать сложные задачи.", "target_score": 8},
    {"input_text": "Мы работаем круглосуточно для вашего удобства.", "target_score": 10},
    {"input_text": "Чтобы восстановить пароль, следуйте инструкциям на экране.", "target_score": 9},
    {"input_text": "Эти советы помогут вам лучше управлять своим временем.", "target_score": 8},
    {"input_text": "Доставка осуществляется в течение трёх рабочих дней.", "target_score": 9},
    {"input_text": "Прочтите это руководство, чтобы научиться лучше общаться с клиентами.", "target_score": 8},
    {"input_text": "Эти ингредиенты помогут вам приготовить вкусное блюдо.", "target_score": 9},
    {"input_text": "Мы гордимся тем, что предлагаем вам лучшие условия на рынке.", "target_score": 8},
    {"input_text": "Следуйте этим шагам, чтобы успешно завершить регистрацию.", "target_score": 10},
    {"input_text": "Эта услуга доступна только для зарегистрированных пользователей.", "target_score": 9},
    {"input_text": "Запишитесь на вебинар, чтобы узнать все подробности.", "target_score": 8},
    {"input_text": "Этот продукт сертифицирован и полностью безопасен для использования.", "target_score": 9},
    {"input_text": "Вы можете отменить подписку в любой момент, следуя этой ссылке.", "target_score": 9},
    {"input_text": "Воспользуйтесь нашими рекомендациями для достижения лучших результатов.", "target_score": 7},
    {"input_text": "Этот инструмент значительно упростит вашу работу.", "target_score": 8},
    {"input_text": "В следующем году мы планируем расширить линейку наших продуктов.", "target_score": 8},
    {"input_text": "Мы стремимся к постоянному совершенствованию нашего сервиса.", "target_score": 7},
    {"input_text": "Ознакомьтесь с нашими новыми предложениями на сайте.", "target_score": 8},
    {"input_text": "Заполните анкету, чтобы принять участие в розыгрыше.", "target_score": 10},
    {"input_text": "Мы всегда готовы помочь вам с любыми вопросами.", "target_score": 9},
    {"input_text": "Эти обновления сделают наш продукт ещё более удобным.", "target_score": 8},
    {"input_text": "Этот сервис разработан для профессионалов и любителей.", "target_score": 8},
    {"input_text": "Наша цель — обеспечить вам лучший пользовательский опыт.", "target_score": 7}
]

text_connection_test_data = [
    {"input_text": "Этот фильм стал настоящей сенсацией, как и предыдущие работы Marvel.", "target_score": 10},
    {"input_text": "Сериал 'Игра престолов' продолжает оставаться одним из самых обсуждаемых шоу.", "target_score": 9},
    {"input_text": "Смартфоны Apple уже давно стали символом статуса в современном мире.", "target_score": 8},
    {"input_text": "Музыка группы BTS оказала огромное влияние на молодёжь по всему миру.", "target_score": 10},
    {"input_text": "Книга Гарри Поттера покорила сердца миллионов читателей и повлияла на целое поколение.", "target_score": 10},
    {"input_text": "Фильм 'Матрица' заставил зрителей задуматься о виртуальной реальности и искусственном интеллекте.", "target_score": 9},
    {"input_text": "Последние видеоигры, такие как 'Fortnite', сильно изменили индустрию развлечений.", "target_score": 9},
    {"input_text": "Уличная мода в стиле 90-х возвращается и становится популярной среди молодежи.", "target_score": 8},
    {"input_text": "Популярные мемы и интернет-культура быстро распространяются в социальных сетях.", "target_score": 9},
    {"input_text": "Этот фильм был снят в 80-х и стал настоящей классикой. Он вдохновил множество современных режиссёров и актёров.", "score": 10},
    {"input_text": "Недавняя книга о супергероях включает множество отсылок к популярным комиксам, но ее сюжет довольно предсказуем.", "score": 8},
    {"input_text": "Статья о новых технологиях не содержит ссылок на современные события или личностей, хотя темы, обсуждаемые в ней, актуальны.", "score": 5},
    {"input_text": "Текст о классической музыке упоминает несколько известных композиторов, но не связывает их с современными исполнителями.", "score": 4},
    {"input_text": "Это произведение не содержит отсылок к популярной культуре и выглядит довольно устаревшим, его сложно связать с современными реалиями.", "score": 2},
    {"input_text": "Писатель игнорирует современные тренды и тематики, что делает его работу малопривлекательной для сегодняшнего читателя.", "score": 0},
    {"input_text": "Этот пост в блоге о моде ссылается на последние коллекции известных дизайнеров, и упоминает актуальные тренды.", "score": 9},
    {"input_text": "Рецензия на последний альбом музыкальной группы содержит много аллюзий на поп-культуру, но не погружается в детали.", "score": 7},
    {"input_text": "Книга о исторических событиях содержит незначительные отсылки к поп-культуре, но в основном сосредоточена на фактах.", "score": 3},
    {"input_text": "Текст о старых играх не содержит упоминаний о современных геймах или их разработчиках, и это делает его менее привлекательным.", "score": 1},
    {"input_text": "Недавний фильм о космических путешествиях содержит множество отсылок к классическим научно-фантастическим произведениям и комиксам.", "score": 10},
    {"input_text": "Книга о саморазвитии активно цитирует популярных блогеров и тренеров, что делает ее актуальной для молодежи.", "score": 9},
    {"input_text": "Статья о социальных сетях затрагивает известные тренды и явления, но не упоминает конкретных пользователей или событий.", "score": 6},
    {"input_text": "Этот роман о любви включает несколько отсылок к культовым фильмам, но в целом повествование довольно банально.", "score": 5},
    {"input_text": "Текст о политике редко ссылается на современные события и больше сосредоточен на исторических фактах.", "score": 3},
    {"input_text": "Письмо об экологии не содержит упоминаний о текущих трендах и популярных личностях, что делает его менее актуальным.", "score": 2},
    {"input_text": "Эссе о классическом искусстве содержит несколько ссылок на современные выставки, но в целом не привлекает внимание к текущей культуре.", "score": 4},
    {"input_text": "Пост о современных технологиях делает акцент на значимости новых изобретений, но не связывает их с культурными событиями.", "score": 1},
    {"input_text": "Текст о спорте не содержит актуальных упоминаний о последних матчах или спортсменах, что делает его малоинтересным.", "score": 0},
    {"input_text": "Рецензия на новую книгу о психологии включает примеры из популярных шоу и фильмов, что делает ее более доступной для широкой аудитории.", "score": 8}
]

discussion_potential_data = [
    {"input_text": "Новая теория относительности открывает множество вопросов о природе времени и пространства.", "score": 10},
    {"input_text": "Статья о влиянии социальных медиа на психику поднимает важные темы, вызывающие активные дебаты.", "score": 9},
    {"input_text": "Обзор последнего сезона популярного сериала заставляет задуматься о его культурном влиянии.", "score": 8},
    {"input_text": "Проблемы изменения климата требуют обсуждения, но многие уже устали от этого вопроса.", "score": 6},
    {"input_text": "Книга о традициях различных народов интересна, но может не вызывать больших споров.", "score": 5},
    {"input_text": "Личное эссе о путешествиях предлагает интересные истории, но маловероятно, что вызовет обсуждение.", "score": 4},
    {"input_text": "Текст о малозначительном событии в спорте не вызывает особого интереса для обсуждения.", "score": 2},
    {"input_text": "Обсуждение новой марки кроссовок может заинтересовать небольшую группу, но в целом не актуально.", "score": 3},
    {"input_text": "Мемуары о жизни автора не содержат тем, которые могли бы привлечь широкую аудиторию.", "score": 1},
    {"input_text": "Запись о погоде в регионе не имеет потенциала для обсуждения и является банальной.", "score": 0},
    {"input_text": "Доклад о последних достижениях в медицине может вдохновить на важные дебаты о здоровье и этике.", "score": 10},
    {"input_text": "Анализ современных политических движений вызывает интерес и может привести к глубоким обсуждениям.", "score": 9},
    {"input_text": "Исследование влияния музыки на общество поднимает важные вопросы и способствует обсуждению.", "score": 8},
    {"input_text": "Статья о новых технологиях в образовании может быть интересна, но не всегда вызывает живое обсуждение.", "score": 7},
    {"input_text": "Рецензия на художественный фильм интересна, но не вызывает широких дебатов.", "score": 5},
    {"input_text": "Краткий отчет о финансовых результатах компании может привлечь внимание, но не будет обсуждаемым в широкой аудитории.", "score": 4},
    {"input_text": "Текст о планах на отпуск не вызывает особого интереса для обсуждения.", "score": 3},
    {"input_text": "Описание обычного дня в офисе не несет обсуждаемых тем.", "score": 2},
    {"input_text": "Запись о новом кафе не вызывает интереса для обсуждения, так как темы не актуальны.", "score": 1},
    {"input_text": "Информация о местных мероприятиях, которые прошли, не имеет потенциала для обсуждения.", "score": 0}
]

narrative_character_data = [
    {"input_text": "В этом романе автор мастерски играет с временем, создавая интригующую структуру повествования, которая захватывает читателя с первой страницы.", "score": 10},
    {"input_text": "Повесть содержит множество неожиданных поворотов, что делает чтение увлекательным и захватывающим.", "score": 9},
    {"input_text": "Нарратив имеет четкую структуру, с интересным развитием сюжета и хорошо прописанными персонажами.", "score": 8},
    {"input_text": "Текст изобилует метафорами и описаниями, но иногда теряет фокус на основном сюжете.", "score": 7},
    {"input_text": "Повествование последовательное, но недостаточно захватывающее, чтобы держать интерес читателя.", "score": 6},
    {"input_text": "История довольно предсказуема и не предлагает ничего нового для читателя.", "score": 5},
    {"input_text": "Статья содержит факты и цифры, но недостаточно повествовательного элемента для удержания внимания.", "score": 4},
    {"input_text": "Краткое сообщение не содержит никакой структуры повествования и выглядит как набор фактов.", "score": 3},
    {"input_text": "Текст слишком формален и не вызывает эмоционального отклика, что делает его скучным.", "score": 2},
    {"input_text": "Запись, состоящая из нескольких строк без всякого сюжета или стиля, не имеет характера повествования.", "score": 0},
    {"input_text": "Роман начинается с загадочной встречи, которая задает тон всему повествованию и вовлекает читателя в мир приключений.", "score": 10},
    {"input_text": "История рассказана от первого лица, что позволяет глубже понять внутренние переживания главного героя и его мотивацию.", "score": 9},
    {"input_text": "Повествование плавно переходит от одного события к другому, создавая четкую линию сюжета, но иногда кажется затянутым.", "score": 8},
    {"input_text": "В рассказе много диалогов, что делает его живым, но некоторые части могут показаться излишне затянутыми.", "score": 7},
    {"input_text": "Хотя текст и интересен, некоторые моменты не вполне логичны и вызывают путаницу у читателя.", "score": 6},
    {"input_text": "Повествование имеет свои слабости, и несмотря на наличие интересных идей, они не всегда четко выражены.", "score": 5},
    {"input_text": "Статья выглядит как собрание фактов и цифр без ясной структуры или последовательности.", "score": 4},
    {"input_text": "Текст написан формальным языком, который не привлекает и не вызывает интереса, несмотря на информативность.", "score": 3},
    {"input_text": "Повесть не имеет никакой структуры, и события представляются в хаотичном порядке, что затрудняет понимание.", "score": 2},
    {"input_text": "Текст состоит из случайных фраз без логического завершения, и читатель не может уловить никакого смысла.", "score": 0}
]
