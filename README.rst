djlime-metatags
===============

Django-приложение, позволяющее задать мета-теги для объектов базы данных и URL-путей.

Установка
---------

$ pip install djlime-metatags

Подключение
-----------

- Добавьте приложение metatags в кортеж INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'metatags',
    )
- Выполните команду::

    python manage.py migrate

- Для подключения мета-тегов к объектам необходимо импортировать класс MetaTagInline в файл admin.py, вашего приложения и указать его в списке inlines, ModelAdmin-класса ::

    from metatags.admin import MetaTagInline
    
    ...

    class PageAdmin(admin.ModelAdmin):
        list_display = ('url', 'title')
        inlines = (MetaTagInline,)

    ...

- Также приложение реализует свой ModelAdmin класс, реализующий интерфейс добавления мета-тегов для заданных URL-путей.

- Загрузите библиотеку тегов **{% load meta_tags %}** и создайте в секции head блок, для включения метатегов: ::

    {% load meta_tags %}

    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />

        {% block meta_tags %}
            {% include_meta_tags %}
        {% endblock %}
        ...
    </head>

Параметры включающего тега include_meta_tags
--------------------------------------------

Вcе параметры являются необязательными.

**model_instance** - Экземпляр модели, для которого необходимо получить мета-теги. None по умолчанию.

**page_title_field** - Поле модели, хранящее альтернативный заголовок страницы. 'title' по умолчанию.

**default_title** - Заголовок страницы по умолчанию. Используется совместно с URL-путями, и не имеет никакого
смысла при передаче экземпляра модели во включающий тег. '' по умолчанию.

**default_keywords** - Ключевые слова по умолчанию.

**default_description** - Описание по умолчанию.


Команды управления
------------------

**syncmetatags** - синхронизация полей при совместном использовании с приложением django-modeltranslation.
Данная команда доступна начиная с версии **0.9.11**.
