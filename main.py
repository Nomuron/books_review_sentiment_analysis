from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def selenium_simulation():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681')
    opinion_parent = driver.find_elements_by_css_selector('.bv-content-summary-body-text p')
    opinions = [opinion.text for opinion in opinion_parent]
    # opinions = [opinion.find_element_by_tag_name("p").text for opinion in opinion_parent]
    yield opinions


def main():
    for text in selenium_simulation():
        print(text)


if __name__ == '__main__':
    main()
