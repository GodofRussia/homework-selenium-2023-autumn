SCROLL_INTO_VIEW_JS_SCRIPT = "arguments[0].scrollIntoView(true);"
CHECKED_JS_SCRIPT = "return arguments[0].checked"

AUTH_COOKIE_NAME = "remixnsid"

SPAN = "span"
DIV = "div"
INPUT = "input"
H2 = "h2"
HREF = "href"


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


class CatalogTabs:
    PRODUCTS = "Товары"
    GROUPS = "Группы"
    DIAGNOSTIC = "Диагностика"
    EVENTS = "События"
    DOWNLOADS_HISTORY = "История загрузок"


PRODUCTS_TAB_ID = "tab_catalogs.catalogMain"


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
