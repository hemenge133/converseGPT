# converseGPT [DEPRECATED]
## With the launch of OpenAI's Custom GPTs, it doesn't make sense to put time into a wrapper around their APIs anymore.
## GPT-based chat app and infra-as-code backend to enable anybody to scale a customized chat app stably with no / minimal coding required.


## Features
- Extensibility: langchain provides a number of useful abstractions and integrations with other tools. ie. Chains, Agents, Memory.
    - The current configuration is meant to closely resemble chatGPT.
    - Uses langchain to call chatGPT by default, is easily extended to use other LLMs (see model integrations [here](https://python.langchain.com/docs/integrations/chat/))
- [WIP] Use a single config file to manage common model parameters and tools such as agent instructions and input embeddings.
- [WIP] Scalable AWS backend
    - [WIP] All components in autoscaling groups with containerized EC2 host images (AMIs) or something like terraform. 
    - CI/CD pipeline (GH actions) tracking last successful commit, auto rollback in case of test failures
    - WSGI server (gunicorn)
    - Cache for sessions (redis)
    - Proxy server (nginx)
 
## [Live Demo](https://conversegptapp.net/)
Note: As this is currently more of a WIP than a product, you must use your own OpenAI API key in the live demo.
  
![alt text](https://github.com/hemenge133/converseGPT/blob/main/imgs/ss_dark.png?raw=true)
![alt text](https://github.com/hemenge133/converseGPT/blob/main/imgs/ss_light.png?raw=true)
