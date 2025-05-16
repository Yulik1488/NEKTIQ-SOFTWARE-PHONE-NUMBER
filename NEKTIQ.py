
from pystyle import Colorate, Colors, Center
import os
import requests
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import NumberParseException, PhoneNumberType, number_type
from datetime import datetime
import pytz
from colorama import Fore, Style
import time
from geopy.geocoders import Nominatim

def clear_console():
    # Команда для очистки консоли зависит от операционной системы
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux и macOS
        os.system('clear')


def menu():
    clear_console()
    clear_console()

    banner = r"""

                                             ,----,                         
             ,--.                 ,--.     ,/   .`|                         
           ,--.'|    ,---,.   ,--/  /|   ,`   .'  :   ,---,    ,----..      
       ,--,:  : |  ,'  .' |,---,': / ' ;    ;     /,`--.' |   /   /   \     
    ,`--.'`|  ' :,---.'   |:   : '/ /.'___,/    ,' |   :  :  /   .     :    
    |   :  :  | ||   |   .'|   '   , |    :     |  :   |  ' .   /   ;.  \   
    :   |   \ | ::   :  |-,'   |  /  ;    |.';  ;  |   :  |.   ;   /  ` ;   
    |   : '  '; |:   |  ;/||   ;  ;  `----'  |  |  '   '  ;;   |  ; \ ; |   
    '   ' ;.    ;|   :   .':   '   \     '   :  ;  |   |  ||   :  | ; | '   
    |   | | \   ||   |  |-,|   |    '    |   |  '  '   :  ;.   |  ' ' ' :   
    '   : |  ; .''   :  ;/|'   : |.  \   '   :  |  |   |  ''   ;  \; /  |   
    |   | '`--'  |   |    \|   | '_\.'   ;   |.'   '   :  | \   \  ',  . \  
    '   : |      |   :   .''   : |       '---'     ;   |.'   ;   :      ; | 
    ;   |.'      |   | ,'  ;   |,'                 '---'      \   \ .'`--"  
    '---'        `----'    '---'                               `---`        

     
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬



    """
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(banner)))
    number()



def number():
    number_input = input(Fore.RED + "[ + ] Введите номер телефона: ")
    try:
        google_link = f"https://www.google.com/search?q={number_input}"
        yandex_link = f"https://yandex.ru/search/?text={number_input}"
        parsed_number = phonenumbers.parse(number_input)
        country = geocoder.description_for_number(parsed_number, "ru") or "Не найдено"
        subscriber = carrier.name_for_number(parsed_number, "ru") or "Не найдено"
        timezones = timezone.time_zones_for_number(parsed_number)
        valid_number = phonenumbers.is_valid_number(parsed_number)


        number_type_value = number_type(parsed_number)

        if number_type_value == PhoneNumberType.MOBILE:
            number_kind = "Мобильный"
        elif number_type_value == PhoneNumberType.FIXED_LINE:
            number_kind = "Стационарный"
        elif number_type_value == PhoneNumberType.FIXED_LINE_OR_MOBILE:
            number_kind = "Стационарный или мобильный"
        elif number_type_value == PhoneNumberType.VOIP:
            number_kind = "Виртуальный"
        elif number_type_value == PhoneNumberType.TOLL_FREE:
            number_kind = "Бесплатный"
        elif number_type_value == PhoneNumberType.PREMIUM_RATE:
            number_kind = "Премиум"
        elif number_type_value == PhoneNumberType.SHARED_COST:
            number_kind = "Общий тариф"
        elif number_type_value == PhoneNumberType.UNKNOWN:
            number_kind = "Неизвестный"
        else:
            number_kind = "Другой"

        telegram_link = f"https://t.me/{number_input}"
        viber_link = f"viber://chat?number={number_input}"
        whatsapp_link = f"https://wa.me/{number_input.strip('+')}"
        region = geocoder.region_code_for_number(parsed_number) or "Не найдено"
        country_code = f"+{parsed_number.country_code}"
        national_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        possible = phonenumbers.is_possible_number(parsed_number)
        possible_status = "True" if possible else "False"
        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rfc3966_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.RFC3966)
        number_length = sum(1 for char in number_input if char.isdigit())
        from geopy.geocoders import Nominatim

        country_time = "Не найдено"
        if timezones:
            try:
                # Берем первый часовой пояс
                timezone_str = timezones[0]
                tz = pytz.timezone(timezone_str)
                country_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                country_time = f"Ошибка получения времени: {str(e)}"
        else:
            country_time = "Не найдено"

        if phonenumbers.is_valid_number(parsed_number):
            if parsed_number.country_code == 1:
                number_format = "Международный"
            else:
                number_format = "Национальный"
        else:
            number_format = "Невалидный"

        print(Fore.RED + f"                                               ")
        print(Fore.RED + f"🔍 Результат по номеру телефона -> {number_input}")
        print(Fore.RED + f"                                               ")
        print(Fore.RED + f"[+] Результат с Phonenumbers:")
        print(Fore.RED + f"[+] Номер телефона -> {number_input}")
        print(Fore.RED + f"[+] Страна/Город -> {country}")
        print(Fore.RED + f"[+] Код страны ->  {region}")
        print(Fore.RED + f"[+] Оператор ->  {subscriber}")
        print(Fore.RED + f"[+] Код номера -> {country_code}")
        print(Fore.RED + f"[+] Активен -> {possible_status}")
        print(Fore.RED + f"[+] Валид -> {valid_number}")
        print(Fore.RED + f"[+] Таймзона -> {', '.join(timezones)}")
        print(Fore.RED + f"[+] Количество таймзон -> № {len(timezones)}")
        print(Fore.RED + f"[+] Тип номера -> {number_kind}")
        print(Fore.RED + f"[+] Длина номера -> {number_length} ")
        print(Fore.RED + f"[+] Формат номера -> {number_format}")
        print(Fore.RED + f"[+] Формат международного номера -> {international_format}")
        print(Fore.RED + f"[+] Формат национального номера -> {national_number}")
        print(Fore.RED + f"[+] Время в стране/городе -> {country_time}")
        print(Fore.RED + f"-----------‐--------------‐--------------‐---")
        print(Fore.RED + f"[+] Мессенджеры:")
        print(Fore.RED + f"[+] Telegram -> {telegram_link}")
        print(Fore.RED + f"[+] WhatsApp -> {whatsapp_link}")
        print(Fore.RED + f"[+] Viber -> {viber_link}")
        print(Fore.RED + f"[+] Дзвонок на номер -> {rfc3966_format}")
        print(Fore.RED + f"-----------‐--------------‐--------------‐---")
        print(Fore.RED + f"[+] Социальние сети:")
        print(Fore.RED + f"[+] Instagram -> https://www.instagram.com/accounts/password/reset ")
        print(Fore.RED + f"[+] FaceBook -> https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar ")
        print(Fore.RED + f"[+] Twitter -> https://twitter.com/account/begin_password_reset ")
        print(Fore.RED + f"[+] Linkedin -> https://www.linkedin.com/checkpoint/rp/request-password-reset")
        print(Fore.RED + f"[+] Vkontakte -> https://vk.com/restore")
        print(Fore.RED + f"[+] OK -> https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink")
        print(Fore.RED + f"[+] Microsoft -> https://account.live.com/acsr")
        print(Fore.RED + f"-----------‐--------------‐--------------‐---")
        print(Fore.RED + f"[+] Дополнение:")
        print(Fore.RED + f"[+] Google -> {google_link}")
        print(Fore.RED + f"[+] Яндекс -> {yandex_link}")
        print(Fore.RED + f"[+] Время спроса -> {current_time}")

    except phonenumbers.phonenumberutil.NumberParseException:
        print(Fore.RED + "Некорректный формат номера. Попробуйте снова.")


    choice = input("Нажмите 'y', чтобы продолжить, или 'n', чтобы выйти:").lower()
    if choice == 'y':
        menu()
    elif choice == 'n':
        clear_console()
        exit()
    else:
        clear_console()
        exit()

if __name__ == "__main__":
    menu()













