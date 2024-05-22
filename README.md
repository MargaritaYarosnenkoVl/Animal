README для проекта сайта выставки животных из приюта Доринвест
Обзор проекта
Проект представляет собой веб-сайт, посвященный организации выставок животных из приюта Доринвест. Сайт позволяет просматривать информацию о текущих и прошлых выставках, а также о животных, принимающих участие в них. Пользователи могут оставлять обратную связь и просматривать фотоотчеты с выставок.

Структура проекта
Модели
Show: Информация о выставке, включая название, дату, место проведения, организатора и количество участников.
Animals: Информация о животных, участвующих в выставке, включая имя, описание, возраст, породу и категорию.
Feedback: Обратная связь от пользователей.
Banner: Баннеры, используемые на сайте.
Story: Счастливые истории о животных, которых удалось поместить в новые дома.
Location: Информация о том, как добраться до места проведения выставки.
SocialLinks: Ссылки на социальные сети приюта.
Partners: Информация о партнерах приюта.
EndedShow: Информация о прошедших выставках.
Photoreport: Фотоотчеты с выставок.
AnimalImage: Связь между животными и их фотографиями.
Views
ShowDetail: Отображает подробную информацию о текущей выставке, включая список животных, баннеры, истории, местоположение, социальные ссылки и партнеров.
EndedShowList: Список прошедших выставок.
AnimalList: Список всех животных, участвующих в выставках.
AnimalDetail: Подробная информация о конкретном животном.
URLs
/show/<slug:slug>/: Детальная страница текущей выставки.
/ended_show/: Список прошедших выставок.
/animals/: Список всех животных.
/animals/<slug:slug>/: Детальная страница конкретного животного.
Технологии
Django: Python web framework.
PostgreSQL: База данных.
PythonAnywhere: Хостинг.
Примеры
Сайт
Админ панель
Запуск проекта
Для запуска проекта необходимо установить зависимости, выполнить миграции и запустить сервер разработки Django.

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Лицензия
Проект распространяется под MIT License.
