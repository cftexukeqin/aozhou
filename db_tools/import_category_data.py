import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aozhou.settings')

import django
django.setup()

from apps.goods.models import GoodsCategory

from db_tools.data.category import row_data

for category in row_data:\
    # 实例化
    instance = GoodsCategory()
    instance.desc = category['desc']
    instance.name = category['name']
    instance.save()

print("数据库分类数据写入成功!")