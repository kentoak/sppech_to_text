def transribe_file(speech_file,lang="Japanese"):
    lang_code={
        'English':'en-US',
        'Japanese':'ja-JP',
    }
    client = speech.SpeechClient()
    with io.open(speech_file,'rb') as f:
        c=f.read()
    audio = speech.RecognitionAudio(content=c)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=lang_code[lang]
    )
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
    
