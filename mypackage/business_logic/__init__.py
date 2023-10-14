from telebot import TeleBot
from telebot.util import antiflood
from telebot.apihelper import ApiException

import hashlib


LOWER_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
UPPER_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
EMPTY_SYMB = ' '
CONNECT_SYMB = '-'
UTF = 'utf-8'


def send_text(bot: TeleBot, chat_id: int, text: str) -> bool:
    result = True
    # Send text to chat_id
    try:
        antiflood(bot.send_message, chat_id, text)
    except ApiException:
        result = False
    return result


# _______________________________________________________________

def check_team_name(name: str) -> bool:
    result = True
    should_upper = True
    if len(name) < 3 or len(name) > 20:
        return False
    
    for symb in name:
        if should_upper and not (symb in UPPER_LETTERS):
            return False
        elif symb == CONNECT_SYMB or symb == EMPTY_SYMB:
            should_upper = True
            continue
        elif symb in UPPER_LETTERS:
            return False
        elif not symb in LOWER_LETTERS:
            return False
        should_upper = False
    return result


def check_point_name(name: str) -> bool:
    result = True
    if len(name) < 2 or len(name) > 30:
        return False
    
    if not name[0] in UPPER_LETTERS:
        result = False
    for symb in name[1:]:
        if (not symb in LOWER_LETTERS) and symb != CONNECT_SYMB:
            return False
    return result


def get_hash(user_input: str) -> str:
    result = hashlib.sha256(bytes(user_input, UTF)).hexdigest()
    return result


def check_admin_password(password_hash: str, user_input: str) -> bool:
    result = True
    if hashlib.sha256(bytes(user_input, UTF)).hexdigest() != password_hash:
        result = False
    return result


def check_manager_password(password_hash: str, user_input: str) -> bool:
    result = True
    if hashlib.sha256(bytes(user_input, UTF)).hexdigest() != password_hash:
        result = False
    return result


def assign_starting_point_messages(teams: dict[int, dict], points: list[str], base_message: str) -> dict[int, str]:
    """

    :param teams: Dictionary of teams: {user_id: {name: str, balance: int, chat_id: int}}
    :param points: List of point names
    :param base_message: Base message to be formatted with point name via str.format()
    :return: Dictionary of starting point messages: {chat_id: message}
    """
    result = {}



    return result


def broadcast_starting_points(bot: TeleBot, messages: dict[int, str]) -> dict[int, bool]:
    """

    :param bot: TeleBot instance
    :param messages: Dictionary of messages: {chat_id: message}
    :return:Dictionary of results: {chat_id: result}
    """
    result = {}
    
    for i in messages.keys():
        msgreturn = bot.send_message(i, messages[i])
        if msgreturn.message_id:
            result[i] = True
        else:
            result[i] = False

    return result
