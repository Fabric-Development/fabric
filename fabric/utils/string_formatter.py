class FormatDict(dict):
    def __init__(self, *args, **kwargs):
        super(FormatDict, self).__init__(*args, **kwargs)

    def __missing__(self, key):
        # FIXME: Future me. Fix this. Please.
        try:
            locals().update(self)
            global form_key
            form_key = key
            exec(f"global form_key\nform_key = {form_key}", globals(), locals())
        except Exception as e:
            form_key = form_key.join("{}")
        return form_key


def format(string: str, **kwargs) -> str:
    """
    kind of an advanced python string formatter.

    you can pass anything as long as it will work with f strings

    example usage in a nutshell:
    ```python
    >>> format("this is a {name}, supports {'advanced expressions' + ('!' * 5)}", name="string formatter")
    'this is a string formatter, supports advanced expressions!!!!'
    ```
    ### Powerful tip
    you can pass a function to the formatter, this will take the heavy lifting for you.

    ## NOTE
    `self` is not available in the scope of the formatter.
    """
    d = FormatDict(kwargs)
    return string.format_map(d)


class FormattedString:
    def __init__(self, string: str, **kwargs) -> None:
        self.string = string
        self.format_map = kwargs

    def get_formatted(self, **kwargs) -> str:
        return format(self.string, **(self.format_map | kwargs))
