# coding=utf-8

import json
import os
import BigWorld
from gui import SystemMessages
from ..utils import print_log
from .modNotification import show_notification


class Config:
  config = {}
  defaultParams = {
    'version': '0.0.0.0',
    'initBattleURL': 'http://ns3130917.ip-51-75-52.eu:19079/api/events/OnBattleStart',
    'eventURL': 'http://ns3130917.ip-51-75-52.eu:19079/api/events/send',
    'updateURL': 'https://api.github.com/repos/gogolevjuri/wmm/releases/latest',
    'statusURL': 'http://ns3130917.ip-51-75-52.eu:19070/api',
    'lokiURL': 'https://loki.wotstat.info/loki/api/v1/push',
    'hideServer': False,
    'disableCopyToFuture': False,
    'disableAutoUpdate': False,
  }

  def __init__(self, ConfigPath, DefaultParams=None):
    self.config = {}
    if DefaultParams:
      self.defaultParams = DefaultParams

    if os.path.exists(ConfigPath):
      with open(ConfigPath, "r") as f:
        try:
          self.config = json.loads(f.read())
          print_log('found new config:')
          print_log(self.config)

          newInit = self.config.get('initBattleURL', None)
          newEvent = self.config.get('eventURL', None)
          newUpdate = self.config.get('updateURL', None)

          if newInit and newInit != self.defaultParams.get('initBattleURL') or \
             newEvent and newEvent != self.defaultParams.get('eventURL') or \
             newUpdate and newUpdate != self.defaultParams.get('updateURL'): 
            config_str = '''\n------\n'''.join("%s: %s" % (key, value) for key, value in self.config.items())
            message = '''[WotStat] Обнаружена новая конфигурация в файле /mods/configs/wot_stat/config.cfg\n------\n%s''' % config_str

            BigWorld.callback(5.0, lambda: show_notification(message, message_type=SystemMessages.SM_TYPE.Warning))
        except Exception as e:
          print_log('load config error')
          print_log(e)

    try:
      # noinspection PyUnresolvedReferences
      self.config['version'] = version # type: ignore # noqa: F821
    except Exception as e:
      pass

  def get(self, key):
    return self.config[key] if key in self.config else self.defaultParams[
      key] if key in self.defaultParams else None
