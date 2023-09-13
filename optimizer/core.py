

from optimizer.branch_and_bound import branch_and_bound
from optimizer.data_structures import OptimizationProblem


def solve(optimization_problem: OptimizationProblem):
    
    branch_and_bound(optimization_problem.articles, sum([part_tier.width for part_tier in optimization_problem.shelf.part_tiers]), )