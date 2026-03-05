"""AI-generated unit tests for interactions module."""
import pytest
from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id

def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")

# KEEP: Тест на граничное значение - максимальный item_id
def test_filter_with_max_item_id():
    """Test filtering with maximum possible item_id."""
    interactions = [
        _make_log(1, 1, 999999),
        _make_log(2, 2, 999999),
        _make_log(3, 3, 100)
    ]
    result = _filter_by_item_id(interactions, 999999)
    assert len(result) == 2
    assert all(i.item_id == 999999 for i in result)

# KEEP: Тест на пустой результат фильтрации
def test_filter_returns_empty_when_no_match():
    """Test filter returns empty list when no items match."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 999)
    assert result == []

# FIXED: Тест на несколько совпадений (был исправлен assertion)
def test_filter_multiple_matches():
    """Test filter returns multiple matches correctly."""
    interactions = [
        _make_log(1, 1, 5),
        _make_log(2, 2, 5),
        _make_log(3, 1, 5),
        _make_log(4, 3, 10)
    ]
    result = _filter_by_item_id(interactions, 5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)
