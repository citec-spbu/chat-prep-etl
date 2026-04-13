from testing_system.internal.domain.value_objects import RetrievedDocument
from testing_system.internal.adapter.assistants.mock import MockAssistant
from testing_system.internal.adapter.retrievers.mock import MockRetriever
from testing_system.internal.usecase.ProcessQuery import Processor

def mock_test():

    documents = [
        RetrievedDocument(
            id = 1,
            content="Рейс SU-1231 вылетает 15.05.26 в 09:40 из Санкт-Петербурга в Сочи, время в пути составит 3 часа 20 минут, приземление по местному времени (разница +0).",
            metadata=None
        ),
        RetrievedDocument(
            id = 2,
            content="USER-1, извини, я задержусь на презентацию сегодня вечером (начало в 19:00) — поеду не на такси, а на метро из-за перекрытия Тверской улицы, буду около 19:50.",
            metadata=None
        ),
        RetrievedDocument(
            id = 3,
            content="Агент, запланируй звонок в поликлинику на 22.04.26 в 11:30, чтобы записаться к окулисту; за час до этого напомни взять с собой старый рецепт на линзы.",
            metadata=None
        ),
        RetrievedDocument(
            id = 4,
            content="Посылка для USER-2 будет готова к забору сегодня в 16:00 от дома 14 по Ленинскому проспекту, вес 6.2 кг, нужно доставить её завтра до 12:00 в офис на Бауманской.",
            metadata=None
        ),
        RetrievedDocument(
            id = 5,
            content="Завтра, 14.04.26, с 15:00 до 18:00 ожидается ледяной дождь и гололедица, поэтому если поеду в аэропорт Домодедово, выеду на 2 часа раньше — в 10:30 вместо 12:30.",
            metadata=None
        ),
        RetrievedDocument(
            id = 6,
            content="Забронируй столик в итальянском ресторане «Форнелли» на пятницу 18.04.26 на 20:00 на троих, укажи, что нужно детское кресло и место подальше от сцены.",
            metadata=None
        ),
        RetrievedDocument(
            id = 7,
            content="Через 45 минут (ровно в 14:20) необходимо загрузить отчёт «Q2_v3_final.csv» в общую папку TeamDrive и скинуть ссылку USER-3 в Telegram.",
            metadata=None
        ),
        RetrievedDocument(
            id = 8,
            content="Завтра утром с 09:00 до 13:00 мастер заберёт ноутбук из сервисного центра на Парке Культуры, чек №АС-892 нужно сохранить и напомнить мне за 30 минут до выхода.",
            metadata=None
        ),
        RetrievedDocument(
            id = 9,
            content="Поезд №042А «Сапсан» отправляется 20.04.26 в 07:05 с Ленинградского вокзала в Нижний Новгород, прибытие в 10:56, место в вагоне 8, место 15C.",
            metadata=None
        ),
        RetrievedDocument(
            id = 10,
            content="USER-1, не забудь, что завтра в 18:30 у нашего сына выступление в школе (актовый зал, 3 этаж), я куплю цветы по пути, но если ты заберёшь младшего из сада до 17:00, то успеем без пробок.",
            metadata=None
        )
    ]

    retriever = MockRetriever(documents=documents)
    assistant = MockAssistant()

    usecase = Processor(
        assistant=assistant,
        retriever=retriever
    )

    questions = [
        "Во сколько вылетает рейс SU-1231?"
    ]

    for q in questions:
        print(f"User: {q}\n")
        response = usecase.execute(question=q, system_prompt= """Ты помощник, который отвечает на вопросы ТОЛЬКО на основе предоставленных документов.

Правила:
1. Используй ТОЛЬКО информацию из документов выше
2. Если в документах нет ответа, скажи: "У меня недостаточно информации для ответа"
3. Не добавляй свои знания и не делай предположений
4. Отвечай кратко и точно
5. При цитировании указывай ID документа

Документы представлены в формате: [ID]. [содержание]""")
        print(f"Assistant: {response.answer}\n")