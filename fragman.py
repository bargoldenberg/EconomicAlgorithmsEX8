INCREMRENT_BALANCE_AMOUNT = 0.08

# IMPLEMENTED BY: BAR GOLDENBERG

def choose_item(costs, new_costs, count_player, balances):
    amount_to_subtract = 0
    for item in new_costs:
        if new_costs[item] <= 0:
            print("After adding", INCREMRENT_BALANCE_AMOUNT, "to each citizen", item, "is chosen.")
            amount_to_subtract = costs[item] / count_player[item]
            for i in range(len(votes)):
                if item in votes[i]:
                    balances[i] -= amount_to_subtract
            break
    
def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    for i in range(len(balances)):
        balances[i] += INCREMRENT_BALANCE_AMOUNT
    new_costs = costs.copy()
    count_player = {}
    for i in range(len(votes)):
        for item in votes[i]:
            new_costs[item] -= balances[i]
            if item not in count_player:
                count_player[item] = 1
            else:
                count_player[item] += 1
    choose_item(costs, new_costs, count_player, balances)
    for i in range(len(balances)):
        print("Citizen", i+1, "has", balances[i], "remaining balance.")


votes = [{"Park in street X", "Fix road X"}, {"Park in street X"}]
balances = [1, 1]
costs = {"Park in street X": 2, "Fix road X": 3}

elect_next_budget_item(votes, balances, costs)
print('------------------------')
votes = [ {"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}]
balances = [1.5, 2.4, 3.3, 4.2, 5.1]
costs = {"Park": 1000, "Trees": 2000, "Lights": 3000}


elect_next_budget_item(votes, balances, costs)