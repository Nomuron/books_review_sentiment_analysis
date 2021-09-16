import csv
import os.path


CSV_FILE_DIRECTORY = './data/reviews.csv'


def opinion_rating_compositor(opinion_rating_dict: dict) -> dict:

    for opinion, rating in opinion_rating_dict.items():
        if rating >= 4:
            opinion_rating_dict[opinion] = 'positive'
        elif rating <= 2:
            opinion_rating_dict[opinion] = 'negative'
        else:
            continue

    return opinion_rating_dict


def file_checker() -> bool:
    if os.path.isfile(CSV_FILE_DIRECTORY):
        return True
    else:
        return False


def csv_writer(review: dict) -> None:
    is_file = file_checker()
    with open(CSV_FILE_DIRECTORY, 'a+') as review_data_csv:
        csv_review_writer = csv.writer(review_data_csv, delimiter=';')
        if not is_file:
            csv_review_writer.writerow(['Opinion', 'Rating'])

        csv_review_writer.writerow(*review.items())
