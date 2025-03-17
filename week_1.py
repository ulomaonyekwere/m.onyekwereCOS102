def simple_interest(principal, rate, time):
    
    amount = principal * (1 + (rate / 100) * time)
    return amount

def compound_interest(principal, rate, n, time):
  
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

def annuity_plan(payment, rate, n, time):
   
    r_n = rate / n
    amount = payment * (((1 + r_n) ** (n * time) - 1) / r_n)
    return amount


P = 900  
R = 5     
T = 4
n = 12    
PMT = 30


si_result = simple_interest(P, R, T)
ci_result = compound_interest(P, R/100, n, T)
annuity_result = annuity_plan(PMT, R/100, n, T)

print(f"Simple Interest Amount: {si_result:.2f}")
print(f"Compound Interest Amount: {ci_result:.2f}")
print(f"Annuity Plan Amount: {annuity_result:.2f}")
