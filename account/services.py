import re
import random
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import quote
from django.http.response import HttpResponse


def phone_converter(phone):
    phone = re.sub(r"[()-]", "", phone).replace(' ', '')
    return phone


def send_otp(phone):
    servicecodes = {
        100: "Сообщение принято к отправке. На следующих строчках вы найдете идентификаторы отправленных сообщений в том же порядке, в котором вы указали номера, на которых совершалась отправка.",
        200: "Неправильный api_id",
        201: "Не хватает средств на лицевом счету",
        202: "Неправильно указан получатель",
        203: "Нет текста сообщения",
        204: "Имя отправителя не согласовано с администрацией",
        205: "Сообщение слишком длинное (превышает 8 СМС)",
        206: "Будет превышен или уже превышен дневной лимит на отправку сообщений",
        207: "На этот номер (или один из номеров) нельзя отправлять сообщения, либо указано более 100 номеров в списке получателей",
        208: "Параметр time указан неправильно",
        209: "Вы добавили этот номер (или один из номеров) в стоп-лист",
        210: "Используется GET, где необходимо использовать POST",
        211: "Метод не найден",
        220: "Сервис временно недоступен, попробуйте чуть позже.",
        300: "Неправильный token (возможно истек срок действия, либо ваш IP изменился)",
        301: "Неправильный пароль, либо пользователь не найден",
        302: "Пользователь авторизован, но аккаунт не подтвержден (пользователь не ввел код, присланный в регистрационной смс)",
    }
    api_id = '2A6D0CAE-F0F5-30FF-52E9-1225EC4BED94'
    to = '79787370171'
    key = random.randint(999, 9999)
    return key
    # msg = key
    #
    # url = "http://sms.ru/sms/send?api_id=%s&to=%s&text=%s" % (api_id, to, msg)
    # # if cliargs.debug == True:
    # #     url = "%s&test=1" % (url)
    # # elif cliargs.sendername is not None:
    # #     url = "%s&from=%s" % (url, cliargs.sendername)
    # # elif cliargs.time is not None:
    # #     url = "%s&time=%d" % (url, int(cliargs.time))
    # # elif cliargs.translit == True:
    # #     url = '%s&translit=1' % (url)
    #
    # try:
    #     res = urlopen(url)
    #     print("GET: %s %s\nReply:\n%s" % (res.geturl(), res.msg, res.info()))
    # except URLError as errstr:
    #     print("smssend[debug]: %s" % (errstr))
    #
    # service_result = res.read().splitlines()
    # if service_result is not None and int(service_result[0]) == 100:
    #     # return HttpResponse("smssend[debug]: Message send ok. ID: %s" % (service_result[1]))
    #     return key
    # if service_result is not None and int(service_result[0]) != 100:
    #     # return HttpResponse("smssend[debug]: Unable send sms message to %s when service has returned code: %s " % (
    #     #     to, servicecodes[int(service_result[0])]))
    #     return False
