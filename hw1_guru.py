from selene import browser, be, have
import time

def test_google_positive():
        #Тест поиска гугл
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
        browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
        browser.quit()


def test_google_negative():
        #Негативный Тест поиска !!!!!гугл
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('qwrqt12541trqwtq').press_enter()
        browser.element('.card-section').should(have.text('По запросу qwrqt12541trqwtq ничего не найдено.'))
        browser.quit()


def test_yandex():
        #Тест поиск yandex111
        browser.open('https://ya.ru ')
        time.sleep(25)
        browser.element('[placeholder="Найдётся всё"]').should(be.blank).type('Погода').press_enter()
        browser.element('.weather-forecast__organic').should(have.text('По часам'))
        browser.quit()


def test_duck():
        #Тест поиск duck
        browser.open(' https://duckduckgo.com')
        browser.element('[name="q"]').should(be.blank).type('Тестирование').press_enter()
        browser.element('[rel="noopener"]').should(have.text('Тестирование программного обеспечения'))
        browser.quit()
