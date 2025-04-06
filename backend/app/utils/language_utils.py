SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "zh": "Chinese",
    "ja": "Japanese",
    "ru": "Russian",
    "ar": "Arabic",
    "pt": "Portuguese"
}

def is_supported(lang_code: str) -> bool:
    return lang_code in SUPPORTED_LANGUAGES

def get_language_name(lang_code: str) -> str:
    return SUPPORTED_LANGUAGES.get(lang_code, "Unknown")
