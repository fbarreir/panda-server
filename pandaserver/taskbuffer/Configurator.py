from config import panda_config
from pandalogger.PandaLogger import PandaLogger
from brokerage.SiteMapper import SiteMapper
from taskbuffer.TaskBuffer import taskBuffer as task_buffer

# logger
logger = PandaLogger().getLogger(__name__.split('.')[-1])

class Configurator():
    
    def __init__(self):
        task_buffer.init(panda_config.dbhost, panda_config.dbpasswd, panda_config.nDBConnection ,True)
        site_mapper = SiteMapper(task_buffer)

    def get_nuclei(self):
        """
        First implementation: return the Tier1s...
        """
        #TODO: discuss with Tadashi what format he wants, if he wants sitenames, queues, SE...
        tier1s = []
        for cloud_name in site_mapper.getCloudList():
            # get cloud
            cloud_spec = site_mapper.getCloud(cloud_name)
            # get T1
            t1_name = cloud_spec['source']
            
            tier1s.append(t1_name)
        return tier1s


    def get_satellites(self, site=None, task_id=None):
        return []


    # update endpoint dict
    def get_tier1s_agis(self):
        # get json
        try:
            tmpLog.debug('start')
            jsonStr = ''
            res = urllib2.urlopen('http://atlas-agis-api.cern.ch/request/site/query/list_sites_names/?json&tier_level=1')
            jsonStr = res.read()
            tier1s = json.loads(jsonStr)
            tmpLog.debug('got {0} endpoints '.format(len(self.endPointDict)))
        except:
            errtype,errvalue = sys.exc_info()[:2]
            errStr = 'failed to update EP with {0} {1} jsonStr={2}'.format(errtype.__name__,
                                                                           errvalue,
                                                                           jsonStr)
            tmpLog.error(errStr)
        return