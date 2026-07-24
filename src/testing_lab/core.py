import os
from pathlib import Path


def normalize_text(value: str) -> str:
    """Elimina espacios exteriores y convierte el texto a minusculas."""
    return value.strip().lower()


def classify_score(score: int) -> str:
    """Clasifica una puntuacion valida comprendida entre 0 y 100."""

    if type(score) is not int:
        raise TypeError("score must be an integer")

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score < 50:
        return "insuficiente"

    if score < 70:
        return "aprobado"

    if score < 90:
        return "notable"

    return "excelente"


def get_user_status(user_id, status_service):
    return status_service(user_id)


def get_execution_mode():
    return os.getenv("APP_MODE", "development")


def register_user(user_id, repository):
    if repository.exists(user_id):
        return False

    repository.save(user_id)
    return True


def normalize_file(source_path, destination_path):
    source = Path(source_path)
    destination = Path(destination_path)

    normalized = normalize_text(source.read_text(encoding="utf-8"))
    destination.write_text(normalized, encoding="utf-8")

    return destination


def build_user_response(user_id, status):
    return {
        "id": user_id,
        "status": status,
    }


def process_user_status(source_path, destination_path, user_id):
    normalized_path = normalize_file(source_path, destination_path)
    status = normalized_path.read_text(encoding="utf-8")

    return build_user_response(user_id, status)
