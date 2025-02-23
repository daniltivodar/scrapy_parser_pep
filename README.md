# Парсер на Scrapy

Парсес на Scrapy, это проект, который написан с целью получения всей необходимой информации о документах PEP. В парсере есть паук, который подключается к необходимым источникам в сети, и быстро собирает всю необходимую информацию.

### Технологии
- Python
- Scrapy
- csv

## Установка

1. Склонируйте репозиторий.
```bash
git clone https://github.com/daniltivodar/bs4_parser_pep.git
```

2. Создайте и активируйте виртуальное окружение, заполнив его зависимостями из файла **requirements.txt**.
```bash
cd bs4_parser_pep
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

3. Запустить паука, можно командой:
```bash
scrapy crawl pep
```

##Создатель
**[Данил Тиводар](https://github.com/daniltivodar)**