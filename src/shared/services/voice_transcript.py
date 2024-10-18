import whisper


class VoiceTranscript:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcript(self, audio_file):
        return self.model.transcribe(audio_file)
