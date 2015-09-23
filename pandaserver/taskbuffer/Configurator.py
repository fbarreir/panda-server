from config import panda_config
from pandalogger.PandaLogger import PandaLogger
from brokerage.SiteMapper import SiteMapper
from taskbuffer.TaskBuffer import taskBuffer as task_buffer

# logger
logger = PandaLogger().getLogger(__name__.split('.')[-1])

class JobBroker ():
    
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