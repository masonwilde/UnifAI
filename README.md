# UnifAI

LICENSE PENDING: I need to figure out which license satisfies the requirements of the various libraries used. The intent is for this to be as open as possible, but I'm not a lawyer and I don't want to get sued.

A python library and webUI to wrap a few common "AI" tools into a single "agent".

The goal is to be able to easily create a single agent that can be used to interact with various popular "AI" tools. Customization will be limited to the configuration file and the webUI. If you're looking to fine tune models, feel free to submit a PR to add that functionality, but the initial goal is to make it as easy as possible to use these tools without much overhead.

The focus will be be to run as much as possible locally, but allow API usage for tools that benefit from organizations with far more computing power than the average user.

## Technologies Used (credits)
Many thanks to the creators of the following technologies who make the relatively easy part of combining them into a single agent possible.
* text-to-text - [GPT4all](https://github.com/nomic-ai/gpt4all) - MIT
* text/img-to-img - [Stable Diffusion](https://github.com/CompVis/stable-diffusion) - CreativeML Open RAIL-M
* text-to-speech - [Tortoise-TTS](https://github.com/neonbjb/tortoise-tts) - Apache 2.0
* [Python 3.11.x](https://www.python.org/)
* [Svelte 4.x Frontend](https://svelte.dev/) (I just think it's neat)
* [Python gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
* [MacOS gitignore](https://github.com/github/gitignore/blob/main/Global/macOS.gitignore)

# Install and Dependencies

* `pip install -r requirements.txt`
* Install LFS per your OS. 
* Download an LLM and direct to it in the config file. (I used mistral-7b-instruct-v0.1.Q4_0.gguf from https://gpt4all.io/index.html for testing)
* Clone a Stable Diffusion repo and direct to it in the config file. (trying to get this to work with just a safetensors file) (I used https://huggingface.co/runwayml/stable-diffusion-v1-5 for testing, but it's quite large)
  * You'll likely need to `git lfs install` and `git lfs pull` to get the safetensors file.

# Usage

* `python src/main.py`
* It should currently load the LLM and Stable Diffusion models and allow you to generate text from text or an image from text if you start your prompt with "img".

## Roadmap
* [x] Wrap a local Cerebras LLM for text-to-text generation.
* [ ] Wrap a local StableDiffusion/Midjourney install for text-to-image generation.
* [ ] Wrap a local Grad-TTS install for text-to-audio generation.
* [ ] Combine the above into a single agent.

## Learning Resources Used
