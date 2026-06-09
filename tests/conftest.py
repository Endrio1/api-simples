import pytest

from main import criar_app, items


@pytest.fixture
def client():
    app = criar_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            items.clear()
            yield client
            items.clear()
