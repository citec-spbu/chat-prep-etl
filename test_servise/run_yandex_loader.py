import asyncio

from src.etl.usecase.Save_Data import SaveDataUseCase
from src.etl.adapter.yd_parser import YandexParser


class FakeRepository:
    async def save_batch(self, messages):
        print(f"\n✔ Сохранено сообщений: {len(messages)}")

        # выводим первые 3 для проверки
        for i, msg in enumerate(messages[:3]):
            print(f"\n--- Message {i+1} ---")
            print("TEXT:", msg.text[:100] if msg.text else "")
            print("FILES:", msg.attached_files)


async def main():
    # ===== Parser =====
    yandex_parser = YandexParser()

    # ===== Repository =====
    repository = FakeRepository()

    # ===== UseCase =====
    usecase = SaveDataUseCase(
        grabber=None,              # не нужен для YD
        repository=repository,
        html_grabber=None,           # если уже внутри парсера
        yd_parser=yandex_parser
    )

    # ===== ЗАПУСК =====
    await usecase.execute(
        source_type="yd",
        source="C:\Users\Alina\Desktop\chat-prep-etl\data\Telegram Tesla Chat ChatExport_2026-04-28.zip"
    )


if __name__ == "__main__":
    asyncio.run(main())