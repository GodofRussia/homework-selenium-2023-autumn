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


class WaitTime:
    LONG_WAIT = 20
    MEDIUM_WAIT = 10
    SHORT_WAIT = 5
    SUPER_SHORT_WAIT = 1


class INPUT_FILES:
    name_of_file_picture = "test.jpg"


class POSITIONS:
    first_search_pos = 0
    last_search_pos = -1

    start_days_lead_field_numb = 0
    end_days_lead_field_numb = 1

    save_btn_pos = 1
    user_list_pos = 1

    filter_btn_pos = 2
    event_condition_pos = 1
    text_url_pos_site_page = 1

    delete_option_pos = 1
    delete_button_pos = 1
    cont_btn_adv_page = 1


class URLS:
    user_url = "https://ads.vk.com/hq/audience/user_lists"

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


class LABELS:
    create_auditory_text = "Создание аудитории"

    date_sum = "Отчёт по датам"
    config_table = "Настроить столбцы"

    nothing_found = "Ничего не нашлось"
    create_first = "Создайте первую рекламную кампанию"
    show_regions = 'Регионы показа'
    pixel_found = "Нашли пиксели"


class CLASSES:
    pop_down = "vkuiCustomSelect--pop-down"
