echo "you might need to put in your password to install \"portaudio19-dev\""

echo "installing packages"
pip install gtts
pip install playsound
pip install SpeechRecognition

echo "installing dependences for \"SpeechRecognition\""
sudo apt-get install portaudio19-dev
pip install PyAudio