from collections import defaultdict
import csv
from datetime import datetime as dt

from pep_parse.settings import (
    BASE_DIR,
    DATETIME_FORMAT,
    RESULTS_DIR,
    RESULTS_DIR_NAME,
    STATUS_QUANTITY_TUPLE,
    TOTAL,
)

FILE_PATH_NAME = 'status_summary_{date}.csv'


class PepParsePipeline:
    """Класс для парсинга и написания файла документов PEP."""

    def __init__(self):
        RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """Метод срабатывающий при начале работы паука."""
        self.counts_statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Метод обработки результатов парсинга."""
        self.counts_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Метод срабатывает при закрытии паука, создает csv файл."""
        with open(BASE_DIR / RESULTS_DIR_NAME / (
            FILE_PATH_NAME.format(date=dt.now().strftime(DATETIME_FORMAT))
        ), mode='w', encoding='utf-8') as file:
            csv.writer(
                file, csv.unix_dialect, quoting=csv.QUOTE_MINIMAL,
            ).writerows(
                (
                    STATUS_QUANTITY_TUPLE,
                    *self.counts_statuses.items(),
                    (TOTAL, sum(self.counts_statuses.values())),
                ),
            )
