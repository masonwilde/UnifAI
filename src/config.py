# Configuration file for UnifAI


class Config:
    """The configuration class for UnifAI."""

    def __init__(
        self, name, enable_text_to_text, enable_text_to_image, enable_text_to_speech
    ):
        self.name = name
        self.enable_text_to_text = enable_text_to_text
        if self.enable_text_to_text:
            self.llm_model = "models/mistral-7b-instruct-v0.1.Q4_0.gguf"
        self.enable_text_to_image = enable_text_to_image
        self.enable_text_to_speech = enable_text_to_speech
