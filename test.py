#coding:utf-8

import manage
from db.models import TestDb

if __name__ == '__main__':

    TestDb.objects.create(title='test')
    print(TestDb.objects.get(title='test'))
