from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681'


def selenium_simulation():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    opinion_parent = driver.find_elements_by_css_selector('.bv-content-summary-body-text:nth-child(1)')
    opinions = [opinion.text for opinion in opinion_parent]

    for opinion in opinions:
        yield opinion


def main():
    for text in selenium_simulation():
        print(text, '\n')


if __name__ == '__main__':
    main()
