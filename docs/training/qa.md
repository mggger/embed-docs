# Q&A


## Training Q&A with Embed

Embed allows for the straightforward training of routine questions and answers. Simply define the question and answer, and proceed to train directly.

![Embed-Intro](/img/embed/train_qa.png)

The label is used to filter the train records, it is optional.


## Batch Training for Q&A

For batch training of Q&A, you can opt for batch mode where the question corresponds to "description" and the answer to "text", as shown in the example below:


```json
[
  {"description":  "what's your name", "text": "Embed", "lebal":  "1"},
  {"description":  "Where are you", "text": "Online", "label":  "2"},
  ...
]

```
