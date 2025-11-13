import pytest
from src.string_changer import (
    concatenate_strings_with_space,
    string_has_pattern,
    string_is_rich,
    insert_pattern_at_index
)

# --- concatenate_strings_with_space ---

def test_concatenate_normal_strings():
    """ Teste 1: caso normal com duas strings. """
    assert concatenate_strings_with_space("ola", "mundo") == "ola mundo"

def test_concatenate_with_empty_string():
    """ Teste 2: caso de borda com uma string vazia (ainda deve adicionar espaço). """
    assert concatenate_strings_with_space("hello", "") == "hello "

def test_concatenate_two_empty_strings():
    """ Teste 3: caso de borda com duas strings vazias. """
    assert concatenate_strings_with_space("", "") == " "

# --- string_has_pattern ---

def test_pattern_exists():
    """ Teste 1: verifica se o padro action está presente na string github actions. """
    assert string_has_pattern("github actions", "action") == True

def test_pattern_does_not_exist():
    """ Teste 2: padrão não é encontrado. """
    assert string_has_pattern("github actions", "python") == False

def test_pattern_is_case_sensitive():
    """ Teste 3: verifica se a busca é sensível a maiúsculas/minúsculas (deve ser sensível). """
    assert string_has_pattern("GitHub", "github") == False

# --- string_is_rich ---

def test_string_is_rich_true():
    """ Teste 1: string atende a todos os critérios. """
    assert string_is_rich("Senha Forte 123") == True

def test_string_is_rich_missing_space():
    """ Teste 2: string não atende ao critério de espaço. """
    assert string_is_rich("SenhaForte123!") == False

def test_string_is_rich_missing_uppercase():
    """ Teste 3: string não atende ao critério de letra maiúscula. """
    assert string_is_rich("senha forte 123!") == False

def test_string_is_rich_missing_digit():
    """ Teste 4: string não atende ao critério de dígito. """
    assert string_is_rich("Senha Forte !") == False

# --- insert_pattern_at_index ---

def test_insert_pattern_in_middle():
    """ Teste 1: caso normal inserindo no meio da string. """
    assert insert_pattern_at_index("ola mundo", "lindo ", 4) == "ola lindo mundo"

def test_insert_pattern_at_start():
    """ Teste 2: caso de borda inserindo no índice 0. """
    assert insert_pattern_at_index("mundo", "ola ", 0) == "ola mundo"

def test_insert_pattern_at_end():
    """ Teste 3: caso de borda inserindo no final. """
    assert insert_pattern_at_index("ola", " mundo", 3) == "ola mundo"