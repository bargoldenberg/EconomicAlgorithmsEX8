INCREMRENT_BALANCE_AMOUNT = 0.08

# IMPLEMENTED BY: BAR GOLDENBERG

def choose_item(costs, new_costs, vote_sum, balances):
    amount_to_subtract = 0
    for item in new_costs:
        if new_costs[item] <= 0:
            print("After adding", INCREMRENT_BALANCE_AMOUNT, "to each citizen", item, "is chosen.")
            amount_to_subtract = costs[item] / vote_sum[item]
            for i in range(len(votes)):
                if item in votes[i]:
                    if balances[i] < amount_to_subtract:
                        balances[i] = 0
                        amount_to_subtract += (amount_to_subtract - balances[i])
                    else:
                        balances[i] -= amount_to_subtract
            return True
    return False

def increment_balances(balances):
    for i in range(len(balances)):
            balances[i] += INCREMRENT_BALANCE_AMOUNT

def print_balances(balances):
        for i in range(len(balances)):
            print("Citizen", i+1, "has", balances[i], "remaining balance.")
    
def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    found_item = False
    while not found_item:
        new_costs = costs.copy() 
        vote_sum = {}
        increment_balances(balances)
        for i in range(len(votes)):
            for item in votes[i]:
                new_costs[item] -= balances[i]
                vote_sum[item] = 1 if item not in vote_sum else vote_sum[item] + 1
        found_item = choose_item(costs, new_costs, vote_sum, balances)
        print_balances(balances)


votes = [{"Park in street X", "Fix road X"}, {"Park in street X"}]
balances = [1, 1]
costs = {"Park in street X": 2, "Fix road X": 3}

elect_next_budget_item(votes, balances, costs)
print('------------------------')
votes = [ {"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}]
balances = [1.5, 2.4, 3.3, 4.2, 5.1]
costs = {"Park": 1000, "Trees": 2000, "Lights": 3000}


elect_next_budget_item(votes, balances, costs)