## based on the different optimization targets we use different bonds
from optimizer.data_structures import Node, OptimizationMode, OptimizationProblem
from optimizer.utils import add_article_dict


def next_best_item_maximize(node: Node, optimization_problem: OptimizationProblem):
    best_article = None
    best_article_factor = None
    for next_article in optimization_problem.articles:
        ### here we should of course check if the maximum number of articles allows this
        if optimization_problem.shelf.total_width < (node.used_width + next_article.width):
            ### not possible to fit
            continue
        greedy_bound_coefficient_factor = next_article.coefficient / next_article.width
        if not best_article or greedy_bound_coefficient_factor > best_article_factor:
            best_article = next_article
            best_article_factor = greedy_bound_coefficient_factor
    return best_article, sum([k.coefficient * v for k, v in node.articles.items()]) + next_article.coefficient


def next_best_item_maximize_minimum(node: Node, optimization_problem: OptimizationProblem):
    best_article = None
    best_article_factor = None
    best_lower_bound = None
    for next_article in optimization_problem.articles:
        ### here we should of course check if the maximum number of articles allows this
        if optimization_problem.shelf.total_width < (node.used_width + next_article.width):
            ### not possible to fit
            continue
        current_articles = node.articles
        next_articles = add_article_dict(current_articles, next_article)

        current_coefficient_product_min = min([k.coefficient * v for k, v in current_articles.items()])
        next_coefficient_product_min = min([k.coefficient * v for k, v in next_articles.items()])
        coefficient_product_min_increase_width_factor = (next_coefficient_product_min - current_coefficient_product_min) /  next_article.width
        greedy_bound_coefficient_factor = coefficient_product_min_increase_width_factor
        if not best_article or greedy_bound_coefficient_factor > best_article_factor:
            best_article = next_article
            best_article_factor = greedy_bound_coefficient_factor
            best_lower_bound = next_coefficient_product_min
    return best_article, best_lower_bound


next_item_by_mode = {
    OptimizationMode.MAXIMIZE_COEFFICIENT_SUM: next_best_item_maximize,
    OptimizationMode.MAXIMIZE_MINIMUM_COEFFICIENT: next_best_item_maximize_minimum
}
    

def greedy_lower_bound(node: Node, optimization_problem: OptimizationProblem):
    

    current_node = node
    
    while True:#s nächste passt noch rein
        next_article, next_article_lower_bound = next_item_by_mode[optimization_problem.mode](current_node, optimization_problem)
        if not next_article:
            break
        current_node = Node(
            level=current_node.level + 1,
            count_from_left=0,
            lower_bound=next_article_lower_bound,
            used_width=current_node.used_width + next_article.width,
            articles=add_article_dict(current_node.articles, next_article)
        )

    return current_node.lower_bound
        
        