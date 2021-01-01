# Joni

Joni is a script that can be combined with [nfc-daemon](https://github.com/whotwagner/nfc-daemon.git). It queries a yaml-file
with the given uid of a nfc-tag in order to get a playlist and it plays it

# Install

```
pip3 install .
```

# Configure

```yaml
mpdport: 6600      # optional
mpdhost: localhost # optional
volume: 60         # optional
timeout: 10        # optional

tracks:
    - id: 199392919
      description: "Back to Black and AnneKaffeekanne"
      volume: 5 # optional
      play: 
        - spotify:track:2iEGj7kAwH7HAa5epwYwLB
        - file:///home/pi/Kindercds/annekaffekanne/Track01.wav
```

# Usage

Play a playlist connected to a specific tag:
```
jon.py -L /var/log/joni.log --start 199392919
```

Stop playing:
```
jon.py --stop
```

List tracks:
```
bin/jon.py --list
Music-Database:
ID: 199392919
DESCRIPTION: Back to Black and AnneKaffeekanne
	spotify:track:2iEGj7kAwH7HAa5epwYwLB
	file:///home/pi/Kindercds/annekaffekanne/Track01.wav
```

# Author

Wolfgang Hotwagner (code@feedyourhead.at)

# License

GPL3
