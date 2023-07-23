# AI Voice Translator

This repository uses `PyAudio`, `langdetect`, and `googletrans` to generate translated audio. 

## Installation

```
echo -e "SpeechRecognition\npyttsx3\nlangdetect\ngoogletrans==4.0.0-rc1\nmoviepy\ntqdm\nrotary_embedding_torch\ninflect\nprogressbar\neinops\nunidecode\nscipy\nlibrosa\ntransformers\ntokenizers" > requirements.txt
pip install -r requirements.txt
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
python setup.py install
```


## Usage

The following command will prompt the text "Speak something...", in which you can speak into the mic.

    python3 translate.py

It will recognize the voice, and interpret what was received in terminal. Thehn, it produces an outputed translated in spanish or english (depending on which language was spoken).

## License

This script is open-source and licensed under the MIT License. For more details, check the [LICENSE](LICENSE) file.
