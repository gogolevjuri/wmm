import BigWorld
from .common.serverLogger import send, LEVELS


def print_log(log):
  print("%s [YG2MOD_WOT_STAT]: %s" % (BigWorld.serverTime(), str(log)))
  send(LEVELS.INFO, str(log))


def print_error(log):
  print("%s [YG2MOD_WOT_STAT ERROR]: %s" % (BigWorld.serverTime(), str(log)))
  send(LEVELS.ERROR, str(log))


def print_warn(log):
  print("%s [YG2MOD_WOT_STAT WARN]: %s" % (BigWorld.serverTime(), str(log)))
  send(LEVELS.WARN, str(log))


def print_debug(log):
  if DEBUG_MODE:
    print("%s [YG2MOD_WOT_STAT DEBUG ]: %s" % (BigWorld.serverTime(), str(log)))
