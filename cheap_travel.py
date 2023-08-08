n, m, a, b = list(map(int, input().split()))

total_individual_cost = n * a

special_tickets_needed = n // m
cost_using_special_tickets = special_tickets_needed * b

remaining_journeys = n % m

remaining_cost_individual = remaining_journeys * a

remaining_cost = min(remaining_cost_individual, b)

total_cost = cost_using_special_tickets + remaining_cost

print(min(total_individual_cost, total_cost))