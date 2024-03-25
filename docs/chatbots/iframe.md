---
sidebar_position: 2
---

# IFrame

## Share Your Chatbots

<img src="/img/embed/iframe-settings.png" width="80%" alt="Iframe Settings" />

In the chatbot settings, click `Generate Iframe Address` to get an iframe URL that can be easily integrated into any official website.


**Be cautious when sharing the iframe URL. Anyone with access to this address can integrate your chatbot into their site.**


Here's an example. Remember to replace the iframe address:


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Iframe</title>
    <!-- import Tailwind CSS -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex justify-center items-center h-screen">
<div class="w-full max-w-4xl h-full">
        <div class="w-full h-96">
            <iframe src="http://xxx" style="width: 100%; height: 100%; border: none;"></iframe>
        </div>
</div>
</body>
</html>
```
