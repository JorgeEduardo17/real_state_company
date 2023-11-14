from typing import Generator

from ...db.mongodb import db


def get_db() -> Generator:
    """
    Generator that provides an instance of the database.

    This function is a dependency generator in FastAPI that can be used to inject the database into the
    the database into the routes. It is responsible for providing an instance of the database
    and, in case you are using an ORM/ODM that requires it, it could also handle the opening and closing of the database session.
    and closing of the database session.

    Yields:
        The database instance used by the application.

    Note:
    In this case, no specific action is taken to close the database connection,
    since it is assumed that the connection management is handled globally. If you were using an ODM/ORM
    that requires explicit session handling, this would be the place to close the session.
    """
    try:
        yield db
    finally:
        pass  # Aquí podrías cerrar la sesión si estuvieras usando un ODM/ORM que lo requiera