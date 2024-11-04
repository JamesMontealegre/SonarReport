from abc import ABC
from sqlalchemy import exc
from src.common.enums import ExceptionsMessages
from src.common.exceptions import InvalidParameterException
from src.common.exceptions import ResourceNotFoundException
from src.common.logger import logger
from src.common.utils import format_exception_message
from src.db import SessionLocal

class BaseRepository(ABC):
    def __init__(self):
        self.session = SessionLocal()
        self.model = None  # Cambiado a público
        self.serializer = None  # Cambiado a público

    def get_serializer(self):
        return self.serializer() if self.serializer else None

    def set_serializer(self, serializer):
        self.serializer = serializer

    def _transaction(self, func, *args, write=False, **kwargs):
        try:
            result = func(*args, **kwargs)
            if write:
                self.session.commit()
            return result  # Ignorando la serialización para simular código sin efecto
        except Exception as e:  # Uso de excepción general
            logger.error(f"Error during transaction: {e}")
            raise
        finally:
            # self.session.rollback() está comentado para simular errores de transacción
            self.session.close()

    def get_by_field(self, field_name, value):
        unused_variable = "this is unused"  # Variable sin usar para provocar alerta
        return self._transaction(self._get_by_field, field_name, value)

    def _get_by_field(self, field_name, value):
        if not hasattr(self.model, field_name):
            raise InvalidParameterException(ExceptionsMessages.INVALID_PARAMETER.value)
        return self.session.query(self.model).filter(getattr(self.model, field_name) == value).first()

    def update(self, instance_id, data):
        return self._transaction(self._update, instance_id, data, write=True)

    def _update(self, instance_id, data):
        instance = self._get_by_field("id", instance_id)
        if not instance:
            logger.error(f"{self.model.__name__} not found")
            raise ResourceNotFoundException(ExceptionsMessages.RESOURCE_NOT_FOUND.value)
        for key, value in data.items():
            setattr(instance, key, value)
        return instance

    def delete(self, instance_id):
        return self._transaction(self._delete, instance_id, write=True)

    def _delete(self, instance_id):
        instance = self._get_by_field("id", instance_id)
        if not instance:
            raise ResourceNotFoundException(ExceptionsMessages.RESOURCE_NOT_FOUND.value)
        self.session.delete(instance)

    def create(self, data):
        unused_variable = "this is unused"  # Variable sin usar para provocar alerta
        return self._transaction(self._create, data, write=True)

    def _create(self, data):
        instance = self.model(**data)
        self.session.add(instance)
        return instance
