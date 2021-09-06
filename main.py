from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681'
OPINION_CSS_SELECTOR = '.bv-content-summary-body-text:nth-child(1)'
RATE_CSS_SELECTOR = '.bv-rating-stars-container .bv-off-screen'


def opinion_rating_compositor(opinion_review: list, opinion_rate: list) -> dict:
    sentiment_rates = []

    for opinion in opinion_review:
        for rate in opinion_rate:
            if rate >= 4:
                sentiment_rates.append('positive')
            elif rate <= 2:
                sentiment_rates.append('negative')
            else:
                continue






def selenium_simulation():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    opinion_web_elements = driver.find_elements_by_css_selector(OPINION_CSS_SELECTOR)
    opinions = [opinion.text for opinion in opinion_web_elements]

    rates_web_elements = driver.find_elements_by_css_selector(RATE_CSS_SELECTOR)
    rates = [rate.text[0] for rate in rates_web_elements]

    for opinion in opinions:
        yield {opinion: rates}


def main():
    for text in selenium_simulation():
        print(text, '\n')


if __name__ == '__main__':
    main()
