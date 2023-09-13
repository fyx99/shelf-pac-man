import random
from typing import Dict

from optimizer.data_structures import Article

def generate_test_articles(seed, width=20, occupancy=0.2, average_width=4, width_std=2):
    random.seed(seed)
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
        
        
def add_article_dict(article_dict: Dict[Article, int], article: Article):
    return_dict = article_dict.copy()
    return_dict[article] += 1
    return return_dict


def test_add_article_dict():
    a1 = Article(coefficient=1, width=3)
    a2 = Article(coefficient=4, width=1)
    article_dict = {a1: 2, a2: 6}
    return_dict = add_article_dict(article_dict, a2)
    
    assert return_dict[a2] == 7

if __name__ == "__main__":
    test_add_article_dict()