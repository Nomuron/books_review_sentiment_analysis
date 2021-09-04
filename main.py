from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def selenium_simulation():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.barnesandnoble.com/w/eye-of-the-world-robert-jordan/1100356869?ean=9781250768681')


def main():
    selenium_simulation()


if __name__ == '__main__':
    main()
