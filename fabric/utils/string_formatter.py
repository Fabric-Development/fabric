class ___FormatDict___(dict):
    def __init__(self, *args, **kwargs):
        super(___FormatDict___, self).__init__(*args, **kwargs)

    def __missing__(self, key):
        try:
            rkey = eval(key, globals(), self)
        except Exception as e:
            rkey = key.join("{}")
        return rkey


class FormattedString:
    """simple string fomatter made to be baked mid-runtime"""

    def __init__(self, string: str, **kwargs) -> None:
        self.__string__ = string
        self.__format_map__ = kwargs

    def __call__(self, **kwargs) -> str:
        return self.get_formatted(**kwargs)

    def get_formatted(self, **kwargs) -> str:
        return self.__string__.format_map(
            ___FormatDict___(**(self.__format_map__ | kwargs))
        )
