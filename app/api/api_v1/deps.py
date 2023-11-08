from typing import Generator

from ...db.mongodb import db


def get_db() -> Generator:
    try:
        yield db
    finally:
        pass  # Aquí podrías cerrar la sesión si estuvieras usando un ODM/ORM que lo requiera