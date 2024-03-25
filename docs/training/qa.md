# Q&A


## Training Q&A with Embed

Embed allows for the straightforward training of routine questions and answers. Simply define the question and answer, and proceed to train directly.

![Embed-Intro](/img/embed/train_qa.png)

Please be aware of certain limitations with Embed. Since data is stored using 768-dimensional vectors, it's advisable to keep both questions and answers under 768 characters, with a current limit set at 600 characters.


## Batch Training for Q&A

For batch training of Q&A, you can opt for batch mode where the question corresponds to "description" and the answer to "text", as shown in the example below:


```json
[
  {"description":  "what's your name", "text": "Embed"},
  {"description":  "Where are you", "text": "Online"},
  ...
]

```
