from selenium.webdriver.common.by import By


class CenterOfCommerceLocators:
    # creation features
    START_CREATING_CATALOG = (
        By.XPATH,
        "//button[contains(@data-testid, 'create-catalog')]",
    )
    CATALOG_CREATE_BUTTON = (
        By.XPATH,
        '//button[@title="Создать каталог"]',
    )

    # catalogs page
    SEARCH_CATALOG_FIELD = (
        By.XPATH,
        "//input[contains(@data-testid, 'search')]",
    )

    # catalog page
    CATALOG = (By.XPATH, "//button[contains(@data-testid, 'current-catalog')]")

    # creation catalog modal

    FEED_TAB = (
        By.XPATH,
        "//div[contains(@data-testid, 'catalog-source_type-select') and contains(@data-entityid, 'url')]",
    )
    MARKET_TAB = (
        By.XPATH,
        "//div[contains(@data-testid, 'catalog-source_type-select') and contains(@data-entityid, 'marketplace')]",
    )
    MANUAL_TAB = (
        By.XPATH,
        "//div[contains(@data-testid, 'catalog-source_type-select') and contains(@data-entityid, 'file')]",
    )
    CATALOG_TITLE_INPUT = (
        By.XPATH,
        "//input[contains(@data-testid, 'catalogName-input')]",
    )
    CATALOG_URL_UNPUT = (
        By.XPATH,
        "//input[contains(@data-testid, 'catalogUrl-input')]",
    )
    CATALOG_PERIOD_SELECT = (
        By.XPATH,
        "//span[contains(@data-testid, 'catalogPeriod-select')]",
    )
    CATALOG_SELECT_TITLE = (By.CLASS_NAME, "vkuiSelect__title")
    CATALOG_PERIOD_EVERYDAY = (By.XPATH, '//div[text()="Ежедневно"]')
    CATALOG_PERIOD_EVERYHOUR = (By.XPATH, '//div[text()="1 час"]')
    CATALOG_PERIOD_EVERY4HOURS = (By.XPATH, '//div[text()="4 часа"]')
    CATALOG_PERIOD_EVERY8HOURS = (By.XPATH, '//div[text()="8 часов"]')
    CATALOG_ERROR_WITH_MINIMUM_THREE_PRODUCTS = (
        By.CLASS_NAME,
        "formBanner_container__Y0PJ7",
    )
    CATALOG_CLEAR_UTM_CHECKBOX_OFF = (
        By.CLASS_NAME,
        "vkuiIcon--check_box_off_20",
    )
    CATALOG_CLEAR_UTM_CHECKBOX_ON = (
        By.CLASS_NAME,
        "vkuiIcon--check_box_on_20",
    )
    CATALOG_CLEAR_UTM_CHECKBOX = (By.CLASS_NAME, "vkuiVisuallyHiddenInput")
    CATALOG_CHECKBOX_UTM_LABEL = (
        By.XPATH,
        '//div/label[contains(@class, "vkuiTappable")]',
    )
    CATALOG_CATEGORY = lambda category: (
        By.XPATH,
        f'//div[contains(text(), "{category}") and @class="vkuiCustomSelectOption__children"]',
    )
    CATALOG_CATEGORY_ON_DOWNLOAD = lambda category: (
        By.XPATH,
        f'//span[contains(., "{category}") and @class="vkuiButton__content"]',
    )
    MANUAL_FILE_INPUT = (By.CLASS_NAME, "vkuiFile__input")
    FILE_DOWNLOADING_ERROR_NOTIFICATION = (
        By.CLASS_NAME,
        "Snackbar_text__pDXKB",
    )
    DOWNLOADED_FILE = (
        By.XPATH,
        '//header[contains(@title, ".xlsx") or contains(@title, ".csv")]',
    )

    # Каталог

    CATALOG_TABS = (By.CLASS_NAME, "vkuiTabs__in")
    FEED_DOWNLOADING = (By.XPATH, '//span[text() = "Загрузка фида"]')
    DOWNLOADING_HISTORY_ICON = (
        By.CLASS_NAME,
        "UpdateBannerInfo_bannerIcon__dds6O",
    )
    FEED_DOWNLOADING_ON_DIAGNOSTIC = (
        By.XPATH,
        '//h2[text() = "Фид загружается"]',
    )
    DOWNLOAD_FULL_REPORT_BUTTON = (
        By.XPATH,
        '//a[contains(., "Скачать полный отчёт")]',
    )
    ADD_PRODUCTS_BUTTON = (By.XPATH, '//button[contains(.,"Добавить товары")]')
    PROMOTE_BUTTON = (By.XPATH, '//a[contains(., "Рекламировать")]')
    CONNECT_DATA_SOURCE_BUTTON = (
        By.XPATH,
        '//button[contains(.,"Подключить источник данных")]',
    )
    TAB_WITH_EVENTS_NOT_ACCESSED_SOON_SVG = (
        By.CLASS_NAME,
        "vkuiIcon--hourglass_outline_56",
    )
    CREATE_GROUP_BUTTON = (By.XPATH, '//button[contains(.,"Создать группу")]')
    CHOOOSE_CATALOG = (By.CLASS_NAME, "vkuiIcon--chevron_down_outline_28")
    PRODUCT_CELL_ON_CATALOG_TABLE = lambda text: (
        By.XPATH,
        f'//span[contains(text(), "{text}") and contains(@class, "vkuiHeadline")]',
    )
    CATALOG_TITLE = lambda text: (
        By.XPATH,
        f'//div[contains(., "{text}") and contains(@data-testid, "current-catalog")]',
    )
    SEARCH_CATALOG_BY_CLASS = lambda class_name: (
        By.XPATH,
        f'//div[contains(@class, "{class_name}")]/div/label/input[@type= "search"]',
    )
    TAB_BY_ID = lambda id: (By.ID, id)
    COMPANY_SETTING = (
        By.XPATH,
        '//div[contains(., "Настройка кампании") and @data-testid="steps"]',
    )
    PRODUCTS_TABLE_SETTINGS_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "TableSettings_settingsButton__uz8xK")]',
    )
    H2_WITH_TEXT = lambda text: (By.XPATH, f'//h2[text() = "{text}"]')
    H1_WITH_TEXT = lambda text: (By.XPATH, f'//h1[text() = "{text}"]')
    PRODUCTS_SELECT_ALL_CHECKBOX = (
        By.XPATH,
        '//div[contains(@class, "BaseTable__header-cell")]/input',
    )
    PRODUCTS_SELECT_ALL_CHECKBOX_SVG = (
        By.XPATH,
        '//div[contains(@class, "BaseTable__header-cell")]/div/*',
    )
    SORT_INDICATOR_PRODUCT = (
        By.XPATH,
        '//div[contains(.,"Товар")]/div[contains(@class, "BaseTable__sort-indicator")]',
    )
    PRODUCT_TABLE_HEADER = (By.XPATH, '//div[text() = "Товар"]')
    WARNING_SVG = (By.XPATH, '//span[contains(text(), "предупреждение")]')
    PRODUCT_ID_SVG = lambda product_id: (
        By.XPATH,
        f'//span[contains(text(), "{product_id}")]',
    )
    CATALOG_CELL = lambda title: (
        By.XPATH,
        f'//div[contains(@class, "CatalogsTable_item__1fpKp") and contains(., "{title}")]//button',
    )
    CATALOG_CELL_MORE_ACTIONS = (
        By.XPATH,
        '//button[contains(@data-testid, "catalog-item-menu")]',
    )
