
from datetime import datetime
from wisp import Wisp
import time

class Party(object):

    def __init__(self, id_num, api_secrets, guild=None):
        self.a_name = 'p' + str(id_num)
        self.name = 'p' + str(id_num)
        self.id_num = id_num
        self.api_secrets = api_secrets
        self.guild = guild
        self.wisps_len = 0
        self.wisps_list = []
        self.time_spawned_epoch = time.time()
        self.time_spawned_UTC = datetime.utcnow()

    @staticmethod
    def spawn(guild, id_num, api_secrets):
        party = Party(id_num, api_secrets, guild=guild)
        return (party)

    def spawn_wisp(self):
        self.wisps_list.append(Wisp.spawn(self))
        self.wisps_len += 1

    def wisps_printNames(self):
        for wisp in self.wisps_list:
            print "name: ", wisp.name






