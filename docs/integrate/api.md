---
sidebar_position: 2
---

# API

## Querying Knowledge Using the API

To interact with your trained knowledge base, you'll need to obtain an API key from the `Settings` menu:

![api_key](/img/embed/setting.png)



## Example Query: Experience Related to Data Platforms

To query the knowledge base, use the following JSON request body, where `"query": "Experience related to data platform."` represents the information you're seeking.



The request is made to `https://api.gptdevelopment.online/api/embeddings/train/query` using the `POST` method. Authentication is performed using a JWT token obtained from the `Settings` menu.



Here's an example CURL command for testing (remember to replace `${token}` with your actual API Key):

```
curl -X POST 'https://api.gptdevelopment.online/api/embeddings/train/query' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer ${token}' \
-d '{"query": "Experience related to data platform."}'

```



The response from the query should provide detailed information based on the trained data. For instance:

```
Through the development of a self-researched data integration framework and various 
data source extraction plugins, including Oracle, 
MySQL, PostgreSQL, MongoDB, HTTP, custom protocols, etc., 
achieved rapid data extraction and integration, 
signiﬁcantly improving the efﬁciency and stability of the data platfor
```



