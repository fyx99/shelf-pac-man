## data structures to model business problem

from enum import Enum
from typing import List


class PartTier:
    def __init__(self, width=1, height=1, depth=1):
        self.width = width
        self.height = height
        self.depth = depth
        
    def __str__(self):
        return f"PartTier(w={self.width}, h={self.height}, d={self.depth})"
        
class Shelf:
    def __init__(self, part_tiers):
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
    def __init__(self, shelf: Shelf, articles: List[Article], minimum_articles=1, maximum_articles=None, mode: OptimizationMode=None):
        self.shelf = shelf
        self.articles = articles
        self.minimum_articles = minimum_articles if isinstance(minimum_articles, list) else [minimum_articles] * len(articles)
        self.maximum_articles = maximum_articles if isinstance(maximum_articles, list) else [maximum_articles] * len(articles)
        self.mode = mode
        self.status = OptimizationStatus.UNSOLVED
        
    def check_feasibility():
        pass
        
class Node:
    def __init__(self, level, count_from_left, lower_bound, upper_bound, used_width, target_value, articles):
        self.level = level
        self.count_from_left = count_from_left
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.used_width = used_width
        self.target_value = target_value
        self.articles = articles
        self._articles_coefficient_sum = None
        
    @property
    def articles_coefficient_sum(self):
        if not self._articles_coefficient_sum:
            ed = {article: 0 for article in self.articles}
            for article in self.articles:
                ed[article] += article.coefficient
            self._articles_coefficient_sum = ed
        return self._articles_coefficient_sum
            
    def __repr__(self):
        return f"Node(w={self.used_width}, target={self.target_value}, articles={self.articles})"
        