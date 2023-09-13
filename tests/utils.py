import random

from optimizer.data_structures import Article

def generate_test_articles(seed):
    random.seed(seed)
    width = 20
    occupancy = 0.2
    average_width = 4
    width_std = 2
    sum_width_articles = 0
    articles = []
    while sum_width_articles < (width * occupancy):
        curr_width = max(1, round(random.gauss(average_width, width_std)))
        articles.append(Article(
            width=curr_width, 
            height=random.randint(1, 20)*10, 
            depth=random.randint(1, 20)*10, 
            coefficient=round(random.random() * 2000) / 20
        ))
        sum_width_articles += curr_width
    return articles        
        