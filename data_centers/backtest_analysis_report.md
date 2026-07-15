# Backtest Calibration Analysis Report: The Pre-Crisis Predictability Mismatch

This report analyzes the structural reasons why the Techno-Economic Systems Model (TESM) exhibits a fitting mismatch during the pre-crisis "run-up" bubble phase across historical backtests (e.g., DOTCOM, GFC, JAPAN).

---

## 🔍 Key Findings: Why the Model Underperforms Before the Crash

The systematic mismatch during the pre-crisis peak phase is driven by three primary architectural factors in macroeconomic system dynamics modeling:

### 1. Speculative Reflexivity vs. Fundamental Sentiment
In the model, investor sentiment and valuation multiples are driven by fundamental feedback loops:
$$\text{roicScore} \propto \text{ROIC} - \text{WACC}$$
$$\text{growthScore} \propto \text{YoY Growth} - 12\%$$
$$\text{Sentiment} = \min(\text{roicScore}, \text{growthScore})$$

*   **The Mismatch**: Real-world bubble run-ups (such as the Dot-com bubble or GFC credit expansion) are driven by **purely speculative momentum feedback loops** (speculative capital inflows driving prices up, which attracts more momentum capital, completely decoupled from underlying ROI).
*   **System Impact**: Because the model prevents multiples from expanding beyond the boundary cap set by actual ROIC and SaaS growth, it cannot replicate the extreme, irrational valuation spikes observed at the absolute peak of speculative bubbles.

### 2. Global RMSE Optimization Trade-offs
The calibration engine optimizes parameters globally by minimizing the Root Mean Squared Error (RMSE) over the entire timeline (typically 12–24 quarters):
$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^{N} (I_{\text{actual}, t} - I_{\text{simulated}, t})^2}$$

*   **The Mismatch**: The pre-crisis bubble run-up and peak represent a very short temporal window (typically the first 10-15% of the backtest). The post-crisis collapse, liquidation, and stagnation plateau represent the remaining 85% of the timeline.
*   **System Impact**: To minimize the overall mathematical error, the optimizer is forced to select parameters that fit the long-term stagnation plateau and recovery curves perfectly. This global compromise mathematically flattens the simulated pre-crisis peak because fitting the peak too aggressively would cause massive, unacceptable errors in the long-term stagnation phase.

### 3. Exogenous Shock Timing vs. Endogenous Mechanics
*   **The Mismatch**: Real-world crashes are triggered by exogenous policy or liquidity shocks (e.g., the Federal Reserve raising rates aggressively in 2000, the overnight freeze of the interbank lending market in 2007, or the sudden implementation of land value tax guidelines in Tokyo).
*   **System Impact**: The simulation models these thresholds endogenously (e.g., physical capacity constraints or contract renewals). Without injecting the exact historical calendar date of the exogenous monetary/liquidity shock, the simulated peak will naturally occur slightly earlier or later than the historical peak.

---

## 📈 Specific Case Analyses

### DOTCOM (Dot-com Bubble)
*   **Actual Path**: A vertical, exponential spike in valuation multiples (reaching >100x EV/Revenue for hot internet stocks) followed by a sudden, total collapse.
*   **Simulated Path**: A smoother, capped valuation curve. The simulation correctly identifies the structural unsustainability of building telecom capacity without enterprise adoption, but it models the build-up as a gradual capital deployment cycle rather than a manic stock market speculation.

### JAPAN (Asset Price Bubble)
*   **Actual Path**: A long, multi-year asset bubble followed by a 20-year structural stagnation.
*   **Simulated Path**: Starts at 100 and aligns closely with the post-bubble decay rate. The pre-crisis peak is flattened because the model's capital reflexivity factor must remain low ($\beta = 0.1$) to prevent the model from generating explosive hyper-growth during the subsequent 15 years of stagnation.

---

## 🛠️ Model Improvements to Capture Bubble Peaks

If the primary goal of the model is shifted toward predicting bubble peaks rather than long-term stagnation plateaus, the following equations should be introduced:

1.  **Introduce a Momentum Term to Multiple Expansion**:
    Allow multiples to expand based on the *first derivative* (acceleration) of index growth, representing speculative momentum:
    $$\text{Multiple}_{t} = \text{Multiple}_{t-1} \times \left(1 + \gamma \cdot \max(0, \Delta \text{Index}_{t-1})\right)$$
2.  **Split Calibration Weights (Weighted RMSE)**:
    Weight the pre-crisis quarters higher in the optimizer:
    $$\text{Weighted RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^{N} w_t \cdot (I_{\text{actual}, t} - I_{\text{simulated}, t})^2}$$
    where $w_t = 3.0$ for the peak quarters.
