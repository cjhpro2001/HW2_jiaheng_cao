print("LLM business writing prototype")

import os
from pathlib import Path
from datetime import datetime

from google import genai

# -----------------------------
# Configurable prompt / settings
# -----------------------------
MODEL_NAME = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """
You are a business writing assistant for financial analysts.
Write a concise investment-style business summary based only on the provided input.
Do not invent facts. If the input is incomplete, say so clearly.
Focus on:
1. key business performance signals
2. main growth or decline drivers
3. risks or concerns
4. overall professional tone
Keep the output to one short paragraph.
""".strip()

DEFAULT_INPUT = """
A consumer electronics company reported that quarterly revenue increased by 18% year over year,
driven by strong smartphone sales in Asia and improved online marketing efficiency.
Operating margin improved from 12% to 15%.
However, management noted that component costs remain volatile.
""".strip()


def load_input() -> str:
    """
    Load input text from input.txt if it exists.
    Otherwise, use the built-in default example.
    """
    input_file = Path("input.txt")
    if input_file.exists():
        text = input_file.read_text(encoding="utf-8").strip()
        if text:
            return text
    return DEFAULT_INPUT


def build_prompt(user_input: str) -> str:
    return f"""
Task: Write an investment-style business summary.

Input:
{user_input}

Output requirements:
- Professional and concise
- No bullet points
- No made-up facts
- Mention uncertainty if information is incomplete
""".strip()


def generate_summary(user_input: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing GEMINI_API_KEY. Please set your API key in the environment first."
        )

    client = genai.Client(api_key=api_key)

    prompt = build_prompt(user_input)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
            "temperature": 0.3,
        },
    )

    return response.text.strip()


def save_output(user_input: str, summary: str) -> str:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"summary_{timestamp}.txt"

    content = f"""=== INPUT ===
{user_input}

=== GENERATED SUMMARY ===
{summary}
"""

    output_file.write_text(content, encoding="utf-8")
    return str(output_file)


def main():
    print("=== Investment Summary Prototype ===")

    user_input = load_input()
    print("\n[Input Loaded]\n")
    print(user_input)

    try:
        summary = generate_summary(user_input)
    except Exception as e:
        print("\n[Error]")
        print(e)
        return

    print("\n[Generated Summary]\n")
    print(summary)

    output_path = save_output(user_input, summary)
    print(f"\n[Saved to] {output_path}")


if __name__ == "__main__":
    main()