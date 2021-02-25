from system.input import *
from system.output import *

from modules.device import *
from modules.info import *
from modules.media import *


registry = {
    # info
    'general_info_query':general_info,
    # media
    'play_media':mediaplayer.mediaplayer(),
}       


class processor():
    def __init__(self, output = text2speech):
        self.output = output

    def processAction(self, intent = "", **kwargs):
        if not intent:
            return 'Cannot parse empty intent'
        
        try:
            #self.registry[intent]['function'].run()
            x = registry[intent].run([arg for arg in kwargs.values()])
            if isinstance(x, str): return self.output.engine(x)
            print(intent, [arg for arg in kwargs.values()])
        except:
            return 'There is no function linked to that intent'


