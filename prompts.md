# Prompt Iteration

## Initial Version

Write a short business summary based on the input. Keep it clear and professional.

---

## Revision 1

You are helping a financial analyst.

Write a concise business summary based only on the given input.

Try to:
- point out key performance signals (e.g., revenue changes)
- explain possible reasons for growth or decline
- mention any risks if relevant
- keep the tone professional and analytical

Avoid adding information that is not in the input.

---

## Revision 2

You are helping a financial analyst prepare a quick investment-style summary.

Write one short paragraph based only on the given input.

Focus on:
- the most important performance signals
- main drivers behind the change
- any potential risks or uncertainty

If the information is incomplete, say that clearly instead of guessing.  
Do not make up numbers or facts.

---

## What Changed and Why

In the first revision, I added more structure to guide the model (like focusing on performance, drivers, and risks), because the initial version was too general and sometimes produced vague summaries.

In the second revision, I made the instructions more specific and added constraints (like one paragraph and handling incomplete information). This was mainly to reduce hallucination and make the output more reliable.

---

## What Improved / Stayed the Same / Got Worse

After the revisions, the summaries became more focused and closer to what a financial analyst would actually write. The model was also less likely to add unsupported details.

However, the output became slightly shorter and less detailed, which shows a trade-off between clarity/accuracy and richness.
