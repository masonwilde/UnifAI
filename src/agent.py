import text_to_text.gpt4all as ttt
import text_to_image.stable_diffusion_wrapper as tti
import text_to_speech as tts


class Agent:
    def __init__(self, config):
        self.config = config
        if self.config.enable_text_to_text:
            print("Loading text to text...")
            self.ttt = ttt.TTT(config)
            print("Loaded text to text.")
        if self.config.enable_text_to_image:
            print("Loading text to image...")
            self.tti = tti.TTI(config)
            print("Loaded text to image.")
        if self.config.enable_text_to_speech:
            print("Loading text to speech...")
            self.tts = tts.TTS(config)
            print("Loaded text to speech.")

    def prompt_ttt(self, prompt):
        if not self.config.enable_text_to_text:
            raise Exception("Text to text is not enabled.")
        return self.ttt.prompt(prompt)

    def prompt_tti(self, prompt):
        if not self.config.enable_text_to_image:
            raise Exception("Text to image is not enabled.")
        img = self.tti.prompt(prompt)
        img.show()

    def prompt_tts(self, prompt):
        if not self.config.enable_text_to_speech:
            raise Exception("Text to speech is not enabled.")
        return self.tts.prompt(prompt)
