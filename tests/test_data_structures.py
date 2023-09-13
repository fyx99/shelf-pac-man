
from optimizer.data_structures import Article, Node, OptimizationMode, OptimizationProblem, PartTier, Shelf



def test_node_equals():
    
    a = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])

    prob = OptimizationProblem(s1, a, 1, 99999999, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    
    node1a = Node(
        articles={a[0]: 1, a[1]: 1, a[2]: 1}
    )
    
    node1b = Node(
        articles={a[0]: 1, a[1]: 1, a[2]: 1}
    )
    
    node2 = Node(
        articles={a[0]: 7, a[1]: 8, a[2]: 9}
    )
    
    assert node1a.equals(node1b) == True
    assert node1b.equals(node1a) == True
    assert node1a.equals(node2) == False
    assert node1b.equals(node2) == False
    assert node2.equals(node1a) == False
    assert node2.equals(node1b) == False
    
    
if __name__ == "__main__":
    test_node_equals()