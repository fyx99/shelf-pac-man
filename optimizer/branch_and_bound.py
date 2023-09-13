## branch and bound fundement 
from optimizer.bounds import greedy_lower_bound

from optimizer.data_structures import Node, OptimizationMode, OptimizationProblem
from optimizer.utils import add_article_dict

node_target_value_by_mode = {
    OptimizationMode.MAXIMIZE_COEFFICIENT_SUM: lambda node: sum([k.coefficient * v for k, v in node.articles.items()]),
    OptimizationMode.MAXIMIZE_MINIMUM_COEFFICIENT: lambda node: min([k.coefficient * v for k, v in node.articles.items()])
}

def branch_and_bound(optimization_problem: OptimizationProblem, max_loop_index=None):
    
    
    ### generate start node of optimization problem
    
    q = []    # queue for nodes to check
    start_node = Node(
        level=0,
        count_from_left=0,
        lower_bound=0,
        used_width=sum([min_num * article.width for min_num, article in zip(optimization_problem.minimum_articles, optimization_problem.articles)]),
        articles={article: min_num for min_num, article in zip(optimization_problem.minimum_articles, optimization_problem.articles)}
    )
    start_node.target_value = node_target_value_by_mode[optimization_problem.mode](start_node)
    
    
    
    q.append(start_node)
    
    best_node = start_node
    best_lower_bound = start_node.lower_bound
    perf_loop_index = 0
    perf_candidate_checked_count = 0
    perf_candidate_dismissed_count = 0
    perf_candidate_duplicate_count = 0
    perf_candidate_afterwards_dismissed_count = 0
    
    ### iteratively go through possible solutions
        
    while len(q):
        ## logging
        if perf_loop_index % 100 == 0:
            print(perf_loop_index, perf_candidate_checked_count, perf_candidate_dismissed_count, perf_candidate_duplicate_count, len(q), best_lower_bound)
            
        ### get next node in line
        current_node = q.pop()
        perf_candidate_checked_count += 1
        ### keep track of best node
        
        if current_node.lower_bound < best_lower_bound:
            perf_candidate_afterwards_dismissed_count += 1
            continue
        
        print("NODE START")



        if current_node.target_value > best_node.target_value: 
            best_node = current_node
    
        ### produce all the possible candidated beneth this node
        
            ### here we only produce ones that are greater or equal the highest found upper bound
            ### plus we make a duplicate check to prevent same nodes double
        
        
        for n, possible_additional_article in enumerate(optimization_problem.articles):
            
            ### check if it actually fits
            if current_node.used_width + possible_additional_article.width > optimization_problem.shelf.total_width:
                continue
            
            ### other way of checking duplicates validate later
            count_from_left = len(optimization_problem.articles) * current_node.count_from_left - (len(optimization_problem.articles) - n - 1)
            #if count_from_left % 3 == 0:
            #    continue # duploop_indexcate node
            # sollte nur hinzufügen wenn die node die option hat eine höhere profit bound zu haben
            
            candidate = Node(
                    level=current_node.level + 1,
                    count_from_left=count_from_left,
                    lower_bound=0,
                    used_width=current_node.used_width + possible_additional_article.width,
                    articles=add_article_dict(current_node.articles, possible_additional_article)
                )
            candidate.target_value = node_target_value_by_mode[optimization_problem.mode](candidate)

            #print(repr(candidate))
            candidate.lower_bound = greedy_lower_bound(candidate, optimization_problem)
            
            if candidate.lower_bound >= best_lower_bound:
                best_lower_bound = candidate.lower_bound
                ### das ist jetzt ein gewisses fragezeichen nehm ich jz ne extra var oder wie setz ich das
                for queued_candidate in q:
                    if queued_candidate.equals(candidate):
                        print("CANDIATE NODE DISCARDED DUE TO DUPLICATE")
                        perf_candidate_duplicate_count += 1
                        break
                else:
                    print(f"CANDIDATE FOUND {candidate.lower_bound}")
                    
                    q.append(candidate)
            else:
                #print(f"CANDIDATE TOO LOW LOWER BOUND {candidate.lower_bound} < {best_lower_bound}")
                perf_candidate_dismissed_count += 1


            
        ## logging and handling
        perf_loop_index += 1
        if max_loop_index and perf_loop_index > max_loop_index:
            print(f"STOPPED AT ITERATION {perf_loop_index} BECAUSE OF MAX_LOOP_INDEX")
            break
        
    # result is a node with the best chances
    return best_node
        
        