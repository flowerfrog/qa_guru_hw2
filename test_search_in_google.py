import pytest
from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_google_should_not_find_result():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('FJE^hds&&Q#^e888190<>').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
