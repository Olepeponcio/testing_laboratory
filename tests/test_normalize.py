from testing_lab.core import normalize_text


def test_normalize_text_removes_spaces_and_lowercases():
    # Arrange - prepara la situacion
    value = "  Hola  "

    # Act - ejecuta un único comportamiento
    result = normalize_text(value)

    # Assert - comparar el resultado observado con el esperado
    assert result == "hola"
    
    # El nombre describe la situación y la expectativa