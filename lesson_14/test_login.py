import pytest
from lesson_14 import log_event
from datetime import datetime
import os

def setup_module(module):
    if not os.path.exists('login_system.log'):
        with open('login_system.log', 'w'):
            pass

@pytest.mark.parametrize("user, status",
[
    ("Anna", "success"),
    ("Vlad", "expired"),
    ("Liza", "failed")
])
def test_logging(user: str, status: str):
    setup_module(None)
    log_event(user, status)
    with open('login_system.log', 'r') as log_file:
        content = log_file.read()
        assert any(f"Username: {user}, Status: {status}" in line for line in content.splitlines())

if __name__ == '__main__':
    pytest.main()
