## branch and bound fundement 

from queue import Queue

from optimizer.data_structures import Node, OptimizationProblem


def check_if_next_article_fits_on_shelf():
    

def process_node(optimization_problem, best_node, current_node):
    
    if current_node.sum_coefficient > best_node.sum_coefficient:
        best_node = current_node
    
    
    for n, possible_additional_article in enumerate(optimization_problem.articles):
        if current_node.used_width + possible_additional_article.width > optimization_problem.shelf.total_width:
            continue
        count_from_left = len(optimization_problem.articles) * current_node.count_from_left - (len(optimization_problem.articles) - n - 1)
        #if count_from_left % 3 == 0:
        #    continue # duploop_indexcate node
        # sollte nur hinzufügen wenn die node die option hat eine höhere profit bound zu haben
        
        candidate = Node(
                level=current_node.level + 1,
                count_from_left=count_from_left,
                lower_bound=0,
                upper_bound=0,
                used_width=current_node.used_width + possible_additional_article.width,
                sum_coefficient=current_node.sum_coefficient + possible_additional_article.coefficient,
                articles=[*current_node.articles, possible_additional_article]
            )
        #print(repr(candidate))
        candidate.upper_bound = greedy_bound(candidate, optimization_problem.articles, max_width)
        
        if candidate.upper_bound >= best_upper_bound:
            best_upper_bound = candidate.upper_bound
            print(f"Candidate {candidate.upper_bound} put")
            return candidate
        else:
            print(f"Candidate {candidate.upper_bound}")
            return None



def branch_and_bound(optimization_problem: OptimizationProblem, max_loop_index=None):
    
    q = Queue()    # queue for nodes to check
    start_node = Node(0, 0, 0, 0, 0, 0, optimization_problem.minimum_articles)   # most empty node without any articles
    q.put(start_node)
    
    best_node = start_node
    loop_index = 0
        
    while not q.empty():
        ## logging
        if loop_index % 10000 == 0:
            print(loop_index, best_node.sum_coefficient, q.qsize())
            
        current_node = q.get()
        candidate = process_node(optimization_problem, best_node, current_node)
        if candidate:
            q.put(candidate)
            
        ## logging
        loop_index += 1
        
        if max_loop_index and loop_index > max_loop_index:
            break
        
    # result is a node with the best chances
    return best_node
        
        
