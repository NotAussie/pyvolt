import typing

Language = typing.Literal[
    # english
    'en',
    'en_US',
    # foreign languages
    'ar',
    'as',
    'az',
    'be',
    'bg',
    'bn',
    'br',
    'ca',
    'ceb',
    'ckb',
    'cs',
    'da',
    'de',
    'el',
    'es',
    'es_419',
    'et',
    'fi',
    'fil',
    'fr',
    'ga',
    'hi',
    'hr',
    'hu',
    'hy',
    'id',
    'is',
    'it',
    'ja',
    'ko',
    'lb',
    'lt',
    'mk',
    'ms',
    'nb_NO',
    'nl',
    'fa',
    'pl',
    'pt_BR',
    'pt_PT',
    'ro',
    'ru',
    'sk',
    'sl',
    'sq',
    'sr',
    'si',
    'sv',
    'ta',
    'th',
    'tr',
    'uk',
    'ur',
    'vec',
    'vi',
    'zh_Hans',
    'zh_Hant',
    'lv',
    # constructed languages
    'tokipona',
    'esperanto',
    # joke languages
    'owo',
    'pr',
    'bottom',
    'leet',
    'piglatin',
    'enchantment',
]

__all__ = ('Language',)