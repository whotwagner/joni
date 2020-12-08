import yaml
from pathlib import Path
from .model import ConfigModel
from mpd import MPDClient

class Joni:
    cfgfile = None
    config = None
    client = None

    def __init__(self, cfgfile='test.yml'):
        print("Config-File: %s" % cfgfile)
        self.cfgfile = cfgfile
        self.readCfg(self.cfgfile)
        self.client = MPDClient()
        self.client.timeout = self.config.timeout
        self.client.connect(self.config.mpdhost, self.config.mpdport)
        self.client.setvol(self.config.volume)
        print("mpd_version: %s" % self.client.mpd_version)

    def readCfg(self,cfgfile):
        path = Path(cfgfile)
        with open(path) as f:
            ymldata = yaml.load(f, Loader=yaml.FullLoader)
        try:
            self.config = ConfigModel(**ymldata)
            print(self.config.tracks)
        except ValidationError as e:
            print(e.errors())
        f.close()

    def find(self,uid):
        print("Searching for \"%s\"" % uid)
        for track in self.config.tracks:
            print("testing \"%s\" against \"%s\"" % (uid,track.id))
            if str(track.id) == str(uid):
                return track
        return None
    
    def list(self):
        print("Music-Database:")
        for track in self.config.tracks:
            print("ID: %s" % track.id)
            if track.description:
                print("DESCRIPTION: %s" % track.description)
            for item in track.play:
                print("\t%s" % item)

    def start(self,uid):
        track = self.find(uid)
        if track != None:
            print("Found: %s" % track.play)
            if track.volume:
                print("Set volume to: %s " % track.volume)
                self.client.setvol(track.volume)
            else:
                self.client.setvol(self.config.volume)
            self.client.clear()
            for item in track.play:
                self.client.add(item)
            self.client.play()
        else:
            print("NEW NFC-CARD FOUND")

    def stop(self):
        print("Stopping..")   
        self.client.stop()
