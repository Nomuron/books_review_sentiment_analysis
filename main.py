from typing import Generator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681'
OPINION_CSS_SELECTOR = '.bv-content-summary-body-text:nth-child(1)'
RATE_CSS_SELECTOR = '.bv-rating-stars-container .bv-off-screen'


def opinion_rating_compositor(opinion_rating_dict: dict) -> None:

    for opinion, rating in opinion_rating_dict.items():
        if rating >= 4:
            opinion_rating_dict[opinion] = 'positive'
        elif rating <= 2:
            opinion_rating_dict[opinion] = 'negative'
        else:
            continue

    print(opinion_rating_dict)


def selenium_simulation() -> Generator[dict, None, None]:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    opinion_web_elements = driver.find_elements_by_css_selector(OPINION_CSS_SELECTOR)
    opinions = [opinion.text for opinion in opinion_web_elements]

    rates_web_elements = driver.find_elements_by_css_selector(RATE_CSS_SELECTOR)
    rates = [rate.text[0] for rate in rates_web_elements]

    for opinion, rate in zip(opinions, rates):
        yield {opinion: int(rate)}


def main():
    for text in selenium_simulation():
        opinion_rating_compositor(text)


if __name__ == '__main__':
    main()
