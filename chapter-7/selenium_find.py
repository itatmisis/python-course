# quickstart для Селениума
import time

from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def find_wait(  # noqa: C901, CCR001
    browser,  # noqa: ANN001
    what: str,
    how=By.CSS_SELECTOR,  # noqa: ANN001
    wait_time: int = 4,
    amount: int = 1,
    no_error: bool = True,
):  # noqa: ANN201
    """
    Получает безопасно елемент страницы
    :return: web-element
    :param browser: web-browser
    :param what: css-selector
    :param wait_time: amount of time to wait until error in seconds
    :param amount: amount of element to get. -1 to all with one try
    :param no_error: if True will return None on timeout error, otherwise raise TimeoutException
    """
    if amount == 1:
        # Искать только 1
        if no_error:
            try:
                to_return = WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((how, what)))
            except exceptions.TimeoutException:
                return None
            else:
                return to_return
        else:
            return WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((how, what)))
    if amount == -1:
        # Искать все
        if no_error:
            try:
                to_return = WebDriverWait(browser, wait_time).until(EC.presence_of_all_elements_located((how, what)))
            except exceptions.TimeoutException:
                return None
            else:
                return to_return
        else:
            return WebDriverWait(browser, wait_time).until(EC.presence_of_all_elements_located((how, what)))
    else:  # Не оптимизовано, исправить потом
        # Искать конкретное количество, на выходе может быть найденно больше, будут возвращенны все
        if no_error:
            try:
                array_to_return = WebDriverWait(browser, wait_time).until(
                    EC.presence_of_all_elements_located((how, what))
                )
            except exceptions.TimeoutException:
                return None
            else:
                sleeped = 0
                while len(array_to_return) < amount and (sleeped > wait_time):
                    array_to_return = WebDriverWait(browser, wait_time).until(
                        EC.presence_of_all_elements_located((how, what))
                    )
                    time.sleep(0.5)
                    sleeped += 0.5
                return array_to_return
        else:
            array_to_return = WebDriverWait(browser, wait_time).until(EC.presence_of_all_elements_located((how, what)))
            sleeped = 0
            while len(array_to_return) < amount and (sleeped > wait_time):
                array_to_return = WebDriverWait(browser, wait_time).until(
                    EC.presence_of_all_elements_located((how, what))
                )
                time.sleep(0.5)
                sleeped += 0.5
            return array_to_return
