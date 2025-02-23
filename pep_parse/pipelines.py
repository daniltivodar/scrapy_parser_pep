from collections import defaultdict
import csv
from datetime import datetime as dt

from pep_parse.constants import (
    DATETIME_FORMAT,
    RESULTS_DIR_NAME,
    STATUS_QUANTITY_TUPLE,
    TOTAL,
)
from pep_parse.settings import BASE_DIR

FILE_PATH_NAME = 'status_summary_{date}.csv'


class PepParsePipeline:
    """Класс для парсинга и написания файла документов PEP."""

    def open_spider(self, spider):
        """Метод срабатывающий при начале работы паука."""
        self.counts_statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Метод обработки результатов парсинга."""
        self.counts_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Метод срабатывает при закрытии паука, создает csv файл."""
        results_dir = BASE_DIR / RESULTS_DIR_NAME
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / (
            FILE_PATH_NAME.format(date=dt.now().strftime(DATETIME_FORMAT))
        )
        with open(file_path, mode='w', encoding='utf-8') as file:
            csv.writer(file, csv.unix_dialect).writerows(
                [
                    STATUS_QUANTITY_TUPLE,
                    *self.counts_statuses.items(),
                    (TOTAL, sum(self.counts_statuses.values())),
                ]
            )
            file.truncate()
