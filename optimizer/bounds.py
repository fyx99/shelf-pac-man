## based on the different optimization targets we use different bonds




def next_best_item_maximize(node, max_width):
    best_article = None
    for article in articles:
        if max_width > (node.used_width + article.width) and (not best_article or article.coefficient > best_article.coefficient):
            best_article = article
    return best_article    

def next_best_item_maximize_minimum(node, max_width):
    best_article_current_coefficient_sum = None
    best_article = None
    for article in articles:
        if max_width > (node.used_width + article.width) and (not best_article or node.articles_coefficient_sum.get(article, 0) < best_article_current_coefficient_sum):
            best_article = article
            best_article_current_coefficient_sum = node.articles_coefficient_sum.get(article, 0)
    return best_article


def greedy_bound(node, articles, max_width, type=None):
    

    current_node = node
    
    while True:#s nächste passt noch rein
        next_article = next_best_item_maximize_minimum(current_node, max_width)
        if not next_article:
            break
        current_node = Node(
            level=current_node.level + 1,
            count_from_left=0,
            lower_bound=0,
            upper_bound=current_node.sum_coefficient + next_article.coefficient,
            used_width=current_node.used_width + next_article.width,
            sum_coefficient=current_node.sum_coefficient + next_article.coefficient,
            articles=[*current_node.articles, next_article]
        )

    return current_node.upper_bound
        
        