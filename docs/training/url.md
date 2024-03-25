---
sidebar_position: 2
---

# URL

## Train URL (Experimental Feature)

Utilize the built-in browser render technology, Embed, to train your knowledge base with web pages. When you want to include web pages in your knowledge base, you can train it as follows:


- ``Description:`` Enter a description of the webpage. This description is used to match user queries.
- ``URL:``, The webpage URL that needs to be trained.


### Batch Train
For training multiple webpages simultaneously, you can organize them in a JSON format as shown below:

```json
[
  {"description":  "Embed Website", "url": "https://gptdevelopment.online"},
  {"description":  "Embed Docs Website", "url": "https://docs.gptdevelopment.online"},
  ...
]

```