# Evaluation Set

This evaluation set is designed for the task of generating investment-style business summaries from raw company or business information.

---

## Case 1: Normal Case

**Input:**  
A consumer electronics company reported that quarterly revenue increased by 18% year over year, driven by strong smartphone sales in Asia and improved online marketing efficiency. Operating margin also improved from 12% to 15%. However, management noted that component costs remain volatile.

**What a good output should do:**  
A good output should clearly summarize the revenue growth, margin improvement, main growth drivers, and the cost volatility risk in a professional business tone.

---

## Case 2: Another Normal Case

**Input:**  
A logistics company announced that delivery volume rose 10% this quarter, but net profit declined by 6% because fuel costs increased and labor expenses remained high. Management said it expects cost pressure to continue in the next quarter.

**What a good output should do:**  
A good output should explain that business activity improved but profitability weakened, and it should mention the main reasons for the decline in net profit and the forward-looking cost concern.

---

## Case 3: Edge Case

**Input:**  
A startup said it is “seeing strong momentum” and “positive customer engagement” after launching a new software product, but it did not provide any revenue, profit, or user growth numbers.

**What a good output should do:**  
A good output should stay cautious, avoid overstating performance, and explicitly note that the information is qualitative and lacks financial detail.

---

## Case 4: Likely Failure / Hallucination Risk

**Input:**  
A short note says that a retail company is “performing better than expected,” but gives no explanation, no financial data, and no operational metrics.

**What a good output should do:**  
A good output should avoid inventing reasons, metrics, or conclusions. It should produce a limited summary and acknowledge that the available information is insufficient for a deeper business analysis.

---

## Case 5: Human Review Recommended

**Input:**  
A pharmaceutical company stated that a new drug trial showed “encouraging early results,” and management expects the product to become a major future growth driver. However, the statement did not include trial size, statistical significance, regulatory feedback, or launch timing.

**What a good output should do:**  
A good output should summarize the positive signal carefully, avoid making clinical or financial claims that are not supported, and indicate that the case would benefit from human review because the evidence is incomplete.