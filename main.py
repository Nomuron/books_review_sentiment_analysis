from modules import *


def main():
    for text in selenium_simulation():
        csv_writer(opinion_rating_compositor(text))


if __name__ == '__main__':
    main()
