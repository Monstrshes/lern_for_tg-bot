from environs import Env
from dataclasses import dataclass



@dataclass
class Tg_Bot():
    token: str

@dataclass
class Config():
    tg_bot: Tg_Bot

def load_config(path = None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=Tg_Bot(token=env('BOT_TOKEN')))