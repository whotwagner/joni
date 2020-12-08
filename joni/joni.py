import yaml
import logging
from pathlib import Path
from .model import ConfigModel
from mpd import MPDClient

class Joni:
    cfgfile = None
    config = None
    client = None

    def __init__(self, cfgfile='test.yml'):
        logging.debug("Config-File: %s", cfgfile)
        self.cfgfile = cfgfile
        self.readCfg(self.cfgfile)
        self.client = MPDClient()
        self.client.timeout = self.config.timeout
        self.client.connect(self.config.mpdhost, self.config.mpdport)
        self.client.setvol(self.config.volume)
        logging.debug("mpd_version: %s", self.client.mpd_version)

    def readCfg(self,cfgfile):
        path = Path(cfgfile)
        with open(path) as f:
            ymldata = yaml.load(f, Loader=yaml.FullLoader)
        try:
            self.config = ConfigModel(**ymldata)
        except ValidationError as e:
            print(e.errors())
            logging.error(e.errors())
        f.close()

    def find(self,uid):
        logging.info("Searching for \"%s\"", uid)
        for track in self.config.tracks:
            logging.debug("testing \"%s\" against \"%s\"",uid,track.id)
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
            if track.volume:
                logging.info("Set volume to: %s ", track.volume)
                self.client.setvol(track.volume)
            else:
                self.client.setvol(self.config.volume)
            self.client.clear()
            for item in track.play:
                self.client.add(item)
            logging.info("Start playing...")
            self.client.play()
        else:
            logging.info("NEW NFC-CARD FOUND: %s", uid)

    def stop(self):
        logging.info("Stopping...")
        self.client.stop()
