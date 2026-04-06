# LLM Business Writing Prototype Report

## 1. Business Use Case

The workflow I chose is generating short business summaries for financial analysis. In practice, analysts often need to quickly turn raw notes or brief descriptions into structured summaries for internal communication or investment discussion.

This task relies heavily on written communication and is repetitive, making it a good candidate for partial automation using an LLM.

---

## 2. Model Choice

I used the Gemini 2.5 Flash model because it provides fast responses and is sufficient for short-form business writing tasks.

I did not extensively test other models, but this model was adequate for generating concise summaries with reasonable quality and speed. Since the task is not highly technical or domain-specific, a lightweight model is appropriate.

---

## 3. Baseline vs. Final Design

In the initial version of the prompt, the instruction was very general (“write a business summary”), which often led to vague and generic outputs. The model sometimes failed to highlight key performance signals or provide meaningful structure.

After prompt iteration, I introduced more specific guidance:
- focusing on performance signals, drivers, and risks  
- restricting the output to one short paragraph  
- explicitly preventing the model from inventing information  
- requiring the model to acknowledge incomplete inputs  

As a result, the final outputs became more structured, more relevant to financial analysis, and less likely to include unsupported claims. The summaries better resembled what an analyst might actually write.

---

## 4. Limitations and Failure Cases

The prototype still has limitations. When the input is too short or lacks important context, the model may produce overly generic summaries or fail to provide meaningful insights.

In some cases, even with constraints, the model may still imply relationships (e.g., causes of growth) that are not clearly supported by the input. This means human review is still necessary, especially for high-stakes use cases like investment decisions.

---

## 5. Deployment Recommendation

I would recommend deploying this workflow as a support tool rather than a fully automated system.

It can be useful for:
- generating first drafts of summaries  
- improving efficiency in routine reporting tasks  

However, it should always be paired with human review, particularly to verify factual accuracy and ensure that no unsupported conclusions are included.

With proper oversight, this system can improve productivity without introducing significant risk.