## data structures to model business problem

from enum import Enum
from typing import Dict, List


class PartTier:
    def __init__(self, width=1, height=1, depth=1):
        self.width = width
        self.height = height
        self.depth = depth
        
    def __str__(self):
        return f"PartTier(w={self.width}, h={self.height}, d={self.depth})"
        
class Shelf:
    def __init__(self, part_tiers: List[PartTier]):
        self.part_tiers = part_tiers
        
    
    @property
    def total_width(self):
        return sum([pt.width for pt in self.part_tiers])
    
    @property
    def depth_at(self, at):
        pass
    
    @property
    def height_at(self, at):
        pass
        
    def __repr__(self):
        return "Shelf(" + ", ".join(list(map(str, self.part_tiers))) + ")"


class Article:
    def __init__(self, width=1, height=1, depth=1, coefficient=1):
        self.width = width
        self.height = height
        self.depth = depth
        self.coefficient = coefficient
    
    def __repr__(self):
        return f"Article(w={self.width}, h={self.height}, d={self.depth}, c={self.coefficient})"
        
class OptimizationMode(Enum):
    MAXIMIZE_MINIMUM_COEFFICIENT = 1
    MAXIMIZE_COEFFICIENT_SUM = 2
    
class OptimizationStatus(Enum):
    SOLVED = 1
    INFEASIBLE = 2
    UNSOLVED = 3

class OptimizationProblem:
    def __init__(self, shelf: Shelf, articles: List[Article], minimum_articles=1, maximum_articles=None, mode: OptimizationMode=None, result=None):
        self.shelf = shelf
        self.articles = articles
        self.minimum_articles = minimum_articles if isinstance(minimum_articles, list) else [minimum_articles] * len(articles)
        self.maximum_articles = maximum_articles if isinstance(maximum_articles, list) else [maximum_articles] * len(articles)
        self.mode = mode
        self.result = result
        self.status = OptimizationStatus.UNSOLVED
        
    def check_feasibility():
        pass
        
class Node:
    def __init__(self, level=0, count_from_left=0, lower_bound=None, used_width=None, target_value=0, articles=None):
        self.level = level
        self.count_from_left = count_from_left
        self.lower_bound = lower_bound
        self.used_width = used_width
        self.target_value = target_value
        self.articles:Dict[Article, int] = articles    # this is a array with the count of the articles

    
    def equals(self, other):
        if len(self.articles) != len(other.articles):
            return False
        for s, o in zip(list(self.articles.values()), list(other.articles.values())):
            if s != o:
                return False
        return True
        
    def __repr__(self):
        return f"Node(w={self.used_width}, target={self.target_value}, articles={self.articles})"
        