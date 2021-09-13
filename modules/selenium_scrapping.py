from typing import Generator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681'
OPINION_CSS_SELECTOR = '.bv-content-summary-body-text:nth-child(1)'
RATE_CSS_SELECTOR = '.bv-rating-stars-container .bv-off-screen'


def selenium_simulation() -> Generator[dict, None, None]:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    opinion_web_elements = driver.find_elements_by_css_selector(OPINION_CSS_SELECTOR)
    opinions = [opinion.text.replace("\n", " ").replace("\"", "") for opinion in opinion_web_elements]

    rates_web_elements = driver.find_elements_by_css_selector(RATE_CSS_SELECTOR)
    rates = [rate.text[0] for rate in rates_web_elements]

    driver.find_element_by_css_selector('#onetrust-accept-btn-handler').click()
    driver.find_element_by_css_selector('span.bv-content-btn-pages-next').click()

    for opinion, rate in zip(opinions, rates):
        yield {opinion: int(rate)}
