
      
from optimizer.branch_and_bound import branch_and_bound
from optimizer.data_structures import Article, OptimizationMode, OptimizationProblem, PartTier, Shelf


def test_branch_and_bound():
    
    a = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])
    
    
    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    best_node = branch_and_bound(prob)
    
    assert list(best_node.articles.values())[1] == 4
    
    prob = OptimizationProblem(s1, a, 1, None, OptimizationMode.MAXIMIZE_MINIMUM_COEFFICIENT)
    best_node = branch_and_bound(prob)
    
    assert list(best_node.articles.values()) == [2, 2, 1]
    
if __name__ == "__main__":
    test_branch_and_bound()