
from datetime import datetime
from party import Party
import time

class Guild(object):

    def __init__(self, id_num):
        self.a_name = 'g' + str(id_num)
        self.name = 'g' + str(id_num)
        self.id_num = id_num
        self.parties_len = 0       
        self.parties_list = []
        self.time_spawned_epoch = time.time()
        self.time_spawned_UTC = datetime.utcnow()
    
    def spawn_party(self, id_num, api_secrets):
        print "api_secrets: ", api_secrets
        party = Party.spawn(self, id_num, api_secrets)
        self.parties_list.append(party)
        self.parties_len += 1
        return (party)

    def parties_printNames(self):
        for party in self.parties_list:
            print "name: ", party.name




  
