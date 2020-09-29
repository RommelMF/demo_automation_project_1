__author__ = 'rmostafin'
import pytest

from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()

    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username='admin2@mail.ru', password='2', name='admin2')
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture