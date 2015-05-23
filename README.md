# Notebook
## A dialogue system with empathy

### Rationale of empathy dialogue

- Real world: we need to listen more and speak less
- Empathy dialogue: much input, few output

### Technique

- Empathy Graph
As take turn continues, we have a set of rules to update graph G = (N, E)
* N: utterance, with POS tagging
* E: empathy edge (acknowledgements), rules of transitiions based on response of the
  audience, five main methods

* Can we build a Hidden Markov Model for Empathy Graph?
  - Sentimental Hidden Markov Model?

### Checklist

- Scenarios

TODO: what are different types of responses to a dialogue?

Rudimentary response:
-----------------------
Audience: "I feel X"
Tom Ridder: "That's interesting.. What makes you feel X?"

Audience: "I want to do X"
Tom Riddler: "That sounds interesting.. But I want to ask - Why do you want to do X?" | "How much do you want to do X?"

Audience: "I love X"
Tom Ridder: "Why do you love X?"

Audience: "My Mom passed away last week."
Tom Ridder: "I am so sorry to hear that. Do you mind sharing more with me?"

