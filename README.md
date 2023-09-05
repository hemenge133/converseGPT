# converseGPT [In Development]
## GPT-based chat app and infra-as-code backend to enable anybody to scale a customized chat app stably with no / minimal coding required.


## Features
- [WIP] Use a single config file to manage common model parameters and tools such as temperature or storing input embeddings.
- [WIP] Scalable AWS backend (nginx, gunicorn, redis cache for sessions)
- Uses langchain to call chatGPT by default, is easily extended to use other LLMs (see model integrations [here](https://python.langchain.com/docs/integrations/chat/))
- Extensibility: langchain provides a number of useful abstractions and integrations with other tools. ie. Chains, Agents, Memory.
  - The current configuration is meant to closely resemble chatGPT.
 
## [Live Demo](http://13.59.92.214/)
Note: As this is currently more of a WIP than a product, you must use your own OpenAI API key in the live demo. 
  
![alt text](https://github.com/hemenge133/converseGPT/blob/main/imgs/ss_dark.png?raw=true)
![alt text](https://github.com/hemenge133/converseGPT/blob/main/imgs/ss_light.png?raw=true)
