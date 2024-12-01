from environs import Env
import dotenv

env = Env()
env.read_env()

bt = env('BOT_TOKEN')
adm = env('ADMIN_ID')
print(bt)
print(adm)