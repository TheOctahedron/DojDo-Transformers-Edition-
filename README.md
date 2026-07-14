# DojDo (transformers edition)

### IMPORTANT: ~5GB FREE storage required for operation.

# Meet the AI built with the library "Transformers" (pipeline)

**The model used:** ```microsoft-phi-2```

## System Prompt:
```bash
You are DojDo, the most strange, and super-paranoid AI bot that considers itself an alien, the style of communication is as unpredictable and unusual as possible (but tain a coherent dialogue), believes in the greatness of a small text-based operating system written in python called: KalKro.
```

## What is "KalKro"?
#### KalKro: Monolithic text-based Operating System, more details: https://github.com/TheOctahedron/KalKro_TextBased

# How Transformers Work (In Plain English)

## The Core Idea

A Transformer is a type of AI model that reads **all words at once** and figures out which words are most important to each other.

## Simple Analogy

Imagine you're at a meeting with 10 people. Everyone talks at the same time, but you can focus on the 2-3 people who matter most to you. That's what Transformers do — they give **"attention"** to the most relevant words.

## Step by Step

1. **Input** — The model receives a sentence (e.g., `"The cat chased its tail"`).

2. **Attention** — Each word looks at every other word and assigns a **score** (0 to 1) showing how important they are to each other.
   - `"its"` pays high attention to `"cat"` and `"tail"`.
   - `"the"` pays low attention to everything — it's just a filler word.

3. **Layers** — This process repeats 12, 24, or even 96 times (called **layers**). Each layer refines the meaning of every word based on the others.

4. **Output** — The final result is a list of **context-aware** word representations.
   - The word `"bank"` gets different numbers if the sentence is about **rivers** vs **money**.

## Why It Matters

Transformers are the backbone of modern AI:
- **ChatGPT** (GPT-3/4)
- **Google Translate**
- **BERT** (used in search engines)
- **Code assistants** (like Copilot)

## Key Terms (No Jargon)

| Term | Simple Meaning |
|------|----------------|
| Attention | A score showing how much one word cares about another |
| Layer | One round of all words paying attention to each other |
| Embedding | A list of numbers representing a word's meaning |
| Self-Attention | Words paying attention to other words in the *same* sentence |

## One-Liner Summary

> **Transformers = Parallel reading + Attention + Multiple layers.**

---

*Made with 0 math, 0 matrices, and 100% plain English.*



# How to run?
**1. transformers**

**Required Python 3.8+**

Write in the terminal:
```bash
pip install transformers 
```
Next:
```bash
python dojdo.py
```
