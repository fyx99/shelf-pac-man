import unittest

from optimizer.data_structures import Article, OptimizationProblem, OptimizationMode, OptimizationStatus, PartTier, Shelf

def basic_shelf_maximize_coefficient_sum():
    a1 = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])

    prob = OptimizationProblem(s1, a1, 1, 99999999, OptimizationMode.MAXIMIZE_COEFFICIENT_SUM)
    
    result = []
    
    assert result[0] == 1
    assert result[1] == 5
    assert result[2] == 1
    
    assert prob.status == OptimizationStatus.SOLVED

def basic_shelf_maximize_minimum_coefficient():
    a1 = [Article(width=2, coefficient=1), Article(width=1, coefficient=2), Article(width=3, coefficient=3)]
    s1 = Shelf(part_tiers=[PartTier(width=10)])

    prob = OptimizationProblem(s1, a1, 1, 99999999, OptimizationMode.MAXIMIZE_MINIMUM_COEFFICIENT)
    
    result = []
    
    assert result[0] == 3
    assert result[1] == 2
    assert result[2] == 1
    
    assert prob.status == OptimizationStatus.SOLVED
    
    
if __name__ == "__main__":
    basic_shelf_maximize_coefficient_sum()
    basic_shelf_maximize_minimum_coefficient()