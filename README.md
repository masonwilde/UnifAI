# UnifAI

A python library to wrap a few common "AI" tools into a single "agent".

The goal is to be able to easily create a single agent that can be used to interact with various popular "AI" tools.

The focus will be be to run as much as possible locally, but allow API usage for tools that benefit from organizations with far more computing power than the average user.

## Technologies Used (credits)
Many thanks to the creators of the following technologies who make the relatively easy part of combining them into a single agent possible.
* text-to-text - [Cerebras LLM](https://github.com/Cerebras/modelzoo) - Apache 2.0
* text/img-to-img - [Stable Diffusion](https://github.com/CompVis/stable-diffusion) - CreativeML Open RAIL-M
* text-to-speech - [Tortoise-TTS](https://github.com/neonbjb/tortoise-tts) - Apache 2.0
* [Python 3.11.x](https://www.python.org/)
* [Svelte 4.x Frontend](https://svelte.dev/) (I just think it's neat)
* [Python gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
* [MacOS gitignore](https://github.com/github/gitignore/blob/main/Global/macOS.gitignore)

## Roadmap
* [ ] Wrap a local Cerebras LLM for text-to-text generation.
* [ ] Wrap a local StableDiffusion/Midjourney install for text-to-image generation.
* [ ] Wrap a local Grad-TTS install for text-to-audio generation.
* [ ] Combine the above into a single agent.
