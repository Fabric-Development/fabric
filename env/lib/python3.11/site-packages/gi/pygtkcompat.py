import warnings

from gi import PyGIDeprecationWarning

warnings.warn('gi.pygtkcompat is being deprecated in favor of using "pygtkcompat" directly.',
              PyGIDeprecationWarning)

# pyflakes.ignore
from pygtkcompat import (enable,
                         enable_gtk,
                         enable_vte,
                         enable_poppler,
                         enable_webkit,
                         enable_gudev,
                         enable_gst,
                         enable_goocanvas)


__all__ = ['enable',
           'enable_gtk',
           'enable_vte',
           'enable_poppler',
           'enable_webkit',
           'enable_gudev',
           'enable_gst',
           'enable_goocanvas']
