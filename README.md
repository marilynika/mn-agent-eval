# Agent eval: type-blind tool looping

This repo is a custom Harbor evaluation exploring how different models handle strict API schemas.. it tests for a failure mode I call **Type-blind tool looping**.

## imagine this..
When a tool throws a formatting error (like requiring `YYYY-MM-DD` instead of "tomorrow"), what does the model do? 

A more resilient agent reads the error, adjusts its payload, and tries again but a susceptible agent ignores the feedback and just hits the API with the exact same bad payload until it times out.

## How the models did
* **Gemini 1.5 Pro:** Passed. It actually read the error message, calculated the correct date format using the environment context, and successfully called the tool on its second attempt.
* **Gemini 1.5 Flash:** Failed (Looped). It completely ignored the error text and blindly retried the exact same invalid payload until it hit the iteration limit.
