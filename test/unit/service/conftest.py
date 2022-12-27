from application.service.impl.message_service_impl import MessageServiceImpl
import pytest

@pytest.fixture(scope='function')
def mock_repository(mocker):
    return mocker.Mock()

@pytest.fixture(scope='function')
def message_service(mock_repository):
    service = MessageServiceImpl(mock_repository) 
    yield service

