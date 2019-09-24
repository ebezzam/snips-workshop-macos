# replace assistant
rm -rf /usr/local/share/snips/assistant
cp -r assistant /usr/local/share/snips
./restart.sh

# run simple assistant
python V1_action-how-are-you.py