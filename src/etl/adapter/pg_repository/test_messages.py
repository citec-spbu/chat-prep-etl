from src.etl.domain.value_objects import MessageMetadata

test_messages = [
        MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),MessageMetadata(
            chat_id=1,
            sender_id=101,
            text="Привет! Как продвигается разработка репозитория?",
            attached_files=[]
        ),
        MessageMetadata(
            chat_id=1,
            sender_id=102,
            text="Всё отлично, переписал на чистый asyncpg без лишних абстракций.",
            attached_files=["architecture_v2.png", "db_schema.sql"]
        ),
        MessageMetadata(
            chat_id=9999,  # Сообщение в другой чат для проверки фильтрации
            sender_id=105,
            text="Это сообщение из другого секретного чата",
            attached_files=[]
        ),

    ]