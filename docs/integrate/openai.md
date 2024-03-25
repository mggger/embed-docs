---
sidebar_position: 1
---

# OpenAI Custom GPTs Integration Guide

Elevate your service by integrating OpenAI Custom GPTs. Follow these steps for a seamless setup:

1. **Obtain an API Key** directly from the Embed service page settings.
2. **Configure OpenAI Custom Actions** using your newly acquired API Key.
3. **Enable GPTs to Utilize This Action**

## Obtaining an API Key

### Acquire an API Key from the Embed Service
Navigate to the Embed service sidebar to find the API Key. Click on `settings` to proceed.

<img src="/img/embed/settings.png" width="60%" alt="API Key Settings" />

### Configuring Your API Key in OpenAI GPTs Builder
Upon receiving your API Key, enter it into the OpenAI GPTs Builder Action. Select Bearer as the authentication method and paste your API Key as shown in the screenshot:

<img src="/img/embed/api_key.png" width="60%" alt="OpenAI API Key Configuration" />


## Configuring OpenAI Custom Actions

### Start by Setting Up in the Embed Service
Specify the action's name, description, and privacy policy, then save your settings.

<img src="/img/embed/action_create.png" width="60%" alt="Action Creation" />

After saving, click on `Integrate` to view the configuration details.

<img src="/img/embed/action_define.png" width="60%" alt="Action Define" />

### Transfer Configuration Details to OpenAI GPTs Builder
Copy both the **Scheme** and **Privacy Policy** details.

<img src="/img/embed/action_config.png" width="60%" alt="Action Configuration" />

## Enabling GPTs to Use This Action

Inform the GPTs of the newly created action name, allowing it to be invoked in specific contexts. For instance, if you've created an action named `getKnowledge`, instruct the GPTs in the Builder with the following prompt:

```
To answer user's questions you will search the right getKnowledge 
by calling the action 'getKnowledge'
```

***
<img src="/img/embed/gpt-example.png" width="60%" alt="Gpt Example" />