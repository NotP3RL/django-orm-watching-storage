# django-orm-watching-storage
Репозиторий с сайтом для урока «Пишем пульт охраны банка» курса dvmn.org

### Как установить

Для запуска необходим Python 3.*, который можно установить с [официального сайта](https://www.python.org/).

После скачивания архива с кодом его необходимо распаковать в пустую папку. После этого необходимо скачать все сторонние библиотеки, открыв папку в консоли и написав в неё:
```
pip install -r requirements.txt
```

Если у Вас есть доступ к удалённой базе данных нашего банка, то создайте .env файл в директории с проектом и заполните настройками в следующем виде:
```
DB_ENGINE=Серверная часть базы данных для использования. 
        Встроенные серверные базы данных:
        'django.db.backends.postgresql'
        'django.db.backends.mysql'
        'django.db.backends.sqlite3'
        'django.db.backends.oracle'
DB_HOST=Какой хост использовать при подключении к базе данных
DB_PORT=Порт, используемый при подключении к базе данных
DB_NAME=Имя используемой базы данных
DB_USER=Имя пользователя, используемое при подключении к базе данных
DB_PASSWORD=Пароль, используемый при подключении к базе данных
DEBUG=True или False для включения/отключения дебаг-режима (необязателен для успешной работы программы)
ALLOWED_HOSTS=Список строк, представляющих имена хостов/доменов, которые могут обслуживать этот сайт Django. (необязателен для тестового запуска)
```

Для установки ключа шифрования паролей пользователей сайта создайте и экспортируйте переменную окружения SECRET_KEY.

### Как запустить

```
python manage.py runserver
```
Далее нужно ввести в новом окне браузера адрес [127.0.0.1:8000](https://127.0.0.1:8000).

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
