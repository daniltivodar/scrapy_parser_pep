from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

BASE_DIR = Path('__file__').parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

RESULTS_DIR_NAME = 'results'

RESULTS_DIR = BASE_DIR / RESULTS_DIR_NAME

STATUS_QUANTITY_TUPLE = ('Статус', 'Количество')

TOTAL = 'Итого'

FEEDS = {
    '{dir_name}/pep_%(time)s.csv'.format(dir_name=RESULTS_DIR_NAME): {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
