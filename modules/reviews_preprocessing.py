def opinion_rating_compositor(opinion_rating_dict: dict) -> None:

    for opinion, rating in opinion_rating_dict.items():
        if rating >= 4:
            opinion_rating_dict[opinion] = 'positive'
        elif rating <= 2:
            opinion_rating_dict[opinion] = 'negative'
        else:
            continue

    print(opinion_rating_dict)