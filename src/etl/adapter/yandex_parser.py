from src.etl.domain.value_objects import MessageMetadata

class YandexParser:

    def parse(self, source: str) -> List[MessageMetadata]:
        # TODO: реализовать парсинг HTML/архива Яндекс.Диска

        print(f"[YandexParser] called with source: {source}")

        return []