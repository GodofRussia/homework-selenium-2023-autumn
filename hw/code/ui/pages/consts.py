from collections.abc import Mapping
from typing import List, NamedTuple

SCROLL_INTO_VIEW_JS_SCRIPT = "arguments[0].scrollIntoView(true);"
CHECKED_JS_SCRIPT = "return arguments[0].checked"
JS_CLICK = "arguments[0].click();"

AUTH_COOKIE_NAME = "remixsid"

SPAN = "span"
DIV = "div"
INPUT = "input"
H2 = "h2"
HREF = "href"
HOVER = "hover"


# Main page and navbar
class NavbarStudyTabsTitles:
    USEFULL_MATERIALS = "Полезные материалы"
    EVENTS = "Мероприятия"
    COURSES = "Видеокурсы"
    SERTIFICATION = "Сертификация"


class NavbarTabsTitles:
    NEWS = "Новости"
    STUDY = "Обучение"
    STUDY_DROPDOWN = NavbarStudyTabsTitles
    CASES = "Кейсы"
    IDEAS_FORUM = "Форум идей"
    MONETISATION = "Монетизация"
    HELP = "Справка"


class MainPageExternalLinks:
    COURSES_URL = "https://expert.vk.com/catalog/courses/"
    SERTIFICATION_URL = "https://expert.vk.com/certification/"


MainPageNavigationClass = "Navigation"


# Audience
AUDIENCE_USER_LIST_URL = "https://ads.vk.com/hq/audience/user_lists"


# Center of commerce
class CenterOfCommerceTabs:
    FEED = "feed"
    MARKETPLACE = "marketplace"
    MANUAL = "manual"


class CatalogPeriods:
    EVERYDAY = "everyday"
    ONE_HOUR = "1 hour"
    FOUR_HOURS = "4 hours"
    EIGHT_HOURS = "8 hours"

class NoSuchCatalogTabException(Exception):
    pass

class CatalogTabs(Mapping):
    PRODUCTS = "Товары"
    GROUPS = "Группы"
    DIAGNOSTIC = "Диагностика"
    EVENTS = "События"
    DOWNLOADS_HISTORY = "История загрузок"

    def __class_getitem__(cls, catalog):
        match catalog:
            case CatalogTabs.PRODUCTS:
                return "tab_catalogs.catalogMain"
            case CatalogTabs.GROUPS:
                return "tab_catalogs.catalogMain.catalogGroups"
            case CatalogTabs.EVENTS:
                return "tab_catalogs.catalogMain.catalogEvents"
            case CatalogTabs.DOWNLOADS_HISTORY:
                return "tab_catalogs.catalogMain.catalogHistory"
            case CatalogTabs.DIAGNOSTIC:
                return "tab_catalogs.catalogMain.catalogDiagnostics"
            case _:
                raise NoSuchCatalogTabException()

PRODUCTS_TAB_ID = "tab_catalogs.catalogMain"

CATALOG_TITLE_PREFIX = "Товары – "

class Catalog(NamedTuple):
    tab: str
    url: str
    title: str

CatalogsToBeCreated: List[Catalog] = [Catalog(tab, url, title) for tab, url, title in [
    (CenterOfCommerceTabs.FEED, "https://vk.com/luxvisage_cosmetics", "fff"),
    (CenterOfCommerceTabs.FEED, "https://vk.com/market-204475787", "dddsdsd"),
    (CenterOfCommerceTabs.FEED, "https://vk.com/voentorg_chipok", "Тачки"),
]]

class Product(NamedTuple):
    product_id: int
    title: str

CosmeticProducts = [Product(8005304, "Тени для век Glam Look матовые, палетка"), 
                    Product(8008361, "Лак для ногтей GEL SHINE перламутровый"),
                    Product(8699561, "Подарочный набор декоративной косметики Beauty Box №6"),
                    Product(8013293, "Жидкость для снятия лака без ацетона с витамином F"),
                    Product(8008361, "Лак для ногтей GEL SHINE перламутровый")]

TopCosmeticProduct = Product(8002726, "Лак для ногтей GEL SHINE перламутровый")

class MarketPlaceApiInput:
    TOKEN = "Введите токен для доступа к API"
    KEY = "Введите ключ API"


CENTER_OF_COMMERCE_TABLE_SETTINGS = "Настройка таблицы"
CENTER_OF_COMMERCE_CLIENT_ID_INPUT_TXT = "Введите Client ID"
CENTER_OF_COMMERCE_VK_PRODUCT_HREF = "https://vk.com/market"

INVALID_API_KEY_ERROR = "Указан неверный ключ"
INVALID_API_KEY_ENCODING_ERROR = "String is not compatible with encoding"
WARNING_PROTOCOL_REQUIRED = "Необходимо указать протокол http(s)"
REQUIRED_FIELD = "Обязательное поле"
NEW_CATALOG_TITLE = "Новый каталог"

INVALID_MARKETPLACE_URL = "Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе"

TEST_FILE_ADV_PAGE_NAME = "test.jpg"

SEARCH_PRODUCT_CLASS = "Toolbar_search__Fva6"
SEARCH_CATALOG_CLASS = "Nav_selectorSearch__QXVrQ"
TITLE_CLASS = "vkuiHeadline"
CONTENT_CLASS = "vkuiHeader__content-in"

# Group adv page
GROUP_ADV_INVALID_UTM = "Неверный формат utm-метки"


# LK Page
class SidebarTabsTitles:
    COMPANIES = "Кампании"
    AUDITORIES = "Аудитории"
    BUDGET = "Бюджет"
    LEARNING = "Обучение"
    CENTER_OF_COMMERCE = "Центр коммерции"
    SITES = "Сайты"
    MOBILE_APPS = "Мобильные приложения"
    LEAD_FORMS = "Лид-формы"
    SETTINGS = "Настройки"
    HELP = "Помощь"
PLACE = "Россия"


class WaitTime:
    SUPER_LONG_WAIT = 50
    LONG_WAIT = 20
    MEDIUM_WAIT = 10
    SHORT_WAIT = 5
    SUPER_SHORT_WAIT = 1


class BASE_POSITIONS:
    first_search_pos = 0
    last_search_pos = -1


class POSITIONS_ADV:
    title_position = 0
    continue_button = 1


class POSITIONS_GROUP:
    bottom_age = 0
    upper_age = 1

    continue_btn = 1
    save_btn = 0

    interest_region = 0
    key_phrase_minus_input = 1

    utm = 1
    checkbox = 1


class POSITIONS_SITE:
    category_event = 0
    event_condition = 1

    text_url_pos = 1

    delete_btn_pop_up = 1
    delete_modal_btn = 1


class POSITIONS_AUDIENCE:
    from_input_days = 0
    to_input_days = 1

    save_button_modal = 1
    user_list = 1

    delete_source_btn = 1
    filter_btn = 2

    period_pos = 0
    delete_confirm_btn = 1
    delete_btn_pop_up = 2


class URLS:
    banned_url = "https://labudiduba.com/"
    redirect_url_err = "Ссылка содержит запрещённый редирект на домен"

    correct_url_text = "https://vk.com/"
    vk_group_url = "vk.com/vkeducation"
    vk_group_incorrect_url = "https://vk.com/sweetmarin"

    bad_url = "adbbbsabasb"
    test_site = "ababababba.com"
    domen_vk_link = "vk.com"

    ad_plan_url = "https://ads.vk.com/hq/new_create/ad_plan"
    ad_groups_url = "https://ads.vk.com/hq/dashboard/ad_groups"
    ads_url = "https://ads.vk.com/hq/dashboard/ads"

    new_ad = "https://ads.vk.com/hq/new_create/ad_plan"
    site_url = "https://ads.vk.com/hq/pixels"
    audience_url = "https://ads.vk.com/hq/audience"
    company_url = "https://ads.vk.com/hq/dashboard/ad_plans?mode=ads&attribution=impression&sort=-created"
    lead_url = "https://ads.vk.com/hq/leadads/leadforms"

    base_url = "https://ads.vk.com"


class ERR_TEXT:
    latin_err_text = "Используйте латиницу только там, где без неё не обойтись"
    len_err_text = "Превышена максимальная длина поля"

    err_text = "ошибк"

    len_err_auditory = "Максимальная длина 255 символов"
    duplication_err = "У вас дублируются"

    incorrect_value_err = "Недопустимое значение переменной"
    empty_field_err = "Поле не должно быть пустым"

    len_err_site = "Максимальное количество символов - 255"
    validation_failed = "validation_failed"


class INPUT_TEXT:
    text_to_max_size = "слово"

    big_value_for_days = 10
    small_value_for_days = 5

    string_256_symbols = "a"*256

    min_period = 1
    less_than_min_period = 0
    max_period = 30
    more_than_max_period = 9999

    key_phrase_text = "строка1"
    long_key_phrase_text = key_phrase_text * 71

    max_age = 16
    min_age = 15

    less_than_need_cost = 22
    empty_value = ""
    corrected_cost = 200

    incorrect_input_collection_data = "привет"
    lead_info: str = "asdfawfafwafaw"
    URL_OPTIONS_LEN = 3

    title_text = "word"


class LABELS:
    create_auditory_text = "Создание аудитории"

    date_sum = "Отчёт по датам"
    config_table = "Настроить столбцы"

    nothing_found = "Ничего не нашлось"
    create_first = "Создайте первую рекламную кампанию"
    show_regions = 'Регионы показа'
    pixel_found = "Нашли пиксели"

    preview = "Предпросмотр"


class CLASSES:
    pop_down = "vkuiCustomSelect--pop-down"
    disabled_selector = "vkuiFormField--disabled"


GLOBAL_ACTIONS_DURATION = 20


def get_events_url(pixel_id):
    return f"https://ads.vk.com/hq/pixels/{pixel_id}/events"


def get_tags_url(pixel_id):
    return f"https://ads.vk.com/hq/pixels/{pixel_id}/tags"


def get_access_url(pixel_id):
    return f"https://ads.vk.com/hq/pixels/{pixel_id}/pixel_access"


def get_count_string(cnt: int):
    return f"Итого: {cnt}"


def get_screenshots_path(name_of_test):
    return f"screenshots/fail_{name_of_test}.png"
