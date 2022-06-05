from src.settings import DATA_ROOT, LOGS_ROOT, UTCNOW


def test_settings():
    assert all([x is not None for x in (UTCNOW, LOGS_ROOT, DATA_ROOT)])
