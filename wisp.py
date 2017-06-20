
from datetime import datetime
import time

class Wisp(object):
    def __init__(self, party):
        self.name = None
        self.id_num = None
        self.response_status = None
        self.party = party        
        self.ip = None
        self.digital_ocean_id = None
        self.snapshot_id = None
        self.time_spawned_epoch = None
        self.time_spawned_UTC = None

    @staticmethod
    def spawn(party):
        wisp = Wisp(party)
        wisp.find_soul()
        return (wisp)

    def find_soul(self):
        self.id_num = self.party.wisps_len
        self.a_name = 'w' + str(self.id_num) + self.party.name
        self.name = 'w' + str(self.id_num) + self.party.name
        self.response_status = 200        
        self.ip = "1.2.5.6.2.5"
        self.digital_ocean_id = "29f999a9b9c9d9ccccc99d9e92f2c2"
        self.snapshot_id = "014824298198137"
        self.time_spawned_epoch = time.time()
        self.time_spawned_UTC = datetime.utcnow()





