import os

os.environ.setdefault('user_setting', 'usersetting.setting')
from conf import settings

print(settings.DEBUG)
