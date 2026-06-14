import pytest
import sys
import os

# Garantir que a raiz do projeto esteja no PYTHONPATH quando pytest é executado
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root not in sys.path:
    sys.path.insert(0, root)

from main import criar_app, items


@pytest.fixture
def client():
    app = criar_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            items.clear()
            yield client
            items.clear()
