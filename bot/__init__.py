from .start import register_start_handler
from .help import register_help_handler
from .search import register_search_handler
from .recent import register_recent_handler
from .count import register_count_handler
from .grafic import register_grafic_handler
from .search_company import register_search_company_handler
from .search_vacancy import register_search_vacancy_handler

def register_handlers(dp):
    register_start_handler(dp)
    register_help_handler(dp)
    register_search_handler(dp)
    register_recent_handler(dp)
    register_count_handler(dp)
    register_grafic_handler(dp)
    register_search_company_handler(dp)
    register_search_vacancy_handler(dp)
