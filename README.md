# Популярность бренда

Проект предназначен для оценки популярности Coca-Cola во [Вконтакте](https://vk.com). Программа подсчитывает посты с упоминанием бренда за последние 7 дней и строит диаграмму с помощью сервиса [plot.ly](https://plot.ly).

### Как установить

1. Python3 должен быть уже установлен.  
2. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
3. Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
4. Для работы с [Api Вконтакте](https://vk.com/dev) требуется `Сервисный ключ доступа`, чтобы его получить:
    * Зарегистрируйте Standalone-приложение на [vk.com/dev](https://vk.com/dev)
    * Найдите `Сервисный ключ доступа` в настройках приложения

    Найденный ключ следует положить в файл `.env` под именем `VK_SERVICE_KEY`.
5. Для работы с сервисом [plot.ly](https://plot.ly) требуется настроить библиотеку, для этого:
    * Зарегистрируйтесь на [сайте](https://plot.ly/Auth/login/?action=signup#/)
    * Пройдите [Initialization for Online Plotting](https://plot.ly/python/getting-started/#initialization-for-online-plotting)
6. Запустите файл `brand_stats.py`.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
