from application.repository.impl.sqlalchemy_message_repository import SQLAlchemyMessageRepository
import pytest

@pytest.fixture(scope='function')
def mock_sqlalchemy(mocker):
    return mocker.Mock()

@pytest.fixture(scope='function')
def message_repo(mock_sqlalchemy):
    repo = SQLAlchemyMessageRepository(mock_sqlalchemy)
    yield repo

