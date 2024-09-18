import assemblyai as aai

class AI_Speech_Recognition:
    def __init__(self):
        aai.settings.api_key= "e00c3bb6dd714a1d99364bba25f507d8"
        self.transcriber = None

    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data= self.on_data,
            on_error= self.on_error,
            on_open= self.on_open,
            on_close= self.on_close,
            end_utterance_silence_threshold= 1000
        )

        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        # print("Session ID:", session_opened.session_id)
        return


    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            print(transcript.text, end="\r\n")
        else:
            print(transcript.text, end="\r")


    def on_error(self, error: aai.RealtimeError):
        # print("An error occured:", error)
        return


    def on_close(self):
        # print("Closing Session")
        return