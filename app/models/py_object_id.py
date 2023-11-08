from bson import ObjectId


class PyObjectId(ObjectId):
    """Clase para manejar ObjectId de MongoDB en modelos Pydantic."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ObjectId no válido")
        # Devuelve el ObjectId como una cadena
        return str(ObjectId(v))

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
