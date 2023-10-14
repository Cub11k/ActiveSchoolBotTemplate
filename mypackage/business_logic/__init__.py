from telebot import TeleBot
from telebot.util import antiflood
from telebot.apihelper import ApiException

import hashlib


APPROVED_SYMBS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя- '

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
    result = False
    if 5 <= len(name) <= 20 and all(s in APPROVED_SYMBS for s in name) and name[0].isupper():
        result = True
    return result


def check_point_name(name: str) -> bool:
    result = False
    if 2 <= len(name) <= 20 and all(s in APPROVED_SYMBS for s in name):
        result = True
    return result


def get_hash(user_input: str) -> str:
    result = hashlib.sha256(bytes(user_input, 'utf-8')).hexdigest()
    return result


def check_admin_password(password_hash: str, user_input: str) -> bool:
    result = True
    if hashlib.sha256(bytes(user_input, 'utf-8')).hexdigest() != password_hash:
        result = False
    return result


def check_manager_password(password_hash: str, user_input: str) -> bool:
    result = True
    if hashlib.sha256(bytes(user_input, 'utf-8')).hexdigest() != password_hash:
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
    # Assign starting points to teams
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
