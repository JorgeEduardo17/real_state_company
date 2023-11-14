from fastapi import HTTPException


def handle_db_error(error):
    """
    Maneja errores de base de datos y lanza una excepción HTTP.

    Esta función se utiliza para interceptar errores relacionados con operaciones de base de datos y
    convertirlos en excepciones HTTP que pueden ser manejadas por FastAPI para enviar respuestas
    adecuadas a los clientes. Lanza una excepción HTTP con un código de estado 500, lo que indica un error del servidor.

    Args:
        error: El error de base de datos capturado, generalmente una excepción.

    Raises:
        HTTPException: Una excepción HTTP con un estado 500 y un mensaje de detalle que contiene la información del error original.
    """
    raise HTTPException(status_code=500, detail=str(error))