import os
import importlib
from conf import globalsetting


class Setting:
    def __init__(self):
        user_setting = os.environ.get('user_setting')
        print(dir(globalsetting))
        for setting in dir(globalsetting):
            if setting.isupper():
                setattr(self, setting, getattr(globalsetting, setting))

        mod = importlib.import_module(user_setting)
        print(mod)
        for setting in dir(mod):
            if setting.isupper():
                setattr(self, setting, getattr(mod, setting))


settings = Setting()
