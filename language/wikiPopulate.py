import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language.settings')
import django
django.setup()
from wiki.models import Category, Page

def populate():
    Category.objects.all().delete()
    Page.objects.all().delete()
    # Python
    category = addCategory('Python')
    addPage(category, '官方 Python 教材', 'http://docs.python.org/2/tutorial/')
    addPage(category, '如何像電腦科學家一樣思考', 'http://www.greenteapress.com/thinkpython/')
    addPage(category, '10 分鐘內學好 Python', 'http://www.korokithakis.net/tutorials/python/')
    # 其他程式語言
    category = addCategory('其他程式語言')
    addPage(category, 'C 程式語言', 'http://www.tutorialspoint.com/cprogramming/c_overview.htm')
    addPage(category, 'Java 程式語言', 'https://www.java.com/zh_TW/')
    # Django
    category = addCategory('Django')
    addPage(category, '官方 Django 教材', 'https://docs.djangoproject.com/en/1.8/intro/tutorial01/')
    addPage(category, 'Django 真讚', 'http://www.djangorocks.com/')
    addPage(category, '如何和 Django 跳探戈', 'http://www.tangowithdjango.com/')
    # 其他框架
    category = addCategory('其他框架')
    addPage(category, 'Bottle 框架', 'http://bottlepy.org/docs/dev/')
    addPage(category, 'Flask 框架', 'http://flask.pocoo.org')
    # 印出所輸入的資料
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(category.name, '--', page.title)
            
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    return category

def addPage(category, title, url):
    Page.objects.get_or_create(category=category, title=title, url=url)

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 