      
from optimizer.bounds import greedy_lower_bound, next_best_item_maximize, next_best_item_maximize_minimum
from optimizer.data_structures import Article, Node, OptimizationMode, OptimizationProblem, PartTier, Shelf


def test_next_best_item_maximize():
    
    a = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])

    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    
    node = Node(
        lower_bound=1,
        used_width=6,
        articles={a[0]: 1, a[1]: 1, a[2]: 1}
    )
    
    next_article, next_article_lower_bound = next_best_item_maximize(node, prob)
    
    assert next_article == a[1]
    assert next_article_lower_bound == 9
    
        
def test_next_best_item_maximize_minimum():
    
    a = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])

    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    
    node = Node(
        lower_bound=1,
        used_width=6,
        articles={a[0]: 1, a[1]: 1, a[2]: 1}
    )
    
    next_article, next_article_lower_bound = next_best_item_maximize_minimum(node, prob)
    
    assert next_article == a[0]
    assert next_article_lower_bound == 2
    
        
def test_greedy_lower_bound():
    
    a = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=20)])
    
    node = Node(
        lower_bound=1,
        used_width=6,
        articles={a[0]: 1, a[1]: 1, a[2]: 1}
    )
    
    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    node_lower_bound = greedy_lower_bound(node, prob)
    
    assert node_lower_bound == 35
    
    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_MINIMUM_COEFFICIENT)
    node_lower_bound = greedy_lower_bound(node, prob)
    
    assert node_lower_bound == 5
    
if __name__ == "__main__":
    test_next_best_item_maximize()   
    test_next_best_item_maximize_minimum()       
    test_greedy_lower_bound()
