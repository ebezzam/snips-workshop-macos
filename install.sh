brew tap snipsco/homebrew-snips
brew install snips-asr snips-hotword snips-dialogue snips-watch snips-audio-server snips-nlu snips-tts
brew install mosquitto

# start Snips components
brew services start mosquitto
brew services start snips-audio-server
brew services start snips-hotword
brew services start snips-tts
brew services start snips-nlu
brew services start snips-asr
brew services start snips-dialogue

# install packages
pip install -r requirements.txt

# unzip assistant
unzip assistant_BEZZAM.zip