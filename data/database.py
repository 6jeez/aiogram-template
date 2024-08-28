import json
import aiosqlite


async def initialize_db(db_path: str):
    """
    Инициализирует базу данных и создает таблицу users, если она еще не существует.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY
                )
            """
            )
            await db.commit()
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")


async def add_user_if_not_exists(db_path: str, user_id: int) -> bool:
    """
    Добавляет user_id в таблицу users, если его там нет.
    Возвращает True, если добавление прошло успешно, иначе False.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :param user_id: Идентификатор пользователя, который нужно добавить.
    :return: True, если user_id был добавлен, False, если он уже существует.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute(
                "SELECT 1 FROM users WHERE user_id = ?", (user_id,)
            ) as cursor:
                result = await cursor.fetchone()

            if result is None:
                await db.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
                await db.commit()
                return True
            else:
                return False
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        return False


def get_value_from_json(file_path: str, key: str):
    """
    Возвращает значение из JSON-файла по заданному ключу.

    :param file_path: Путь к JSON-файлу.
    :param key: Ключ, по которому нужно получить значение.
    :return: Значение, соответствующее заданному ключу, или None, если ключ не найден.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get(key, None)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при работе с файлом: {e}")
        return None
