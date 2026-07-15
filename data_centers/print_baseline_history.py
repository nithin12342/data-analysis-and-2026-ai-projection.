from tesm_simulation import run_simulation

sim = run_simulation()

print("Baseline History (Every 10 Quarters):")
print(f"{'Qtr':<5} | {'Index':<8} | {'Revenue':<8} | {'Sentiment':<10} | {'Multiple':<8} | {'ROIC':<6}")
print("-" * 55)

for t in range(0, 80, 10):
    print(f"{t:<5} | {sim['indexVal'][t]:<8.1f} | {sim['cloudRevenue'][t]:<8.1f} | {sim['investorSentiment'][t]:<10.2f} | {sim['multipleSales'][t]:<8.1f} | {sim['roic'][t]*100:<5.1f}%")
