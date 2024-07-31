# -*- coding: utf-8 -*-
from helpers import getClientLanguage

RU = {
  "modUpdated": "YG [WotStat] успешно обновлён до версии %s. После перезапуска игры обновление будет применено",
  "serverNotResponse": "YG [WotStat] В данный момент наблюдаются проблемы с сервером WotStat. Если проблема будет продолжаться более дня, напишите на почту soprachev@mail.ru",
  "modslist.title": "YG WotStat Аналитика",
  "modslist.description": "YG Просмотр персональной аналитики WotStat за текущую сессию",
  "helloNotification": "YG WotStat успешно активирован, ваша персональная аналитика за сессию доступна по ссылке <a href=\"event:%s\">%s</a>",
  "openDialog.title": "YG WotStat Аналитика",
  "openDialog.body": "YG Персональная сессионная аналитика откроется в браузере по умолчанию.\n\nНовые события в сессии подгружаются автоматически.",
  "openDialog.cancelButton": "YG Отмена",
  "openDialog.openButton": "YG Открыть в браузере"
}

EN = {
  "modUpdated": "wg2 [WotStat] successfully updated to version %s. The update will be applied after restarting the game.",
  "serverNotResponse": "wg2 [WotStat] Currently experiencing issues with the WotStat server. If the problem persists for more than a day, please write to soprachev@mail.ru",
  "modslist.title": "wg2 WotStat Analytics",
  "modslist.description": "wg2 View your WotStat personal analytics for the current session",
  "helloNotification": "wg2 WotStat successfully activated, your session personal analytics are available at <a href=\"event:%s\">%s</a>",
  "openDialog.title": "wg2 WotStat Analytics",
  "openDialog.body": "wg2 Your session personal analytics will open in the default browser.\n\nNew session events are automatically loaded.",
  "openDialog.cancelButton": "wg2  Cancel",
  "openDialog.openButton": "wg2 Open in browser"
}
language = getClientLanguage()
current_localizations = RU

if language == 'ru':
  current_localizations = RU
else:
  current_localizations = EN


def t(key):
  if key in current_localizations:
    return current_localizations[key]
  return key
