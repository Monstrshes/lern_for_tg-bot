from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str  #токен для доступа к боту

class Config:
    tg_bot: TgBot

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))