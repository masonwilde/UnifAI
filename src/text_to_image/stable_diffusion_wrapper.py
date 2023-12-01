import os
import torch
from diffusers import StableDiffusionPipeline


class TTI:
    def __init__(self, config):
        print(os.getcwd())
        self.config = config
        print(os.path.abspath(config.sd_model))
        # TODO: Figure out why this can't jsut use a .safetensors file.
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            config.sd_model,
            use_safetensors=True,
        )
        # Apple Silicon Specific
        # TODO: Make this work on non-Apple Silicon and detect best option.
        self.pipeline = self.pipeline.to("mps")

    def prompt(self, prompt):
        return self.pipeline(prompt).images[0]
