from __future__ import annotations

from typing import (Any, BinaryIO, ByteString, Callable, Generic, List, Optional,
                    Sequence, Text, Tuple, TypeVar, Union)

del annotations

HAS_ATSUI_FONT: bool = ...
HAS_FT_FONT: bool = ...
HAS_GLITZ_SURFACE: bool = ...
HAS_IMAGE_SURFACE: bool = ...
HAS_MIME_SURFACE: bool = ...
"""
.. versionadded:: 1.12.0
"""
HAS_PDF_SURFACE: bool = ...
HAS_PNG_FUNCTIONS: bool = ...
HAS_PS_SURFACE: bool = ...
HAS_QUARTZ_SURFACE: bool = ...
HAS_RECORDING_SURFACE: bool = ...
HAS_SCRIPT_SURFACE: bool = ...
"""
.. versionadded:: 1.12.0
"""
HAS_SVG_SURFACE: bool = ...
HAS_TEE_SURFACE: bool = ...
"""
.. versionadded:: 1.15.3
"""
HAS_USER_FONT: bool = ...
HAS_WIN32_FONT: bool = ...
HAS_WIN32_SURFACE: bool = ...
HAS_XCB_SURFACE: bool = ...
HAS_XLIB_SURFACE: bool = ...
HAS_DWRITE_FONT: bool = ...
"""
.. versionadded:: 1.23.0
"""

PDF_OUTLINE_ROOT: int = ...
"""
The root outline item in :meth:`PDFSurface.add_outline`

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

COLOR_PALETTE_DEFAULT: int = ...
"""
The default color palette index. See :meth:`FontOptions.set_color_palette`

.. versionadded:: 1.25.0 Only available with cairo 1.17.8+
"""

version: str = ...
"""the pycairo version, as a string"""

version_info: Tuple[int, int, int] = ...
"""the pycairo version, as a tuple"""

CAIRO_VERSION: int = ...
"""
The version of cairo available at compile-time in the same format as
returned by :func:`cairo_version`

.. versionadded:: 1.18.0
"""

CAIRO_VERSION_STRING: str = ...
"""
A human-readable string literal containing the version of cairo available
at compile-time, in the form of "X.Y.Z".

.. versionadded:: 1.18.0
"""

CAIRO_VERSION_MAJOR: int = ...
"""
The major component of the version of cairo available at compile-time.

.. versionadded:: 1.18.0
"""

CAIRO_VERSION_MINOR: int = ...
"""
The minor component of the version of cairo available at compile-time.

.. versionadded:: 1.18.0
"""

CAIRO_VERSION_MICRO: int = ...
"""
The micro component of the version of cairo available at compile-time.

.. versionadded:: 1.18.0
"""

def cairo_version() -> int:
    """
    :returns: the encoded version

    Returns the version of the underlying C cairo library, encoded in a single
    integer.
    """

def cairo_version_string() -> str:
    """
    :returns: the encoded version

    Returns the version of the underlying C cairo library as a human-readable
    string of the form "X.Y.Z".
    """

class Path:
    """
    *Path* cannot be instantiated directly, it is created by calling
    :meth:`Context.copy_path` and :meth:`Context.copy_path_flat`.

    str(path) lists the path elements.

    See :class:`path attributes <cairo.PathDataType>`

    Path is an iterator.

    See examples/warpedtext.py for example usage.
    """

class Rectangle(Tuple[float, float, float, float]):
    """
    .. versionadded:: 1.15
        In prior versions a (float, float, float, float) tuple was
        used instead of :class:`Rectangle`.

    A data structure for holding a rectangle.
    """

    x: float = ...
    y: float = ...
    width: float = ...
    height: float = ...

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        :param x:
            X coordinate of the left side of the rectangle
        :param y:
            Y coordinate of the the top side of the rectangle
        :param width:
            width of the rectangle
        :param height:
            height of the rectangle
        """

class _IntEnum(int):
    def __init__(self, value: int) -> None: ...

class Antialias(_IntEnum):
    """
    Specifies the type of antialiasing to do when rendering text or shapes.

    .. versionadded:: 1.13
    """

    BEST: "Antialias" = ...
    """
    Hint that the backend should render at the highest quality, sacrificing
    speed if necessary.
    """

    DEFAULT: "Antialias" = ...
    """Use the default antialiasing for the subsystem and target device"""

    FAST: "Antialias" = ...
    """
    Hint that the backend should perform some antialiasing but prefer
    speed over quality.
    """

    GOOD: "Antialias" = ...
    """The backend should balance quality against performance."""

    GRAY: "Antialias" = ...
    """
    Perform single-color antialiasing (using shades of gray for black text
    on a white background, for example).
    """

    NONE: "Antialias" = ...
    """Use a bilevel alpha mask"""

    SUBPIXEL: "Antialias" = ...
    """
    Perform antialiasing by taking advantage of the order of subpixel
    elements on devices such as LCD panels.
    """

class Content(_IntEnum):
    """
    These constants are used to describe the content that a :class:`Surface`
    will contain, whether color information, alpha information (translucence
    vs. opacity), or both.

    .. versionadded:: 1.13
    """

    ALPHA: "Content" = ...
    """The surface will hold alpha content only."""

    COLOR: "Content" = ...
    """The surface will hold color content only."""

    COLOR_ALPHA: "Content" = ...
    """The surface will hold color and alpha content."""

class FillRule(_IntEnum):
    """
    These constants are used to select how paths are filled. For both fill
    rules, whether or not a point is included in the fill is determined by
    taking a ray from that point to infinity and looking at intersections with
    the path. The ray can be in any direction, as long as it doesn't pass
    through the end point of a segment or have a tricky intersection such as
    intersecting tangent to the path. (Note that filling is not actually
    implemented in this way. This is just a description of the rule that is
    applied.)

    The default fill rule is :attr:`WINDING`.

    .. versionadded:: 1.13
    """

    EVEN_ODD: "FillRule" = ...
    """
    Counts the total number of intersections, without regard to the
    orientation of the contour. If the total number of intersections is
    odd, the point will be filled.
    """

    WINDING: "FillRule" = ...
    """
    If the path crosses the ray from left-to-right, counts +1. If the path
    crosses the ray from right to left, counts -1. (Left and right are
    determined from the perspective of looking along the ray from the
    starting point.) If the total count is non-zero, the point will be
    filled.
    """

class Format(_IntEnum):
    """
    These constants are used to identify the memory format of
    :class:`ImageSurface` data.

    New entries may be added in future versions.

    .. versionadded:: 1.13
    """

    def stride_for_width(self, width: int) -> int:
        """
        :param width: the desired width of an :class:`ImageSurface`
            to be created.
        :returns: the appropriate stride to use given the desired format and
            width, or -1 if either the format is invalid or the width too
            large.

        This method provides a stride value that will respect all alignment
        requirements of the accelerated image-rendering code within cairo.
        Typical usage will be of the form::

            format = cairo.Format.RGB24
            stride = format.stride_for_width(width)
            surface = cairo.ImageSurface.create_for_data(
                data, format, width, height, stride)

        Also available under
        :meth:`cairo.ImageSurface.format_stride_for_width`.

        .. versionadded:: 1.14
        """

    A1: "Format" = ...
    """
    each pixel is a 1-bit quantity holding an alpha value. Pixels are
    packed together into 32-bit quantities. The ordering of the bits
    matches the endianess of the platform. On a big-endian machine, the
    first pixel is in the uppermost bit, on a little-endian machine the
    first pixel is in the least-significant bit.
    """

    A8: "Format" = ...
    """
    each pixel is a 8-bit quantity holding an alpha value.
    """

    ARGB32: "Format" = ...
    """
    each pixel is a 32-bit quantity, with alpha in the upper 8 bits, then
    red, then green, then blue. The 32-bit quantities are stored
    native-endian. Pre-multiplied alpha is used. (That is, 50% transparent
    red is 0x80800000, not 0x80ff0000.)
    """

    INVALID: "Format" = ...
    """no such format exists or is supported."""

    RGB16_565: "Format" = ...
    """
    each pixel is a 16-bit quantity with red in the upper 5 bits, then
    green in the middle 6 bits, and blue in the lower 5 bits.
    """

    RGB24: "Format" = ...
    """
    each pixel is a 32-bit quantity, with the upper 8 bits unused. [#]_  Red,
    Green, and Blue are stored in the remaining 24 bits in that order.

    .. [#] Cairo operators (for example CLEAR and SRC) may overwrite unused bytes as an implementation side-effect, their values should be considered undefined.
    """

    RGB30: "Format" = ...
    """
    like :data:`RGB24` but with 10bpc.
    """

    RGB96F: "Format" = ...
    """
    3 floats, R, G, B.

    .. versionadded:: 1.23 Only available with cairo 1.17.2+
    """

    RGBA128F: "Format" = ...
    """
    4 floats, R, G, B, A.

    .. versionadded:: 1.23 Only available with cairo 1.17.2+
    """

class HintMetrics(_IntEnum):
    """
    These constants specify whether to hint font metrics; hinting font metrics
    means quantizing them so that they are integer values in device space.
    Doing this improves the consistency of letter and line spacing, however it
    also means that text will be laid out differently at different zoom
    factors.

    .. versionadded:: 1.13
    """

    DEFAULT: "HintMetrics" = ...
    """
    Hint metrics in the default manner for the font backend and target
    device
    """

    OFF: "HintMetrics" = ...
    """"Do not hint font metrics"""

    ON: "HintMetrics" = ...
    """Hint font metrics"""

class ColorMode(_IntEnum):
    """
    Specifies if color fonts are to be rendered using the color glyphs or
    outline glyphs. Glyphs that do not have a color presentation, and non-color
    fonts are not affected by this font option.

    .. versionadded:: 1.25 Only available with cairo 1.17.8+
    """

    DEFAULT: "ColorMode" = ...
    """
    Use the default color mode for font backend and target device.
    """

    NO_COLOR: "ColorMode" = ...
    """
    Disable rendering color glyphs. Glyphs are always rendered as outline glyphs
    """

    COLOR: "ColorMode" = ...
    """
    Enable rendering color glyphs. If the font contains a color presentation for
    a glyph, and when supported by the font backend, the glyph will be rendered
    in color.
    """

class Dither(_IntEnum):
    """
    Dither is an intentionally applied form of noise used to randomize
    quantization error, preventing large-scale patterns such as color banding in
    images (e.g. for gradients). Ordered dithering applies a precomputed
    threshold matrix to spread the errors smoothly.

    :class:`Dither` is modeled on pixman dithering algorithm choice. As of
    Pixman 0.40, FAST corresponds to a 8x8 ordered bayer noise and GOOD and BEST
    use an ordered 64x64 precomputed blue noise.

    .. versionadded:: 1.25 Only available with cairo 1.18.0+
    """

    NONE: "Dither" = ...
    """
    No dithering.
    """

    DEFAULT: "Dither" = ...
    """
    Default choice at cairo compile time. Currently NONE.
    """

    FAST: "Dither" = ...
    """
    Fastest dithering algorithm supported by the backend
    """

    GOOD: "Dither" = ...
    """
    An algorithm with smoother dithering than FAST
    """

    BEST: "Dither" = ...
    """
    Best algorithm available in the backend
    """

class HintStyle(_IntEnum):
    """
    These constants specify the type of hinting to do on font outlines.
    Hinting is the process of fitting outlines to the pixel grid in order to
    improve the appearance of the result. Since hinting outlines involves
    distorting them, it also reduces the faithfulness to the original outline
    shapes. Not all of the outline hinting styles are supported by all font
    backends.

    New entries may be added in future versions.

    .. versionadded:: 1.13
    """

    DEFAULT: "HintStyle" = ...
    """
    Use the default hint style for font backend and target device
    """

    FULL: "HintStyle" = ...
    """
    Hint outlines to maximize contrast
    """

    MEDIUM: "HintStyle" = ...
    """
    Hint outlines with medium strength giving a compromise between fidelity
    to the original shapes and contrast
    """

    NONE: "HintStyle" = ...
    """Do not hint outlines"""

    SLIGHT: "HintStyle" = ...
    """
    Hint outlines slightly to improve contrast while retaining good
    fidelity to the original shapes.
    """

class SubpixelOrder(_IntEnum):
    """
    The subpixel order specifies the order of color elements within each pixel
    on the display device when rendering with an antialiasing mode of
    :attr:`Antialias.SUBPIXEL`.

    .. versionadded:: 1.13
    """

    BGR: "SubpixelOrder" = ...
    """Subpixel elements are arranged horizontally with blue at the left"""

    DEFAULT: "SubpixelOrder" = ...
    """Use the default subpixel order for for the target device"""

    RGB: "SubpixelOrder" = ...
    """Subpixel elements are arranged horizontally with red at the left"""

    VBGR: "SubpixelOrder" = ...
    """Subpixel elements are arranged vertically with blue at the top"""

    VRGB: "SubpixelOrder" = ...
    """Subpixel elements are arranged vertically with red at the top"""

class LineCap(_IntEnum):
    """
    These constants specify how to render the endpoints of the path when
    stroking.

    The default line cap style is :attr:`BUTT`

    .. versionadded:: 1.13
    """

    BUTT: "LineCap" = ...
    """start(stop) the line exactly at the start(end) point"""

    ROUND: "LineCap" = ...
    """use a round ending, the center of the circle is the end point"""

    SQUARE: "LineCap" = ...
    """use squared ending, the center of the square is the end point"""

class LineJoin(_IntEnum):
    """
    These constants specify how to render the junction of two lines when
    stroking.

    The default line join style is :attr:`MITER`

    .. versionadded:: 1.13
    """

    BEVEL: "LineJoin" = ...
    """
    use a cut-off join, the join is cut off at half the line width from
    the joint point
    """

    MITER: "LineJoin" = ...
    """
    use a sharp (angled) corner, see :meth:`Context.set_miter_limit`
    """

    ROUND: "LineJoin" = ...
    """use a rounded join, the center of the circle is the joint point"""

class Filter(_IntEnum):
    """
    These constants are used to indicate what filtering should be applied when
    reading pixel values from patterns. See :meth:`Pattern.set_filter` for
    indicating the desired filter to be used with a particular pattern.

    .. versionadded:: 1.13
    """

    BEST: "Filter" = ...
    """
    The highest-quality available, performance may not be suitable for
    interactive use.
    """

    BILINEAR: "Filter" = ...
    """Linear interpolation in two dimensions"""

    FAST: "Filter" = ...
    """A high-performance filter, with quality similar *FILTER_NEAREST*"""

    GAUSSIAN: "Filter" = ...
    """
    This filter value is currently unimplemented, and should not be used
    in current code.
    """

    GOOD: "Filter" = ...
    """
    A reasonable-performance filter, with quality similar to
    *FILTER_BILINEAR*
    """

    NEAREST: "Filter" = ...
    """Nearest-neighbor filtering"""

class Operator(_IntEnum):
    """
    These constants are used to set the compositing operator for all cairo
    drawing operations.

    The default operator is :attr:`OVER`.

    The operators marked as *unbounded* modify their destination even outside
    of the mask layer (that is, their effect is not bound by the mask layer).
    However, their effect can still be limited by way of clipping.

    To keep things simple, the operator descriptions here document the
    behavior for when both source and destination are either fully transparent
    or fully opaque.  The actual implementation works for translucent layers
    too.

    For a more detailed explanation of the effects of each operator, including
    the mathematical definitions, see https://cairographics.org/operators.

    .. versionadded:: 1.13
    """

    ADD: "Operator" = ...
    """source and destination layers are accumulated"""

    ATOP: "Operator" = ...
    """draw source on top of destination content and only there"""

    CLEAR: "Operator" = ...
    """clear destination layer (bounded)"""

    COLOR_BURN: "Operator" = ...
    """darkens the destination color to reflect the source color."""

    COLOR_DODGE: "Operator" = ...
    """brightens the destination color to reflect the source color."""

    DARKEN: "Operator" = ...
    """
    replaces the destination with the source if it is darker, otherwise
    keeps the source.
    """

    DEST: "Operator" = ...
    """ignore the source"""

    DEST_ATOP: "Operator" = ...
    """leave destination on top of source content and only there (unbounded)"""

    DEST_IN: "Operator" = ...
    """leave destination only where there was source content (unbounded)"""

    DEST_OUT: "Operator" = ...
    """leave destination only where there was no source content"""

    DEST_OVER: "Operator" = ...
    """draw destination on top of source"""

    DIFFERENCE: "Operator" = ...
    """Takes the difference of the source and destination color."""

    EXCLUSION: "Operator" = ...
    """Produces an effect similar to difference, but with lower contrast."""

    HARD_LIGHT: "Operator" = ...
    """Multiplies or screens, dependent on source color."""

    HSL_COLOR: "Operator" = ...
    """
    Creates a color with the hue and saturation of the source and the
    luminosity of the target. This preserves the gray levels of the target
    and is useful for coloring monochrome images or tinting color images.
    """

    HSL_HUE: "Operator" = ...
    """
    Creates a color with the hue of the source and the saturation and
    luminosity of the target.
    """

    HSL_LUMINOSITY: "Operator" = ...
    """
    Creates a color with the luminosity of the source and the hue and
    saturation of the target. This produces an inverse effect to
    :attr:`HSL_COLOR`
    """

    HSL_SATURATION: "Operator" = ...
    """
    Creates a color with the saturation of the source and the hue and
    luminosity of the target. Painting with this mode onto a gray area
    produces no change.
    """

    IN: "Operator" = ...
    """draw source where there was destination content (unbounded)"""

    LIGHTEN: "Operator" = ...
    """
    replaces the destination with the source if it is lighter, otherwise
    keeps the source.
    """

    MULTIPLY: "Operator" = ...
    """
    source and destination layers are multiplied. This causes the result
    to be at least as dark as the darker inputs.
    """

    OUT: "Operator" = ...
    """draw source where there was no destination content (unbounded)"""

    OVER: "Operator" = ...
    """draw source layer on top of destination layer (bounded)"""

    OVERLAY: "Operator" = ...
    """
    multiplies or screens, depending on the lightness of the destination
    color.
    """

    SATURATE: "Operator" = ...
    """like over, but assuming source and dest are disjoint geometries"""

    SCREEN: "Operator" = ...
    """
    source and destination are complemented and multiplied. This causes
    the result to be at least as light as the lighter inputs.
    """

    SOFT_LIGHT: "Operator" = ...
    """Darkens or lightens, dependent on source color."""

    SOURCE: "Operator" = ...
    """replace destination layer (bounded)"""

    XOR: "Operator" = ...
    """source and destination are shown where there is only one of them"""

class Extend(_IntEnum):
    """
    These constants are used to describe how :class:`Pattern` color/alpha will
    be determined for areas "outside" the pattern's natural area, (for
    example, outside the surface bounds or outside the gradient geometry).

    The default extend mode is :attr:`NONE` for :class:`SurfacePattern` and
    :attr:`PAD` for :class:`Gradient` patterns.

    .. versionadded:: 1.13
    """

    NONE: "Extend" = ...
    """pixels outside of the source pattern are fully transparent"""

    PAD: "Extend" = ...
    """
    pixels outside of the pattern copy the closest pixel from the source
    (Since 1.2; but only implemented for surface patterns since 1.6)
    """

    REFLECT: "Extend" = ...
    """
    the pattern is tiled by reflecting at the edges (Implemented for
    surface patterns since 1.6)
    """

    REPEAT: "Extend" = ...
    """the pattern is tiled by repeating"""

class FontSlant(_IntEnum):
    """
    These constants specify variants of a :class:`FontFace` based on their
    slant.

    .. versionadded:: 1.13
    """

    ITALIC: "FontSlant" = ...
    """Italic font style"""

    NORMAL: "FontSlant" = ...
    """Upright font style"""

    OBLIQUE: "FontSlant" = ...
    """Oblique font style"""

class FontWeight(_IntEnum):
    """
    These constants specify variants of a :class:`FontFace` based on their
    weight.

    .. versionadded:: 1.13
    """

    BOLD: "FontWeight" = ...
    """Bold font weight"""

    NORMAL: "FontWeight" = ...
    """Normal font weight"""

class Status(_IntEnum):
    """
    .. versionadded:: 1.13
    """

    CLIP_NOT_REPRESENTABLE: "Status" = ...
    DEVICE_ERROR: "Status" = ...
    DEVICE_FINISHED: "Status" = ...
    DEVICE_TYPE_MISMATCH: "Status" = ...
    FILE_NOT_FOUND: "Status" = ...
    FONT_TYPE_MISMATCH: "Status" = ...
    INVALID_CLUSTERS: "Status" = ...
    INVALID_CONTENT: "Status" = ...
    INVALID_DASH: "Status" = ...
    INVALID_DSC_COMMENT: "Status" = ...
    INVALID_FORMAT: "Status" = ...
    INVALID_INDEX: "Status" = ...
    INVALID_MATRIX: "Status" = ...
    INVALID_MESH_CONSTRUCTION: "Status" = ...
    INVALID_PATH_DATA: "Status" = ...
    INVALID_POP_GROUP: "Status" = ...
    INVALID_RESTORE: "Status" = ...
    INVALID_SIZE: "Status" = ...
    INVALID_SLANT: "Status" = ...
    INVALID_STATUS: "Status" = ...
    INVALID_STRIDE: "Status" = ...
    INVALID_STRING: "Status" = ...
    INVALID_VISUAL: "Status" = ...
    INVALID_WEIGHT: "Status" = ...
    JBIG2_GLOBAL_MISSING: "Status" = ...
    """
    .. versionadded:: 1.14
    """
    LAST_STATUS: "Status" = ...
    NEGATIVE_COUNT: "Status" = ...
    NO_CURRENT_POINT: "Status" = ...
    NO_MEMORY: "Status" = ...
    NULL_POINTER: "Status" = ...
    PATTERN_TYPE_MISMATCH: "Status" = ...
    READ_ERROR: "Status" = ...
    SUCCESS: "Status" = ...
    SURFACE_FINISHED: "Status" = ...
    SURFACE_TYPE_MISMATCH: "Status" = ...
    TEMP_FILE_ERROR: "Status" = ...
    USER_FONT_ERROR: "Status" = ...
    USER_FONT_IMMUTABLE: "Status" = ...
    USER_FONT_NOT_IMPLEMENTED: "Status" = ...
    WRITE_ERROR: "Status" = ...
    TAG_ERROR: "Status" = ...
    """
    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """
    FREETYPE_ERROR: "Status" = ...
    """
    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """
    PNG_ERROR: "Status" = ...
    """
    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """
    WIN32_GDI_ERROR: "Status" = ...
    """
    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """
    DWRITE_ERROR: "Status" = ...
    """
    .. versionadded:: 1.23.0 Only available with cairo 1.17.6+
    """
    SVG_FONT_ERROR: "Status" = ...
    """
    .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
    """

class PDFVersion(_IntEnum):
    """
    These constants are used to describe the version number of the PDF
    specification that a generated PDF file will conform to.

    .. versionadded:: 1.13
    """

    VERSION_1_4: "PDFVersion" = ...
    """The version 1.4 of the PDF specification."""

    VERSION_1_5: "PDFVersion" = ...
    """The version 1.5 of the PDF specification."""

    VERSION_1_6: "PDFVersion" = ...
    """
    The version 1.6 of the PDF specification.

    .. versionadded:: 1.23.0 Only available with cairo 1.17.6+
    """

    VERSION_1_7: "PDFVersion" = ...
    """
    The version 1.7 of the PDF specification.

    .. versionadded:: 1.23.0 Only available with cairo 1.17.6+
    """

class PSLevel(_IntEnum):
    """
    These constants are used to describe the language level of the PostScript
    Language Reference that a generated PostScript file will conform to.
    Note: the constants are only defined when cairo has been compiled with PS
    support enabled.

    .. versionadded:: 1.13
    """

    LEVEL_2: "PSLevel" = ...
    """The language level 2 of the PostScript specification."""

    LEVEL_3: "PSLevel" = ...
    """The language level 3 of the PostScript specification."""

class PathDataType(_IntEnum):
    """
    These constants are used to describe the type of one portion of a path
    when represented as a :class:`Path`.

    .. versionadded:: 1.13
    """

    CLOSE_PATH: "PathDataType" = ...
    """A close-path operation"""

    CURVE_TO: "PathDataType" = ...
    """A curve-to operation"""

    LINE_TO: "PathDataType" = ...
    """ A line-to operation"""

    MOVE_TO: "PathDataType" = ...
    """A move-to operation"""

class RegionOverlap(_IntEnum):
    """
    .. versionadded:: 1.13
    """

    IN: "RegionOverlap" = ...
    """The contents are entirely inside the region."""

    OUT: "RegionOverlap" = ...
    """The contents are entirely outside the region."""

    PART: "RegionOverlap" = ...
    """The contents are partially inside and partially outside the region."""

class SVGVersion(_IntEnum):
    """
    These constants are used to describe the version number of the SVG
    specification that a generated SVG file will conform to.

    .. versionadded:: 1.13
    """

    VERSION_1_1: "SVGVersion" = ...
    """The version 1.1 of the SVG specification."""

    VERSION_1_2: "SVGVersion" = ...
    """The version 1.2 of the SVG specification."""

class SVGUnit(_IntEnum):
    """
    :class:`SVGUnit` is used to describe the units valid for coordinates and
    lengths in the SVG specification.

    See also:

    * https://www.w3.org/TR/SVG/coords.htmlUnits
    * https://www.w3.org/TR/SVG/types.htmlDataTypeLength
    * https://www.w3.org/TR/css-values-3/lengths

    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """

    USER: "SVGUnit" = ...
    """
    User unit, a value in the current coordinate system. If used in the
    root element for the initial coordinate systems it corresponds to
    pixels.
    """

    EM: "SVGUnit" = ...
    """The size of the element's font."""

    EX: "SVGUnit" = ...
    """The x-height of the element’s font."""

    PX: "SVGUnit" = ...
    """Pixels (1px = 1/96th of 1in)."""

    IN: "SVGUnit" = ...
    """Inches (1in = 2.54cm = 96px)"""

    CM: "SVGUnit" = ...
    """Centimeters (1cm = 96px/2.54)."""

    MM: "SVGUnit" = ...
    """Millimeters (1mm = 1/10th of 1cm)."""

    PT: "SVGUnit" = ...
    """Points (1pt = 1/72th of 1in)."""

    PC: "SVGUnit" = ...
    """Picas (1pc = 1/6th of 1in)."""

    PERCENT: "SVGUnit" = ...
    """Percent, a value that is some fraction of another reference value."""

class PDFMetadata(_IntEnum):
    """
    :class:`PDFMetadata` is used by the :meth:`PDFSurface.set_metadata` method
    to specify the metadata to set.

    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """

    TITLE: "PDFMetadata" = ...
    """The document title"""

    AUTHOR: "PDFMetadata" = ...
    """The document author"""

    SUBJECT: "PDFMetadata" = ...
    """The document subject"""

    KEYWORDS: "PDFMetadata" = ...
    """The document keywords"""

    CREATOR: "PDFMetadata" = ...
    """The document creator"""

    CREATE_DATE: "PDFMetadata" = ...
    """The document creation date"""

    MOD_DATE: "PDFMetadata" = ...
    """The document modification date"""

class PDFOutlineFlags(_IntEnum):
    """
    :class:`PDFOutlineFlags` is used by the :meth:`PDFSurface.add_outline`
    method to specify the attributes of an outline item. These flags may be
    bitwise-or'd to produce any combination of flags.

    .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
    """

    OPEN: "PDFOutlineFlags" = ...
    """The outline item defaults to open in the PDF viewer"""

    BOLD: "PDFOutlineFlags" = ...
    """The outline item is displayed by the viewer in bold text"""

    ITALIC: "PDFOutlineFlags" = ...
    """The outline item is displayed by the viewer in italic text"""

class ScriptMode(_IntEnum):
    """
    A set of script output variants.

    .. versionadded:: 1.14
    """

    ASCII: "ScriptMode" = ...
    """the output will be in readable text (default)"""

    BINARY: "ScriptMode" = ...
    """the output will use byte codes."""

class Matrix:
    """
    *Matrix* is used throughout cairo to convert between different coordinate
    spaces.  A *Matrix* holds an affine transformation, such as a scale,
    rotation, shear, or a combination of these.  The transformation of a point
    (x,y) is given by::

        x_new = xx * x + xy * y + x0
        y_new = yx * x + yy * y + y0

    The current transformation matrix of a :class:`Context`, represented as a
    *Matrix*, defines the transformation from user-space coordinates to
    device-space coordinates.

    Some standard Python operators can be used with matrices:

    To read the values from a *Matrix*::

        xx, yx, xy, yy, x0, y0 = matrix

    To multiply two matrices::

        matrix3 = matrix1.multiply(matrix2)
        # or equivalently
        matrix3 = matrix1 * matrix2

    To compare two matrices::

        matrix1 == matrix2
        matrix1 != matrix2

    For more information on matrix transformation see
    https://www.cairographics.org/cookbook/matrix_transform/
    """

    def __init__(self, xx: float = 1.0, yx: float = 0.0, xy: float = 0.0, yy: float = 1.0, x0: float = 0.0, y0: float = 0.0) -> None:
        """
        :param xx: xx component of the affine transformation
        :param yx: yx component of the affine transformation
        :param xy: xy component of the affine transformation
        :param yy: yy component of the affine transformation
        :param x0: X translation component of the affine transformation
        :param y0: Y translation component of the affine transformation

        Create a new *Matrix* with the affine transformation given by *xx, yx,
        xy, yy, x0, y0*. The transformation is given by::

            x_new = xx * x + xy * y + x0
            y_new = yx * x + yy * y + y0

        To create a new identity matrix::

            matrix = cairo.Matrix()

        To create a matrix with a transformation which translates by tx and ty
        in the X and Y dimensions, respectively::

            matrix = cairo.Matrix(x0=tx, y0=ty)

        To create a matrix with a transformation that scales by sx and sy in the
        X and Y dimensions, respectively::

            matrix = cairo.Matrix(xx=sy, yy=sy)
        """

    @classmethod
    def init_rotate(cls, radians: float) -> "Matrix":
        """
        :param radians: angle of rotation, in radians. The direction of rotation
            is defined such that positive angles rotate in the direction from the
            positive X axis toward the positive Y axis. With the default axis
            orientation of cairo, positive angles rotate in a clockwise direction.
        :returns: a new *Matrix* set to a transformation that rotates by *radians*.
        """

    def invert(self) -> Optional["Matrix"]:
        """
        :returns: If *Matrix* has an inverse, modifies *Matrix* to be the
            inverse matrix and returns *None*
        :raises: :exc:`cairo.Error` if the *Matrix* as no inverse

        Changes *Matrix* to be the inverse of it's original value. Not all
        transformation matrices have inverses; if the matrix collapses points
        together (it is *degenerate*), then it has no inverse and this function
        will fail.
        """

    def multiply(self, matrix2: "Matrix") -> "Matrix":
        """
        :param matrix2: a second matrix
        :returns: a new *Matrix*

        Multiplies the affine transformations in *Matrix* and *matrix2*
        together. The effect of the resulting transformation is to first apply
        the transformation in *Matrix* to the coordinates and then apply the
        transformation in *matrix2* to the coordinates.

        It is allowable for result to be identical to either *Matrix* or *matrix2*.
        """

    def rotate(self, radians: float) -> None:
        """
        :param radians: angle of rotation, in radians. The direction of rotation
            is defined such that positive angles rotate in the direction from the
            positive X axis toward the positive Y axis. With the default axis
            orientation of cairo, positive angles rotate in a clockwise direction.

        Initialize *Matrix* to a transformation that rotates by *radians*.
        """

    def scale(self, sx: float, sy: float) -> None:
        """
        :param sx: scale factor in the X direction
        :param sy: scale factor in the Y direction

        Applies scaling by *sx, sy* to the transformation in *Matrix*. The
        effect of the new transformation is to first scale the coordinates by
        *sx* and *sy*, then apply the original transformation to the
        coordinates.
        """

    def transform_distance(self, dx: float, dy: float) -> Tuple[float, float]:
        """
        :param dx: X component of a distance vector.
        :param dy: Y component of a distance vector.
        :returns: the transformed distance vector (dx,dy), both float

        Transforms the distance vector *(dx,dy)* by *Matrix*. This is similar to
        :meth:`.transform_point` except that the translation components of
        the transformation are ignored. The calculation of the returned vector
        is as follows::

            dx2 = dx1 * a + dy1 * c
            dy2 = dx1 * b + dy1 * d

        Affine transformations are position invariant, so the same vector always
        transforms to the same vector. If *(x1,y1)* transforms to *(x2,y2)* then
        *(x1+dx1,y1+dy1)* will transform to *(x1+dx2,y1+dy2)* for all values
        of *x1* and *x2*.
        """

    def transform_point(self, x: float, y: float) -> Tuple[float, float]:
        """
        :param x: X position.
        :param y: Y position.
        :returns: the transformed point (x,y), both float

        Transforms the point *(x, y)* by *Matrix*.
        """

    def translate(self, tx: float, ty: float) -> None:
        """
        :param tx: amount to translate in the X direction
        :param ty: amount to translate in the Y direction

        Applies a transformation by *tx, ty* to the transformation in
        *Matrix*. The effect of the new transformation is to first translate the
        coordinates by *tx* and *ty*, then apply the original transformation to the
        coordinates.
        """

    xx: float = ...
    """
    xx component of the affine transformation

    .. versionadded:: 1.12.0
    """

    yx: float = ...
    """
    yx component of the affine transformation

    .. versionadded:: 1.12.0
    """

    xy: float = ...
    """
    xy component of the affine transformation

    .. versionadded:: 1.12.0
    """

    yy: float = ...
    """
    yy component of the affine transformation

    .. versionadded:: 1.12.0
    """

    x0: float = ...
    """
    X translation component of the affine transformation

    .. versionadded:: 1.12.0
    """

    y0: float = ...
    """
    Y translation component of the affine transformation

    .. versionadded:: 1.12.0
    """

class Pattern:
    """
    *Pattern* is the abstract base class from which all the other pattern classes
    derive. It cannot be instantiated directly.
    """

    def get_extend(self) -> Extend:
        """
        :returns: the current extend strategy used for drawing the *Pattern*.

        Gets the current extend mode for the *Pattern*. See
        :class:`cairo.Extend` attributes for details on the semantics of each
        extend strategy.
        """

    def get_matrix(self) -> Matrix:
        """
        :returns: a new :class:`Matrix` which stores a copy of the *Pattern's*
            transformation matrix
        """

    def get_filter(self) -> Filter:
        """
        :returns: the current filter used for
            resizing the pattern.

        .. versionadded:: 1.12.0

            Used to be a method of :class:`SurfacePattern` before
        """

    def set_filter(self, filter: Filter) -> None:
        """
        :param filter: a filter describing the filter
            to use for resizing the pattern

        Note that you might want to control filtering even when you do not have
        an explicit *Pattern* object, (for example when using
        :meth:`Context.set_source_surface`). In these cases, it is convenient to
        use :meth:`Context.get_source` to get access to the pattern that cairo
        creates implicitly. For example::

            context.set_source_surface(image, x, y)
            context.get_source().set_filter(cairo.FILTER_NEAREST)

        .. versionadded:: 1.12.0

            Used to be a method of :class:`SurfacePattern` before
        """

    def set_extend(self, extend: Extend) -> None:
        """
        :param extend: an extend describing how the
            area outside of the *Pattern* will be drawn

        Sets the mode to be used for drawing outside the area of a *Pattern*.

        The default extend mode is :attr:`cairo.Extend.NONE` for
        :class:`SurfacePattern` and :attr:`cairo.Extend.PAD` for
        :class:`Gradient` Patterns.
        """

    def set_matrix(self, matrix: Matrix) -> None:
        """
        :param matrix: a :class:`Matrix`

        Sets the *Pattern's* transformation matrix to *matrix*. This matrix is a
        transformation from user space to pattern space.

        When a *Pattern* is first created it always has the identity matrix for
        its transformation matrix, which means that pattern space is initially
        identical to user space.

        Important: Please note that the direction of this transformation matrix
        is from user space to pattern space. This means that if you imagine the
        flow from a *Pattern* to user space (and on to device space), then
        coordinates in that flow will be transformed by the inverse of the
        *Pattern* matrix.

        For example, if you want to make a *Pattern* appear twice as large as it
        does by default the correct code to use is::

            matrix = cairo.Matrix(xx=0.5,yy=0.5)
            pattern.set_matrix(matrix)

        Meanwhile, using values of 2.0 rather than 0.5 in the code above would
        cause the *Pattern* to appear at half of its default size.

        Also, please note the discussion of the user-space locking semantics of
        :class:`Context.set_source`.
        """

    def get_dither(self) -> Dither:
        """
        :returns: the current dithering mode.

        Gets the current dithering mode, as set by :meth:`Pattern.set_dither`.

        .. versionadded:: 1.25.0 Only available with cairo 1.18.0+
        """

    def set_dither(self, dither: Dither) -> None:
        """
        :param dither: a :class:`Dither` describing the new dithering mode

        Set the dithering mode of the rasterizer used for drawing shapes. This
        value is a hint, and a particular backend may or may not support a
        particular value.  At the current time, only pixman is supported.

        .. versionadded:: 1.25.0 Only available with cairo 1.18.0+
        """

class Glyph(Tuple[int, float, float]):
    """
    The :class:`Glyph` holds information about a single glyph when drawing or
    measuring text. A font is (in simple terms) a collection of shapes used to
    draw text. A glyph is one of these shapes. There can be multiple glyphs
    for a single character (alternates to be used in different contexts, for
    example), or a glyph can be a ligature of multiple characters. Cairo
    doesn't expose any way of converting input text into glyphs, so in order
    to use the Cairo interfaces that take arrays of glyphs, you must directly
    access the appropriate underlying font system.

    Note that the offsets given by x and y are not cumulative. When drawing or
    measuring text, each glyph is individually positioned with respect to the
    overall origin

    .. versionadded:: 1.15
        In prior versions a (int, float, float) tuple was used instead
        of :class:`Glyph`.
    """

    index: int = ... # type: ignore
    x: float = ...
    y: float = ...

    def __init__(self, index: int, x: float, y: float) -> None:
        """
        :param index:
            glyph index in the font. The exact interpretation of the glyph index
            depends on the font technology being used.
        :param x:
            the offset in the X direction between the origin used for drawing or
            measuring the string and the origin of this glyph.
        :param y:
            the offset in the Y direction between the origin used for drawing or
            measuring the string and the origin of this glyph.
        """

class TextCluster(Tuple[int, int]):
    """
    .. versionadded:: 1.15

    The :class:`TextCluster` structure holds information about a single text
    cluster. A text cluster is a minimal mapping of some glyphs corresponding
    to some UTF-8 text.

    For a cluster to be valid, both ``num_bytes`` and ``num_glyphs`` should be
    non-negative, and at least one should be non-zero. Note that clusters with
    zero glyphs are not as well supported as normal clusters. For example, PDF
    rendering applications typically ignore those clusters when PDF text is
    being selected.

    See :meth:`Context.show_text_glyphs` for how clusters are used in advanced
    text operations.
    """
    num_bytes: int = ...
    num_glyphs: int = ...
    def __init__(self, num_bytes: int, num_glyphs: int) -> None:
        """
        :param num_bytes:
            the number of bytes of UTF-8 text covered by cluster
        :param num_glyphs:
            the number of glyphs covered by cluster
        """

class TextClusterFlags(_IntEnum):
    """
    Specifies properties of a text cluster mapping.

    .. versionadded:: 1.14
    """

    BACKWARD: "TextClusterFlags" = ...
    """
    The clusters in the cluster array map to glyphs in the glyph array
    from end to start.
    """

class TextExtents(Tuple[float, float, float, float, float, float]):
    """
    .. versionadded:: 1.15
        In prior versions a (float, float, float, float, float, float) tuple
        was used instead of :class:`TextExtents`.

    The :class:`TextExtents` class stores the extents of a single glyph or a
    string of glyphs in user-space coordinates. Because text extents are in
    user-space coordinates, they are mostly, but not entirely, independent of
    the current transformation matrix. If you call ``context.scale(2.0,
    2.0)``, text will be drawn twice as big, but the reported text extents
    will not be doubled. They will change slightly due to hinting (so you
    can't assume that metrics are independent of the transformation matrix),
    but otherwise will remain unchanged.
    """
    x_bearing: float = ...
    y_bearing: float = ...
    width: float = ...
    height: float = ...
    x_advance: float = ...
    y_advance: float = ...
    def __init__(self, x_bearing: float, y_bearing: float, width: float, height: float, x_advance: float, y_advance: float) -> None:
        """
        :param x_bearing:
            the horizontal distance from the origin to the leftmost part of the
            glyphs as drawn. Positive if the glyphs lie entirely to the right of
            the origin.
        :param y_bearing:
            the vertical distance from the origin to the topmost part of the
            glyphs as drawn. Positive only if the glyphs lie completely below the
            origin; will usually be negative.
        :param width:
            width of the glyphs as drawn
        :param height:
            height of the glyphs as drawn
        :param x_advance:
            distance to advance in the X direction after drawing these glyphs
        :param y_advance:
            distance to advance in the Y direction after drawing these glyphs.
            Will typically be zero except for vertical text layout as found in
            East-Asian languages.
        """

class RectangleInt:
    """
    RectangleInt is a data structure for holding a rectangle with integer coordinates.

    .. versionadded:: 1.11.0
    """

    height: int = ...
    width: int = ...
    x: int = ...
    y: int = ...

    def __init__(self, x: int=0, y: int=0, width: int=0, height: int=0) -> None:
        """
        :param x:
            X coordinate of the left side of the rectangle.
        :param y:
            Y coordinate of the top side of the rectangle.
        :param width:
            Width of the rectangle.
        :param height:
            Height of the rectangle.

        Allocates a new RectangleInt object.
        """


class FontFace:
    """
    A *cairo.FontFace* specifies all aspects of a font other than the size or font
    matrix (a font matrix is used to distort a font by sheering it or scaling it
    unequally in the two directions). A *FontFace* can be set on a
    :class:`Context` by using :meth:`Context.set_font_face` the size and font
    matrix are set with :meth:`Context.set_font_size` and
    :meth:`Context.set_font_matrix`.

    There are various types of *FontFace*, depending on the font backend they
    use.

    .. note:: This class cannot be instantiated directly, it is returned by
        :meth:`Context.get_font_face`.
    """

class FontOptions:
    """
    An opaque structure holding all options that are used when rendering fonts.

    Individual features of a *FontOptions* can be set or accessed using functions
    named *FontOptions.set_<feature_name>* and
    *FontOptions.get_<feature_name>*,  like :meth:`FontOptions.set_antialias`
    and :meth:`FontOptions.get_antialias`.

    New features may be added to a *FontOptions* in the future. For this reason,
    :meth:`FontOptions.copy()`, :meth:`FontOptions.equal()`,
    :meth:`FontOptions.merge()`, and :meth:`FontOptions.hash()` should be used to
    copy, check for equality, merge, or compute a hash value of FontOptions
    objects.

    Implements `__eq__` and `__ne__` using `equal()` since 1.12.0.
    """

    def __init__(self) -> None:
        """
        Allocates a new FontOptions object with all options initialized to default
        values.
        """

    def get_antialias(self) -> Antialias:
        """
        :returns: the antialias mode for the *FontOptions* object
        """

    def get_hint_style(self) -> HintStyle:
        """
        :returns: the hint style for the *FontOptions* object
        """

    def get_subpixel_order(self) -> SubpixelOrder:
        """
        :returns: the subpixel order for the *FontOptions* object
        """

    def set_antialias(self, antialias: Antialias) -> None:
        """
        :param antialias: the antialias mode

        This specifies the type of antialiasing to do when rendering text.
        """

    def set_hint_metrics(self, hint_metrics: HintMetrics) -> None:
        """
        :param hint_metrics: the hint metrics mode

        This controls whether metrics are quantized to integer values in device
        units.
        """

    def set_hint_style(self, hint_style: HintStyle) -> None:
        """
        :param hint_style: the hint style

        This controls whether to fit font outlines to the pixel grid, and if so,
        whether to optimize for fidelity or contrast.
        """

    def merge(self, other: "FontOptions") -> None:
        """
        :param FontOptions other: another :class:`FontOptions`

        Merges non-default options from other into options , replacing existing
        values. This operation can be thought of as somewhat similar to
        compositing other onto options with the operation of
        :attr:`Operator.OVER`.

        .. versionadded:: 1.12.0
        """

    def copy(self) -> "FontOptions":
        """
        :returns: a new :class:`FontOptions`

        Returns a new font options object copying the option values from
        original.

        .. versionadded:: 1.12.0
        """

    def hash(self) -> int:
        """
        :returns: the hash value for the font options object

        Compute a hash for the font options object; this value will be useful
        when storing an object containing a :class:`FontOptions` in a hash
        table.

        .. versionadded:: 1.12.0
        """

    def equal(self, other: "FontOptions") -> bool:
        """
        :param other: another :class:`FontOptions`
        :returns: :obj:`True` if all fields of the two font options objects
            match. Note that this function will return :obj:`False` if either
            object is in error.

        Compares two font options objects for equality.

        .. versionadded:: 1.12.0
        """

    def set_variations(self, variations: Optional[str]) -> None:
        """
        :param variations: the new font variations, or :obj:`None`

        Sets the OpenType font variations for the font options object. Font
        variations are specified as a string with a format that is similar to
        the CSS font-variation-settings. The string contains a comma-separated
        list of axis assignments, which each assignment consists of a
        4-character axis name and a value, separated by whitespace and
        optional equals sign.

        Examples:

        * wght=200,wdth=140.5
        * wght 200 , wdth 140.5

        .. versionadded:: 1.18.0 Only available with cairo 1.15.12+
        """

    def get_variations(self) -> str:
        """
        :returns:
            the font variations for the font options object. The returned
            string belongs to the options and must not be modified. It is
            valid until either the font options object is destroyed or the
            font variations in this object is modified with
            :meth:`set_variations`.

        Gets the OpenType font variations for the font options object. See
        :meth:`set_variations` for details about the string format.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.12+
        """

    def get_hint_metrics(self) -> HintMetrics:
        """
        :returns: the hint metrics mode for the *FontOptions* object
        """

    def set_subpixel_order(self, subpixel_order: SubpixelOrder) -> None:
        """
        :param subpixel_order: the subpixel order

        The subpixel order specifies the order of color elements within each
        pixel on the display device when rendering with an antialiasing mode of
        :attr:`cairo.Antialias.SUBPIXEL`.
        """

    def set_color_mode(self, color_mode: ColorMode) -> None:
        """
        :param color_mode: the new color mode

        Sets the color mode for the font options object. This controls whether
        color fonts are to be rendered in color or as outlines. See the
        documentation for :class:`ColorMode` for full details.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

    def get_color_mode(self) -> ColorMode:
        """
        :returns: the color mode for the font options object

        Gets the color mode for the font options object. See the documentation
        for :class:`ColorMode` for full details.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

    def set_color_palette(self, palette_index: int) -> None:
        """
        :param palette_index: the palette index in the CPAL table

        Sets the OpenType font color palette for the font options object.
        OpenType color fonts with a CPAL table may contain multiple palettes.
        The default color palette index is :data:`COLOR_PALETTE_DEFAULT`. If
        palette_index is invalid, the default palette is used.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

    def get_color_palette(self) -> int:
        """
        :returns: the palette index

        Gets the OpenType color font palette for the font options object.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

    def set_custom_palette_color(self, index: int, red: float, green: float, blue: float, alpha: float) -> None:
        """
        :param index: the index of the color to set
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color
        :param alpha: alpha component of color

        Sets a custom palette color for the font options object. This overrides
        the palette color at the specified color index. This override is
        independent of the selected palette index and will remain in place even
        if :meth:`FontOptions.set_color_palette` is called to change the palette
        index.

        It is only possible to override color indexes already in the font
        palette.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

    def get_custom_palette_color(self, index: int) -> Tuple[float, float, float, float]:
        """
        :param index: the index of the color to get
        :returns: a (red, green, blue, alpha) tuple of float
        :raises Error: if no custom color exists for the color index.

        Gets the custom palette color for the color index for the font options
        object.

        .. versionadded:: 1.25.0 Only available with cairo 1.17.8+
        """

class ScaledFont:
    """
    A *ScaledFont* is a font scaled to a particular size and device resolution. A
    *ScaledFont* is most useful for low-level font usage where a library or
    application wants to cache a reference to a scaled font to speed up the
    computation of metrics.

    There are various types of scaled fonts, depending on the font backend they
    use.
    """

    def __init__(self, font_face: FontFace, font_matrix: Matrix, ctm: Matrix, options: FontOptions) -> None:
        """
            :param font_face: a :class:`FontFace` instance
            :param font_matrix: font space to user space transformation :class:`Matrix`
                for the font. In the simplest case of a N point font, this matrix is just
                a scale by N, but it can also be used to shear the font or stretch it
                unequally along the two axes. See :meth:`Context.set_font_matrix`.
            :param ctm: user to device transformation :class:`Matrix` with which the
                font will be used.
            :param options: a :class:`FontOptions` instance to use when getting metrics
                for the font and rendering with it.

            Creates a *ScaledFont* object from a *FontFace* and matrices that describe
            the size of the font and the environment in which it will be used.
        """

    def extents(self) -> Tuple[float, float, float, float, float]:
        """
        Gets the metrics for a *ScaledFont*.
        """

    def get_ctm(self) -> Matrix:
        """
            :returns: the CTM

            Returns the CTM with which scaled_font was created into ctm. Note that
            the translation offsets (x0, y0) of the CTM are ignored by
            :func:`ScaledFont`. So, the matrix this function returns always has 0,
            0 as x0, y0.

            .. versionadded:: 1.12.0
        """

    def get_font_face(self) -> FontFace:
        """
            :returns: the :class:`FontFace` that this *ScaledFont* was created for.

            .. versionadded:: 1.2
        """

    def get_font_matrix(self) -> Matrix:
        """
            :returns: the matrix

            Returns the font matrix with which scaled_font was created.
        """

    def get_font_options(self) -> FontOptions:
        """
            :returns: font options

            Returns the font options with which scaled_font was created.

            .. versionadded:: 1.12.0
        """

    def get_scale_matrix(self) -> Matrix:
        """
            :returns: the scale :class:`Matrix`

            The scale matrix is product of the font matrix and the ctm associated
            with the scaled font, and hence is the matrix mapping from font space to
            device space.

            .. versionadded:: 1.8
        """

    def glyph_extents(self, glyphs: Sequence[Glyph]) -> TextExtents:
        """
            :param glyphs: glyphs, a sequence of :class:`Glyph`

            .. versionadded:: 1.15

            Gets the extents for a list of glyphs. The extents describe a user-space
            rectangle that encloses the "inked" portion of the glyphs, (as they
            would be drawn by :meth:`Context.show_glyphs` if the cairo graphics
            state were set to the same font_face, font_matrix, ctm, and font_options
            as scaled_font ). Additionally, the x_advance and y_advance values
            indicate the amount by which the current point would be advanced by
            cairo_show_glyphs().

            Note that whitespace glyphs do not contribute to the size of the
            rectangle (extents.width and extents.height).
        """

    def text_extents(self, text: str) -> TextExtents:
        """
            :param text: text

            Gets the extents for a string of text. The extents describe a user-space
            rectangle that encloses the "inked" portion of the text drawn at the
            origin (0,0) (as it would be drawn by :meth:`Context.show_text` if the
            cairo graphics state were set to the same font_face, font_matrix, ctm,
            and font_options as *ScaledFont*).  Additionally, the x_advance and
            y_advance values indicate the amount by which the current point would be
            advanced by :meth:`Context.show_text`.

            Note that whitespace characters do not directly contribute to the size
            of the rectangle (width and height). They do contribute indirectly by
            changing the position of non-whitespace characters. In particular,
            trailing whitespace characters are likely to not affect the size of the
            rectangle, though they will affect the x_advance and y_advance values.

            .. versionadded:: 1.2
        """

    def text_to_glyphs(self, x: float, y: float, utf8: str, with_clusters: bool = True) -> Union[Tuple[List[Glyph], List["TextCluster"], TextClusterFlags], List[Glyph]]:
        """
            :param x: X position to place first glyph
            :param y: Y position to place first glyph
            :param utf8: a string of text
            :param with_clusters:
                If :obj:`False` only the glyph list will computed and returned
            :returns:
                a tuple of ([:class:`Glyph`], [:class:`TextCluster`],
                :class:`TextClusterFlags`)
            :raises Error:

            .. versionadded:: 1.15

            Converts UTF-8 text to a list of glyphs, with cluster mapping, that can
            be used to render later.

            For details of how clusters, and cluster_flags map input UTF-8 text to
            the output glyphs see :meth:`Context.show_text_glyphs`.

            The output values can be readily passed to
            :meth:`Context.show_text_glyphs` :meth:`Context.show_glyphs`, or related
            functions, assuming that the exact same scaled font is used for the
            operation.
        """

_SomeDevice = TypeVar("_SomeDevice", bound="Device")

class Device:
    """
    A :class:`Device` represents the driver interface for drawing operations
    to a :class:`Surface`.

    .. versionadded:: 1.14

    .. note::

        .. versionadded:: 1.17.0

            :class:`cairo.Device` can be used as a context manager:

        .. code:: python

            # device.finish() will be called on __exit__
            with cairo.ScriptDevice(f) as device:
                pass
    """

    def finish(self) -> None:
        """
        This function finishes the device and drops all references to external
        resources. All surfaces, fonts and other objects created for this
        device will be finished, too. Further operations on the device will
        not affect the device but will instead trigger a
        :attr:`Status.DEVICE_FINISHED` error.

        This function may acquire devices.

        .. versionadded:: 1.14
        """

    def flush(self) -> None:
        """
        Finish any pending operations for the device and also restore any
        temporary modifications cairo has made to the device's state. This
        function must be called before switching from using the device with
        Cairo to operating on it directly with native APIs. If the device
        doesn't support direct access, then this function does nothing.

        This function may acquire devices.

        .. versionadded:: 1.14
        """

    def acquire(self) -> None:
        """
        :raises cairo.Error:
            If the device is in an error state and could not be acquired.

        Acquires the device for the current thread. This function will block
        until no other thread has acquired the device.

        If the does not raise, you successfully acquired the device. From now
        on your thread owns the device and no other thread will be able to
        acquire it until a matching call to :meth:`release`. It is allowed to
        recursively acquire the device multiple times from the same thread.

        After a successful call to :meth:`acquire`, a matching call to
        :meth:`release` is required.

        .. note::

            You must never acquire two different devices at the same time
            unless this is explicitly allowed. Otherwise the possibility of
            deadlocks exist. As various Cairo functions can acquire devices
            when called, these functions may also cause deadlocks when you
            call them with an acquired device. So you must not have a device
            acquired when calling them. These functions are marked in the
            documentation.

        .. versionadded:: 1.14
        """

    def release(self) -> None:
        """
        Releases a device previously acquired using :meth:`acquire`. See that
        function for details.

        .. versionadded:: 1.14
        """

    def __enter__(self: _SomeDevice) -> _SomeDevice: ...
    __exit__: Any = ...

_PathLike = Union[Text, ByteString]
_FileLike = BinaryIO
_SomeSurface = TypeVar("_SomeSurface", bound="Surface")

class Surface:
    """
    cairo.Surface is the abstract type representing all different drawing targets
    that cairo can render to. The actual drawings are performed using a
    :class:`Context`.

    A cairo.Surface is created by using backend-specific constructors
    of the form cairo.<XXX>Surface().

    *Surface* is the abstract base class from which all the other surface
    classes derive. It cannot be instantiated directly.

    .. note::

        .. versionadded:: 1.17.0

            :class:`cairo.Surface` can be used as a context manager:

        .. code:: python

            # surface.finish() will be called on __exit__
            with cairo.SVGSurface("example.svg", 200, 200) as surface:
                pass

            # surface.unmap_image(image_surface) will be called on __exit__
            with surface.map_to_image(None) as image_surface:
                pass
    """

    def copy_page(self) -> None:
        """
        Emits the current page for backends that support multiple pages, but
        doesn't clear it, so that the contents of the current page will be
        retained for the next page.  Use :meth:`.show_page` if you want to get an
        empty page after the emission.

        :meth:`Context.copy_page` is a convenience function for this.

        .. versionadded:: 1.6
        """

    def create_for_rectangle(self, x: float, y: float, width: float, height: float) -> "Surface":
        """
        :param x: the x-origin of the sub-surface from the top-left of the
            target surface (in device-space units)
        :param y: the y-origin of the sub-surface from the top-left of the
            target surface (in device-space units)
        :param width: width of the sub-surface (in device-space units)
        :param height: height of the sub-surface (in device-space units)
        :returns: a new surface

        Create a new surface that is a rectangle within the target surface. All
        operations drawn to this surface are then clipped and translated onto
        the target surface. Nothing drawn via this sub-surface outside of its
        bounds is drawn onto the target surface, making this a useful method for
        passing constrained child surfaces to library routines that draw
        directly onto the parent surface, i.e. with no further backend
        allocations, double buffering or copies.

        .. note::

            The semantics of subsurfaces have not been finalized yet unless the
            rectangle is in full device units, is contained within the extents of
            the target surface, and the target or subsurface's device transforms
            are not changed.

        .. versionadded:: 1.12.0
        """

    def create_similar(self, content: Content, width: int, height: int) -> "Surface":
        """
        :param content: the content for the new
            surface
        :param width: width of the new surface, (in device-space units)
        :param height: height of the new surface (in device-space units)

        :returns: a newly allocated *Surface*.

        Create a *Surface* that is as compatible as possible with the existing
        surface. For example the new surface will have the same fallback
        resolution and :class:`FontOptions`. Generally, the new surface will
        also use the same backend, unless that is not possible for some
        reason.

        Initially the surface contents are all 0 (transparent if contents have
        transparency, black otherwise.)
        """

    def create_similar_image(self, format: Format, width: int, height: int) -> "ImageSurface":
        """
        :param cairo.Format format: the format for the new surface
        :param width: width of the new surface, (in device-space units)
        :param height: height of the new surface, (in device-space units)
        :returns: a new image surface

        Create a new image surface that is as compatible as possible for
        uploading to and the use in conjunction with an existing surface.
        However, this surface can still be used like any normal image surface.

        Initially the surface contents are all 0 (transparent if contents have
        transparency, black otherwise.)

        .. versionadded:: 1.12.0
        """

    def finish(self) -> None:
        """
        This method finishes the Surface and drops all references to external
        resources. For example, for the Xlib backend it means that cairo will no
        longer access the drawable, which can be freed. After calling finish()
        the only valid operations on a Surface are flushing and finishing it.
        Further drawing to the surface will not affect the surface but will
        instead trigger a `cairo.Error` exception.
        """

    def flush(self) -> None:
        """
        Do any pending drawing for the *Surface* and also restore any temporary
        modification's cairo has made to the *Surface's* state. This method
        must be called before switching from drawing on the *Surface* with cairo
        to drawing on it directly with native APIs. If the *Surface* doesn't
        support direct access, then this function does nothing.
        """

    def get_content(self) -> Content:
        """
        :returns: The content type of *Surface*,
            which indicates whether the *Surface* contains color and/or alpha
            information.

        .. versionadded:: 1.2
        """

    def get_device(self) -> Optional["Device"]:
        """
        :returns: the device or :obj:`None` if the surface does not have an
            associated device

        This function returns the device for a surface.

        .. versionadded:: 1.14.0
        """

    def get_device_offset(self) -> Tuple[float, float]:
        """
        :returns: (x_offset, y_offset) a tuple of float

            * x_offset: the offset in the X direction, in device units
            * y_offset: the offset in the Y direction, in device units

        This method returns the previous device offset set by
        :meth:`.set_device_offset`.

        .. versionadded:: 1.2
        """

    def get_device_scale(self) -> Tuple[float, float]:
        """
        :returns: (x_scale,y_scale) a 2-tuple of float

        This function returns the previous device offset set by
        :meth:`Surface.set_device_scale`.

        .. versionadded:: 1.14.0
        """

    def get_fallback_resolution(self) -> Tuple[float, float]:
        """
        :returns: (x_pixels_per_inch, y_pixels_per_inch) a tuple of float

            * x_pixels_per_inch: horizontal pixels per inch
            * y_pixels_per_inch: vertical pixels per inch

        This method returns the previous fallback resolution set by
        :meth:`.set_fallback_resolution`, or default fallback resolution if
        never set.

        .. versionadded:: 1.8
        """

    def get_font_options(self) -> FontOptions:
        """
        :returns: a :class:`FontOptions`

        Retrieves the default font rendering options for the *Surface*. This
        allows display surfaces to report the correct subpixel order for
        rendering on them, print surfaces to disable hinting of metrics and so
        forth. The result can then be used with :class:`ScaledFont`.
        """

    def get_mime_data(self, mime_type: str) -> Optional[bytes]:
        """
        :param mime_type: the MIME type of the image data
            (:ref:`constants_MIME_TYPE`)
        :returns: :class:`bytes` or :obj:`None`

        Return mime data previously attached to surface
        with :meth:`set_mime_data` using the specified mime type.
        If no data has been attached with the given mime type,
        :obj:`None` is returned.

        .. versionadded:: 1.12.0
        """

    def has_show_text_glyphs(self) -> bool:
        """
        :returns: :obj:`True` if surface supports
            :meth:`Context.show_text_glyphs`, :obj:`False` otherwise

        Returns whether the surface supports sophisticated
        :meth:`Context.show_text_glyphs` operations. That is, whether it
        actually uses the provided text and cluster data to a
        :meth:`Context.show_text_glyphs` call.

        Note: Even if this function returns :obj:`False`, a
        :meth:`Context.show_text_glyphs` operation targeted at surface will
        still succeed. It just will act like a :meth:`Context.show_glyphs`
        operation. Users can use this function to avoid computing UTF-8 text and
        cluster mapping if the target surface does not use it.

        .. versionadded:: 1.12.0
        """

    def map_to_image(self, extents: Optional[RectangleInt]) -> "ImageSurface":
        """
        :param extents: limit the extraction to an rectangular
            region or :obj:`None` for the whole surface

        :returns: newly allocated image surface
        :raises Error:

        Returns an image surface that is the most efficient mechanism for
        modifying the backing store of the target surface.

        Note, the use of the original surface as a target or source whilst it is
        mapped is undefined. The result of mapping the surface multiple times is
        undefined. Calling :meth:`Surface.finish` on the resulting image surface
        results in undefined behavior. Changing the device transform of the
        image surface or of surface before the image surface is unmapped results
        in undefined behavior.

        The caller must use :meth:`Surface.unmap_image` to destroy this image
        surface.

        .. versionadded:: 1.15.0
        """

    def mark_dirty(self) -> None:
        """
        Tells cairo that drawing has been done to *Surface* using means other
        than cairo, and that cairo should reread any cached areas. Note that you
        must call :meth:`.flush` before doing such drawing.
        """

    def mark_dirty_rectangle(self, x: int, y: int, width: int, height: int) -> None:
        """
        :param x: X coordinate of dirty rectangle
        :param y: Y coordinate of dirty rectangle
        :param width: width of dirty rectangle
        :param height: height of dirty rectangle

        Like :meth:`.mark_dirty`, but drawing has been done only to the
        specified rectangle, so that cairo can retain cached contents for other
        parts of the surface.

        Any cached clip set on the *Surface* will be reset by this function, to
        make sure that future cairo calls have the clip set that they expect.
        """

    def set_device_offset(self, x_offset: float, y_offset: float) -> None:
        """
        :param x_offset: the offset in the X direction, in device units
        :param y_offset: the offset in the Y direction, in device units

        Sets an offset that is added to the device coordinates determined by the
        CTM when drawing to *Surface*. One use case for this function is when we
        want to create a *Surface* that redirects drawing for a portion of an
        onscreen surface to an offscreen surface in a way that is completely
        invisible to the user of the cairo API. Setting a transformation via
        :meth:`Context.translate` isn't sufficient to do this, since functions
        like :meth:`Context.device_to_user` will expose the hidden offset.

        Note that the offset affects drawing to the surface as well as using the
        surface in a source pattern.
        """

    def set_device_scale(self, x_scale: float, y_scale: float) -> None:
        """
        :param x_scale: a scale factor in the X direction
        :param y_scale: a scale factor in the Y direction

        Sets a scale that is multiplied to the device coordinates determined by
        the CTM when drawing to surface . One common use for this is to render
        to very high resolution display devices at a scale factor, so that code
        that assumes 1 pixel will be a certain size will still work. Setting a
        transformation via :meth:`Context.translate` isn't sufficient to do
        this, since functions like :meth:`Context.device_to_user` will expose
        the hidden scale.

        .. versionadded:: 1.14.0
        """

    def set_fallback_resolution(self, x_pixels_per_inch: float, y_pixels_per_inch: float) -> None:
        """
        :param x_pixels_per_inch: horizontal setting for pixels per inch
        :param y_pixels_per_inch: vertical setting for pixels per inch

        Set the horizontal and vertical resolution for image fallbacks.

        When certain operations aren't supported natively by a backend, cairo
        will fallback by rendering operations to an image and then overlaying
        that image onto the output. For backends that are natively
        vector-oriented, this function can be used to set the resolution used
        for these image fallbacks, (larger values will result in more detailed
        images, but also larger file sizes).

        Some examples of natively vector-oriented backends are the ps, pdf, and
        svg backends.

        For backends that are natively raster-oriented, image fallbacks are
        still possible, but they are always performed at the native device
        resolution. So this function has no effect on those backends.

        Note: The fallback resolution only takes effect at the time of
        completing a page (with :meth:`Context.show_page` or
        :meth:`Context.copy_page`) so there is currently no way to have more
        than one fallback resolution in effect on a single page.

        The default fallback resoultion is 300 pixels per inch in both
        dimensions.

        .. versionadded:: 1.2
        """

    def set_mime_data(self, mime_type: str, data: bytes) -> None:
        """
        :param mime_type: the MIME type of the image data
            (:ref:`constants_MIME_TYPE`)
        :param data: the image data to attach to the surface

        Attach an image in the format ``mime_type`` to *Surface*.
        To remove the data from a surface,
        call this function with same mime type and :obj:`None` for data.

        The attached image (or filename) data can later be used
        by backends which support it
        (currently: PDF, PS, SVG and Win32 Printing surfaces)
        to emit this data instead of making a snapshot of the surface.
        This approach tends to be faster and requires less memory and disk space.

        The recognized MIME types are listed under :ref:`constants_MIME_TYPE`.

        See corresponding backend surface docs for details
        about which MIME types it can handle.
        Caution: the associated MIME data will be discarded
        if you draw on the surface afterwards.
        Use this function with care.

        .. versionadded:: 1.12.0
        """

    def show_page(self) -> None:
        """
        Emits and clears the current page for backends that support multiple
        pages. Use :meth:`.copy_page` if you don't want to clear the page.

        There is a convenience function for this that takes a
        :meth:`Context.show_page`.

        .. versionadded:: 1.6
        """

    def supports_mime_type(self, mime_type: str) -> bool:
        """
        :param mime_type: the mime type (:ref:`constants_MIME_TYPE`)
        :returns: :obj:`True` if surface supports mime_type, :obj:`False`
            otherwise

        Return whether surface supports ``mime_type``.

        .. versionadded:: 1.12.0
        """

    def write_to_png(self, fobj: Union[_FileLike, _PathLike]) -> None:
        """
        :param fobj: a filename or writable file object
        :raises: :exc:`MemoryError` if memory could not be allocated for the operation

                :exc:`IOError` if an I/O error occurs while attempting to write
                the file

        Writes the contents of *Surface* to *fobj* as a PNG image. *fobj* can either be
        a filename or a file object opened in binary mode.
        """

    def unmap_image(self, image: "ImageSurface") -> None:
        """
        :param image: the currently mapped image

        Unmaps the image surface as returned from :meth:`Surface.map_to_image`.

        The content of the image will be uploaded to the target surface.
        Afterwards, the image is destroyed.

        Using an image surface which wasn't returned by
        :meth:`Surface.map_to_image` results in undefined behavior.

        .. versionadded:: 1.15.0
        """

    def __enter__(self: _SomeSurface) -> _SomeSurface: ...
    __exit__: Any = ...

class ImageSurface(Surface):
    """
    A *cairo.ImageSurface* provides the ability to render to memory buffers
    either allocated by cairo or by the calling code. The supported image
    formats are those defined in :class:`cairo.Format`.
    """

    def __init__(self, format: Format, width: int, height: int) -> None:
        """
        :param format: format of pixels in the surface to create
        :param width: width of the surface, in pixels
        :param height: height of the surface, in pixels
        :returns: a new *ImageSurface*

        Creates an *ImageSurface* of the specified format and dimensions. Initially
        the surface contents are all 0. (Specifically, within each pixel, each
        color or alpha channel belonging to format will be 0. The contents of bits
        within a pixel, but not belonging to the given format are undefined).
        """

    @classmethod
    def create_for_data(cls, data: memoryview, format: Format, width: int, height: int, stride: int = ...) -> "ImageSurface":
        """
        :param data: a writable Python buffer/memoryview object
        :param format: the format of pixels in the
            buffer
        :param width: the width of the image to be stored in the buffer
        :param height: the height of the image to be stored in the buffer
        :param stride: the number of bytes between the start of rows in the
            buffer as allocated. If not given the value from
            :meth:`cairo.Format.stride_for_width` is used.
        :returns: a new *ImageSurface*
        :raises: :exc:`MemoryError` in case of no memory.

                :exc:`cairo.Error` in case of invalid *stride* value.

        Creates an *ImageSurface* for the provided pixel data. The initial
        contents of buffer will be used as the initial image contents; you must
        explicitly clear the buffer, using, for example, cairo_rectangle() and
        cairo_fill() if you want it cleared.

        Note that the *stride* may be larger than width*bytes_per_pixel to
        provide proper alignment for each pixel and row. This alignment is
        required to allow high-performance rendering within cairo. The correct
        way to obtain a legal stride value is to call
        :meth:`cairo.Format.stride_for_width` with the desired format and
        maximum image width value, and use the resulting stride value to
        allocate the data and to create the :class:`ImageSurface`. See
        :meth:`cairo.Format.stride_for_width` for example code.
        """

    @classmethod
    def create_from_png(cls, fobj: Union[_PathLike, _FileLike]) -> "ImageSurface":
        """
        :param fobj:
            a :obj:`_PathLike`, file, or file-like object of the PNG to load.
        :returns: a new *ImageSurface* initialized the contents to the given PNG
            file.

        Creates a new image surface and initializes the contents to the given
        PNG file. *fobj* can either be a filename or a file object opened in
        binary mode.
        """

    format_stride_for_width = Format.stride_for_width
    """
    See :meth:`cairo.Format.stride_for_width`.

    .. versionadded:: 1.6
    """

    def get_data(self) -> memoryview:
        """
        :returns: a Python buffer object for the data of the *ImageSurface*, for
            direct inspection or modification. On Python 3 a memoryview object is
            returned.

        .. versionadded:: 1.2
        """

    def get_format(self) -> Format:
        """
        :returns: the format of the *ImageSurface*.
        :rtype: cairo.Format

        .. versionadded:: 1.2
        """

    def get_height(self) -> int:
        """
        :returns: the height of the *ImageSurface* in pixels.
        """

    def get_stride(self) -> int:
        """
        :returns: the stride of the *ImageSurface* in bytes. The stride is the
            distance in bytes from the beginning of one row of the image data to
            the beginning of the next row.
        """

    def get_width(self) -> int:
        """
        :returns: the width of the *ImageSurface* in pixels.
        """

class SurfacePattern(Pattern):

    def __init__(self, surface: Surface) -> None:
        """
        :param surface: a cairo :class:`Surface`
        """

    def get_surface(self) -> Surface:
        """
        :returns: the :class:`Surface` of the *SurfacePattern*.

        .. versionadded:: 1.4
        """

class Context(Generic[_SomeSurface]):
    """
    *Context* is the main object used when drawing with cairo. To draw with cairo,
    you create a *Context*, set the target surface, and drawing options for the
    *Context*, create shapes with functions like :meth:`Context.move_to` and
    :meth:`Context.line_to`, and then draw shapes with :meth:`Context.stroke` or
    :meth:`Context.fill`.

    *Contexts* can be pushed to a stack via :meth:`Context.save`. They may then
    safely be changed, without losing the current state. Use
    :meth:`Context.restore` to restore to the saved state.
    """

    def __init__(self, target: _SomeSurface) -> None:
        """
        :param target: target :class:`Surface` for the context
        :raises: :exc:`MemoryError` in case of no memory

        Creates a new *Context* with all graphics state parameters set to default
        values and with *target* as a target surface. The target surface should be
        constructed with a backend-specific function such as :class:`ImageSurface`
        (or any other cairo backend surface create variant).
        """

    def append_path(self, path: Path) -> None:
        """
        :param path: :class:`Path` to be appended

        Append the *path* onto the current path. The *path* may be either the
        return value from one of :meth:`Context.copy_path` or
        :meth:`Context.copy_path_flat` or it may be constructed manually (in C).
        """

    def arc(self, xc: float, yc: float, radius: float, angle1: float, angle2: float) -> None:
        """
        :param xc: X position of the center of the arc
        :param yc: Y position of the center of the arc
        :param radius: the radius of the arc
        :param angle1: the start angle, in radians
        :param angle2: the end angle, in radians

        Adds a circular arc of the given *radius* to the current path.  The arc
        is centered at (*xc, yc*), begins at *angle1* and proceeds in the
        direction of increasing angles to end at *angle2*. If *angle2* is less
        than *angle1* it will be progressively increased by 2*PI until it is
        greater than *angle1*.

        If there is a current point, an initial line segment will be added to
        the path to connect the current point to the beginning of the arc. If
        this initial line is undesired, it can be avoided by calling
        :meth:`Context.new_sub_path` before calling :meth:`Context.arc`.

        Angles are measured in radians. An angle of 0.0 is in the direction of
        the positive X axis (in user space). An angle of PI/2.0 radians (90
        degrees) is in the direction of the positive Y axis (in user
        space). Angles increase in the direction from the positive X axis toward
        the positive Y axis. So with the default transformation matrix, angles
        increase in a clockwise direction.

        To convert from degrees to radians, use ``degrees * (math.pi / 180)``.

        This function gives the arc in the direction of increasing angles; see
        :meth:`Context.arc_negative` to get the arc in the direction of
        decreasing angles.

        The arc is circular in user space. To achieve an elliptical arc,
        you can scale the current transformation matrix by different
        amounts in the X and Y directions. For example, to draw an ellipse
        in the box given by *x, y, width, height*::

            ctx.save()
            ctx.translate(x + width / 2., y + height / 2.)
            ctx.scale(width / 2., height / 2.)
            ctx.arc(0., 0., 1., 0., 2 * math.pi)
            ctx.restore()
        """

    def arc_negative(self, xc: float, yc: float, radius: float, angle1: float, angle2: float) -> None:
        """
        :param xc: X position of the center of the arc
        :param yc: Y position of the center of the arc
        :param radius: the radius of the arc
        :param angle1: the start angle, in radians
        :param angle2: the end angle, in radians

        Adds a circular arc of the given *radius* to the current path. The arc
        is centered at (*xc, yc*), begins at *angle1* and proceeds in the
        direction of decreasing angles to end at *angle2*. If *angle2* is
        greater than *angle1* it will be progressively decreased by 2*PI until
        it is less than *angle1*.

        See :meth:`Context.arc` for more details. This function differs only in
        the direction of the arc between the two angles.
        """

    def clip(self) -> None:
        """
        Establishes a new clip region by intersecting the current clip region
        with the current path as it would be filled by :meth:`Context.fill` and
        according to the current :class:`fill rule <cairo.FillRule>` (see
        :meth:`Context.set_fill_rule`).

        After :meth:`.clip`, the current path will be cleared from the
        :class:`Context`.

        The current clip region affects all drawing operations by effectively
        masking out any changes to the surface that are outside the current clip
        region.

        Calling :meth:`.clip` can only make the clip region smaller, never
        larger. But the current clip is part of the graphics state, so a
        temporary restriction of the clip region can be achieved by calling
        :meth:`.clip` within a :meth:`Context.save`/:meth:`Context.restore`
        pair. The only other means of increasing the size of the clip region is
        :meth:`Context.reset_clip`.
        """

    def clip_extents(self) -> Tuple[float, float, float, float]:
        """
        :returns: (x1, y1, x2, y2), all float

        * *x1*: left of the resulting extents
        * *y1*: top of the resulting extents
        * *x2*: right of the resulting extents
        * *y2*: bottom of the resulting extents

        Computes a bounding box in user coordinates covering the area inside the
        current clip.

        .. versionadded:: 1.4
        """

    def clip_preserve(self) -> None:
        """
        Establishes a new clip region by intersecting the current clip region
        with the current path as it would be filled by :meth:`Context.fill` and
        according to the current :class:`fill rule <cairo.FillRule>` (see
        :meth:`Context.set_fill_rule`).

        Unlike :meth:`Context.clip`, :meth:`.clip_preserve` preserves the path
        within the :class:`Context`.

        The current clip region affects all drawing operations by effectively
        masking out any changes to the surface that are outside the current clip
        region.

        Calling :meth:`.clip_preserve` can only make the clip region smaller,
        never larger. But the current clip is part of the graphics state, so a
        temporary restriction of the clip region can be achieved by calling
        :meth:`.clip_preserve` within a
        :meth:`Context.save`/:meth:`Context.restore` pair. The only other means
        of increasing the size of the clip region is :meth:`Context.reset_clip`.
        """

    def close_path(self) -> None:
        """
        Adds a line segment to the path from the current point to the beginning
        of the current sub-path, (the most recent point passed to
        :meth:`Context.move_to`), and closes this sub-path. After this call the
        current point will be at the joined endpoint of the sub-path.

        The behavior of :meth:`.close_path` is distinct from simply calling
        :meth:`Context.line_to` with the equivalent coordinate in the case of
        stroking. When a closed sub-path is stroked, there are no caps on the
        ends of the sub-path. Instead, there is a line join connecting the final
        and initial segments of the sub-path.

        If there is no current point before the call to :meth:`.close_path`,
        this function will have no effect.

        Note: As of cairo version 1.2.4 any call to :meth:`.close_path` will
        place an explicit MOVE_TO element into the path immediately after the
        CLOSE_PATH element, (which can be seen in :meth:`Context.copy_path` for
        example). This can simplify path processing in some cases as it may not
        be necessary to save the "last move_to point" during processing as the
        MOVE_TO immediately after the CLOSE_PATH will provide that point.
        """

    def copy_clip_rectangle_list(self) -> List[Rectangle]:
        """
        :returns: the current clip region as a list of rectangles in user
            coordinates. Returns a list of :class:`Rectangle`

        .. versionadded:: 1.4
        """

    def copy_page(self) -> None:
        """
        Emits the current page for backends that support multiple pages, but
        doesn't clear it, so, the contents of the current page will be retained
        for the next page too.  Use :meth:`Context.show_page` if you want to get
        an empty page after the emission.

        This is a convenience function that simply calls
        :meth:`Surface.copy_page` on *Context's* target.
        """

    def copy_path(self) -> Path:
        """
        :returns: :class:`Path`
        :raises: :exc:`MemoryError` in case of no memory

        Creates a copy of the current path and returns it to the user as a
        :class:`Path`.
        """

    def copy_path_flat(self) -> Path:
        """
        :returns: :class:`Path`
        :raises: :exc:`MemoryError` in case of no memory

        Gets a flattened copy of the current path and returns it to the
        user as a :class:`Path`.

        This function is like :meth:`Context.copy_path` except that any curves
        in the path will be approximated with piecewise-linear approximations,
        (accurate to within the current tolerance value). That is, the result is
        guaranteed to not have any elements of type CAIRO_PATH_CURVE_TO which
        will instead be replaced by a series of CAIRO_PATH_LINE_TO elements.
        """

    def curve_to(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        """
        :param x1: the X coordinate of the first control point
        :param y1: the Y coordinate of the first control point
        :param x2: the X coordinate of the second control point
        :param y2: the Y coordinate of the second control point
        :param x3: the X coordinate of the end of the curve
        :param y3: the Y coordinate of the end of the curve

        Adds a cubic Bézier spline to the path from the current point to
        position *(x3, y3)* in user-space coordinates, using *(x1, y1)* and
        *(x2, y2)* as the control points. After this call the current point will
        be *(x3, y3)*.

        If there is no current point before the call to :meth:`.curve_to`
        this function will behave as if preceded by a call to
        ``ctx.move_to(x1, y1)``.
        """

    def device_to_user(self, x: float, y: float) -> Tuple[float, float]:
        """
        :param x: X value of coordinate
        :param y: Y value of coordinate
        :returns: (x, y), both float

        Transform a coordinate from device space to user space by multiplying
        the given point by the inverse of the current transformation matrix
        (CTM).
        """

    def device_to_user_distance(self, dx: float, dy: float) -> Tuple[float, float]:
        """
        :param dx: X component of a distance vector
        :param dy: Y component of a distance vector
        :returns: (dx, dy), both float

        Transform a distance vector from device space to user space. This
        function is similar to :meth:`Context.device_to_user` except that the
        translation components of the inverse CTM will be ignored when
        transforming *(dx,dy)*.
        """

    def fill(self) -> None:
        """
        A drawing operator that fills the current path according to the current
        :class:`fill rule <cairo.FillRule>`, (each sub-path is implicitly
        closed before being filled). After :meth:`.fill`, the current path will
        be cleared from the :class:`Context`. See :meth:`Context.set_fill_rule`
        and :meth:`Context.fill_preserve`.
        """

    def fill_extents(self) -> Tuple[float, float, float, float]:
        """
        :returns: (x1, y1, x2, y2), all float

        * *x1*: left of the resulting extents
        * *y1*: top of the resulting extents
        * *x2*: right of the resulting extents
        * *y2*: bottom of the resulting extents

        Computes a bounding box in user coordinates covering the area that would
        be affected, (the "inked" area), by a :meth:`Context.fill` operation
        given the current path and fill parameters. If the current path is
        empty, returns an empty rectangle (0,0,0,0). Surface dimensions and
        clipping are not taken into account.

        Contrast with :meth:`Context.path_extents`, which is similar, but returns
        non-zero extents for some paths with no inked area, (such as a
        simple line segment).

        Note that :meth:`.fill_extents` must necessarily do more work to compute
        the precise inked areas in light of the fill rule, so
        :meth:`Context.path_extents` may be more desirable for sake of
        performance if the non-inked path extents are desired.

        See :meth:`Context.fill`, :meth:`Context.set_fill_rule` and
        :meth:`Context.fill_preserve`.
        """

    def fill_preserve(self) -> None:
        """
        A drawing operator that fills the current path according to the current
        :class:`fill rule <cairo.FillRule>`, (each sub-path is implicitly
        closed before being filled). Unlike :meth:`Context.fill`,
        :meth:`.fill_preserve` preserves the path within the :class:`Context`.

        See :meth:`Context.set_fill_rule` and :meth:`Context.fill`.
        """

    def font_extents(self) -> Tuple[float, float, float, float, float]:
        """
        :returns: (ascent, descent, height, max_x_advance, max_y_advance),
            all float

        Gets the font extents for the currently selected font.
        """

    def get_antialias(self) -> Antialias:
        """
        :returns: the current antialias mode,
            as set by :meth:`Context.set_antialias`.
        """

    def get_current_point(self) -> Tuple[float, float]:
        """
        :returns: (x, y), both float

        * *x*: X coordinate of the current point
        * *y*: Y coordinate of the current point

        Gets the current point of the current path, which is conceptually the
        final point reached by the path so far.

        The current point is returned in the user-space coordinate system. If
        there is no defined current point or if :class:`Context` is in an error
        status, *x* and *y* will both be set to 0.0. It is possible to check this
        in advance with :meth:`Context.has_current_point`.

        Most path construction functions alter the current point. See the
        following for details on how they affect the current point:
        :meth:`Context.new_path`, :meth:`Context.new_sub_path`,
        :meth:`Context.append_path`, :meth:`Context.close_path`,
        :meth:`Context.move_to`, :meth:`Context.line_to`,
        :meth:`Context.curve_to`, :meth:`Context.rel_move_to`,
        :meth:`Context.rel_line_to`, :meth:`Context.rel_curve_to`,
        :meth:`Context.arc`, :meth:`Context.arc_negative`,
        :meth:`Context.rectangle`, :meth:`Context.text_path`,
        :meth:`Context.glyph_path`.

        Some functions use and alter the current point but do not otherwise
        change current path:
        :meth:`Context.show_text`.

        Some functions unset the current path and as a result, current point:
        :meth:`Context.fill`, :meth:`Context.stroke`.
        """

    def get_dash(self) -> Tuple[List[float], float]:
        """
        :returns: (dashes, offset)

        * *dashes*: return value as a tuple for the dash array
        * *offset*: return value as float for the current dash offset

        Gets the current dash array.

        .. versionadded:: 1.4
        """

    def get_dash_count(self) -> int:
        """
        :returns: the length of the dash array, or 0 if no dash array set.

        See also :meth:`Context.set_dash` and :meth:`Context.get_dash`.

        .. versionadded:: 1.4
        """

    def get_fill_rule(self) -> FillRule:
        """
        :returns: the current fill rule, as
            set by :meth:`Context.set_fill_rule`.
        """

    def get_font_face(self) -> FontFace:
        """
        :returns: the current :class:`FontFace` for the :class:`Context`.
        """

    def get_font_matrix(self) -> Matrix:
        """
        :returns: the current :class:`Matrix` for the :class:`Context`.

        See :meth:`Context.set_font_matrix`.
        """

    def get_font_options(self) -> FontOptions:
        """
        :returns: the current :class:`FontOptions` for the :class:`Context`.

        Retrieves font rendering options set via
        :meth:`Context.set_font_options`. Note that the returned options do not
        include any options derived from the underlying surface; they are
        literally the options passed to :meth:`Context.set_font_options`.
        """

    def get_group_target(self) -> Surface:
        """
        :returns: the target :class:`Surface`.

        Gets the current destination :class:`Surface` for the
        :class:`Context`. This is either the original target surface as passed
        to :class:`Context` or the target surface for the current group as
        started by the most recent call to :meth:`Context.push_group` or
        :meth:`Context.push_group_with_content`.

        .. versionadded:: 1.2
        """

    def get_hairline(self) -> bool:
        """
        :returns: whether hairline mode is set.

        Returns whether or not hairline mode is set, as set by
        :meth:`Context.set_hairline`.

        .. versionadded:: 1.23 Only available with cairo 1.17.6+
        """

    def get_line_cap(self) -> LineCap:
        """
        :returns: the current line cap style, as
            set by :meth:`Context.set_line_cap`.
        """

    def get_line_join(self) -> LineJoin:
        """
        :returns: the current line join style, as
            set by :meth:`Context.set_line_join`.
        """

    def get_line_width(self) -> float:
        """
        :returns: the current line width

        This function returns the current line width value exactly as set by
        :meth:`Context.set_line_width`. Note that the value is unchanged even if
        the CTM has changed between the calls to :meth:`Context.set_line_width`
        and :meth:`.get_line_width`.
        """

    def get_matrix(self) -> Matrix:
        """
        :returns: the current transformation :class:`Matrix` (CTM)
        """

    def get_miter_limit(self) -> float:
        """
        :returns: the current miter limit, as set by
            :meth:`Context.set_miter_limit`.
        """

    def get_operator(self) -> Operator:
        """
        :returns: the current compositing operator
            for a :class:`Context`.
        """

    def get_scaled_font(self) -> ScaledFont:
        """
        :returns: the current :class:`ScaledFont` for a :class:`Context`.

        .. versionadded:: 1.4
        """

    def get_source(self) -> Pattern:
        """
        :returns: the current source :class:`Pattern` for  a :class:`Context`.
        """

    def get_target(self) -> _SomeSurface:
        """
        :returns: the target :class:`Surface` for the :class:`Context`
        """

    def get_tolerance(self) -> float:
        """
        :returns: the current tolerance value, as set by
            :meth:`Context.set_tolerance`
        """

    def glyph_extents(self, glyphs: Sequence[Glyph]) -> TextExtents:
        """
        :param glyphs: glyphs, a sequence of :class:`Glyph`

        Gets the extents for an array of glyphs. The extents describe a
        user-space rectangle that encloses the "inked" portion of the glyphs,
        (as they would be drawn by :meth:`Context.show_glyphs`). Additionally,
        the x_advance and y_advance values indicate the amount by which the
        current point would be advanced by :meth:`Context.show_glyphs`.

        Note that whitespace glyphs do not contribute to the size of the
        rectangle (extents.width and extents.height).
        """

    def glyph_path(self, glyphs: Sequence[Glyph]) -> None:
        """
        :param glyphs: glyphs to show, a sequence of :class:`Glyph`

        Adds closed paths for the glyphs to the current path. The generated path
        if filled, achieves an effect similar to that of
        :meth:`Context.show_glyphs`.
        """

    def has_current_point(self) -> bool:
        """
        :returns: True iff a current point is defined on the current path.
            See :meth:`Context.get_current_point` for details on the current point.

        .. versionadded:: 1.6
        """

    def identity_matrix(self) -> None:
        """
        Resets the current transformation :class:`Matrix` (CTM) by setting it
        equal to the identity matrix. That is, the user-space and device-space
        axes will be aligned and one user-space unit will transform to one
        device-space unit.
        """

    def in_clip(self, x: float, y: float) -> bool:
        """
        :param x: X coordinate of the point to test
        :param y: Y coordinate of the point to test
        :returns: :obj:`True` if the point is inside, or :obj:`False` if outside.

        Tests whether the given point is inside the area that would be visible
        through the current clip, i.e. the area that would be filled by a
        :meth:`paint` operation.

        See :meth:`clip`, and :meth:`clip_preserve`.

        .. versionadded:: 1.12.0
        """

    def in_fill(self, x: float, y: float) -> bool:
        """
        :param x: X coordinate of the point to test
        :param y: Y coordinate of the point to test
        :returns: True iff the point is inside the area that would be affected
            by a :meth:`Context.fill` operation given the current path and filling
            parameters. Surface dimensions and clipping are not taken into account.

        See :meth:`Context.fill`, :meth:`Context.set_fill_rule` and
        :meth:`Context.fill_preserve`.
        """

    def in_stroke(self, x: float, y: float) -> bool:
        """
        :param x: X coordinate of the point to test
        :param y: Y coordinate of the point to test

        :returns: True iff the point is inside the area that would be affected
            by a :meth:`Context.stroke` operation given the current path and
            stroking parameters. Surface dimensions and clipping are not taken
            into account.

        See :meth:`Context.stroke`, :meth:`Context.set_line_width`,
        :meth:`Context.set_line_join`, :meth:`Context.set_line_cap`,
        :meth:`Context.set_dash`, and :meth:`Context.stroke_preserve`.
        """

    def line_to(self, x: float, y: float) -> None:
        """
        :param x: the X coordinate of the end of the new line
        :param y: the Y coordinate of the end of the new line

        Adds a line to the path from the current point to position *(x, y)* in
        user-space coordinates. After this call the current point will be *(x,
        y)*.

        If there is no current point before the call to :meth:`.line_to`
        this function will behave as ``ctx.move_to(x, y)``.
        """

    def mask(self, pattern: Pattern) -> None:
        """
        :param pattern: a :class:`Pattern`

        A drawing operator that paints the current source using the alpha
        channel of *pattern* as a mask. (Opaque areas of *pattern* are painted
        with the source, transparent areas are not painted.)
        """

    def mask_surface(self, surface: Surface, x: float = 0.0, y: float = 0.0) -> None:
        """
        :param surface: a :class:`Surface`
        :param x: X coordinate at which to place the origin of *surface*
        :param y: Y coordinate at which to place the origin of *surface*

        A drawing operator that paints the current source using the alpha
        channel of *surface* as a mask. (Opaque areas of *surface* are painted
        with the source, transparent areas are not painted.)
        """

    def move_to(self, x: float, y: float) -> None:
        """
        :param x: the X coordinate of the new position
        :param y: the Y coordinate of the new position

        Begin a new sub-path. After this call the current point will be *(x,
        y)*.
        """

    def new_path(self) -> None:
        """
        Clears the current path. After this call there will be no path and no
        current point.
        """

    def new_sub_path(self) -> None:
        """
        Begin a new sub-path. Note that the existing path is not affected. After
        this call there will be no current point.

        In many cases, this call is not needed since new sub-paths are
        frequently started with :meth:`Context.move_to`.

        A call to :meth:`.new_sub_path` is particularly useful when beginning a
        new sub-path with one of the :meth:`Context.arc` calls. This makes
        things easier as it is no longer necessary to manually compute the arc's
        initial coordinates for a call to :meth:`Context.move_to`.

        .. versionadded:: 1.6
        """

    def paint(self) -> None:
        """
        A drawing operator that paints the current source everywhere within the
        current clip region.
        """

    def paint_with_alpha(self, alpha: float) -> None:
        """
        :param alpha: alpha value, between 0 (transparent) and 1 (opaque)

        A drawing operator that paints the current source everywhere within the
        current clip region using a mask of constant alpha value *alpha*. The
        effect is similar to :meth:`Context.paint`, but the drawing is faded out
        using the alpha value.
        """

    def path_extents(self) -> Tuple[float, float, float, float]:
        """
        :returns: (x1, y1, x2, y2), all float

        * *x1*: left of the resulting extents
        * *y1*: top of the resulting extents
        * *x2*: right of the resulting extents
        * *y2*: bottom of the resulting extents

        Computes a bounding box in user-space coordinates covering the points on
        the current path. If the current path is empty, returns an empty
        rectangle (0, 0, 0, 0). Stroke parameters, fill rule, surface
        dimensions and clipping are not taken into account.

        Contrast with :meth:`Context.fill_extents` and
        :meth:`Context.stroke_extents` which return the extents of only the area
        that would be "inked" by the corresponding drawing operations.

        The result of :meth:`.path_extents` is defined as equivalent to the
        limit of :meth:`Context.stroke_extents` with cairo.LINE_CAP_ROUND as the
        line width approaches 0.0, (but never reaching the empty-rectangle
        returned by :meth:`Context.stroke_extents` for a line width of 0.0).

        Specifically, this means that zero-area sub-paths such as
        :meth:`Context.move_to`; :meth:`Context.line_to` segments, (even
        degenerate cases where the coordinates to both calls are identical),
        will be considered as contributing to the extents. However, a lone
        :meth:`Context.move_to` will not contribute to the results of
        :meth:`Context.path_extents`.

        .. versionadded:: 1.6
        """

    def pop_group(self) -> SurfacePattern:
        """
        :returns: a newly created :class:`SurfacePattern` containing the results
            of all drawing operations performed to the group.

        Terminates the redirection begun by a call to :meth:`Context.push_group`
        or :meth:`Context.push_group_with_content` and returns a new pattern
        containing the results of all drawing operations performed to the group.

        The :meth:`.pop_group` function calls :meth:`Context.restore`,
        (balancing a call to :meth:`Context.save` by the
        :meth:`Context.push_group` function), so that any changes to the graphics
        state will not be visible outside the group.

        .. versionadded:: 1.2
        """

    def pop_group_to_source(self) -> None:
        """
        Terminates the redirection begun by a call to :meth:`Context.push_group`
        or :meth:`Context.push_group_with_content` and installs the resulting
        pattern as the source :class:`Pattern` in the given :class:`Context`.

        The behavior of this function is equivalent to the sequence of
        operations::

            group = cairo_pop_group()
            ctx.set_source(group)

        but is more convenient as their is no need for a variable to store
        the short-lived pointer to the pattern.

        The :meth:`Context.pop_group` function calls :meth:`Context.restore`,
        (balancing a call to :meth:`Context.save` by the
        :meth:`Context.push_group` function), so that any changes to the graphics
        state will not be visible outside the group.

        .. versionadded:: 1.2
        """

    def push_group(self) -> None:
        """
        Temporarily redirects drawing to an intermediate surface known as a
        group. The redirection lasts until the group is completed by a call to
        :meth:`Context.pop_group` or :meth:`Context.pop_group_to_source`. These
        calls provide the result of any drawing to the group as a pattern,
        (either as an explicit object, or set as the source pattern).

        This group functionality can be convenient for performing intermediate
        compositing. One common use of a group is to render objects as opaque
        within the group, (so that they occlude each other), and then blend the
        result with translucence onto the destination.

        Groups can be nested arbitrarily deep by making balanced calls to
        :meth:`Context.push_group`/:meth:`Context.pop_group`. Each call
        pushes/pops the new target group onto/from a stack.

        The :meth:`.push_group` function calls :meth:`Context.save` so that any
        changes to the graphics state will not be visible outside the group,
        (the pop_group functions call :meth:`Context.restore`).

        By default the intermediate group will have a :class:`cairo.Content`
        type of :attr:`cairo.Content.COLOR_ALPHA`. Other content types can be
        chosen for the group by using :meth:`Context.push_group_with_content`
        instead.

        As an example, here is how one might fill and stroke a path with
        translucence, but without any portion of the fill being visible
        under the stroke::

            ctx.push_group()
            ctx.set_source(fill_pattern)
            ctx.fill_preserve()
            ctx.set_source(stroke_pattern)
            ctx.stroke()
            ctx.pop_group_to_source()
            ctx.paint_with_alpha(alpha)

        .. versionadded:: 1.2
        """

    def push_group_with_content(self, content: Content) -> None:
        """
        :param cairo.Content content: a content indicating the
            type of group that will be created

        Temporarily redirects drawing to an intermediate surface known as a
        group. The redirection lasts until the group is completed by a call to
        :meth:`Context.pop_group` or :meth:`Context.pop_group_to_source`. These
        calls provide the result of any drawing to the group as a pattern,
        (either as an explicit object, or set as the source pattern).

        The group will have a content type of *content*. The ability to control
        this content type is the only distinction between this function and
        :meth:`Context.push_group` which you should see for a more detailed
        description of group rendering.

        .. versionadded:: 1.2
        """

    def rectangle(self, x: float, y: float, width: float, height: float) -> None:
        """
        :param x: the X coordinate of the top left corner of the rectangle
        :param y: the Y coordinate to the top left corner of the rectangle
        :param width: the width of the rectangle
        :param height: the height of the rectangle

        Adds a closed sub-path rectangle of the given size to the current path
        at position *(x, y)* in user-space coordinates.

        This function is logically equivalent to::

            ctx.move_to(x, y)
            ctx.rel_line_to(width, 0)
            ctx.rel_line_to(0, height)
            ctx.rel_line_to(-width, 0)
            ctx.close_path()
        """

    def rel_curve_to(self, dx1: float, dy1: float, dx2: float, dy2: float, dx3: float, dy3: float) -> None:
        """
        :param dx1: the X offset to the first control point
        :param dy1: the Y offset to the first control point
        :param dx2: the X offset to the second control point
        :param dy2: the Y offset to the second control point
        :param dx3: the X offset to the end of the curve
        :param dy3: the Y offset to the end of the curve
        :raises: :exc:`cairo.Error` if called with no current point.

        Relative-coordinate version of :meth:`Context.curve_to`. All
        offsets are relative to the current point. Adds a cubic Bézier spline to
        the path from the current point to a point offset from the current point
        by *(dx3, dy3)*, using points offset by *(dx1, dy1)* and *(dx2, dy2)* as
        the control points. After this call the current point will be offset by
        *(dx3, dy3)*.

        Given a current point of (x, y), ``ctx.rel_curve_to(dx1, dy1, dx2, dy2,
        dx3, dy3)`` is logically equivalent to ``ctx.curve_to(x+dx1, y+dy1,
        x+dx2, y+dy2, x+dx3, y+dy3)``.
        """

    def rel_line_to(self, dx: float, dy: float) -> None:
        """
        :param dx: the X offset to the end of the new line
        :param dy: the Y offset to the end of the new line
        :raises: :exc:`cairo.Error` if called with no current point.

        Relative-coordinate version of :meth:`Context.line_to`. Adds a line to
        the path from the current point to a point that is offset from the
        current point by *(dx, dy)* in user space. After this call the current
        point will be offset by *(dx, dy)*.

        Given a current point of (x, y), ``ctx.rel_line_to(dx, dy)`` is logically
        equivalent to ``ctx.line_to(x + dx, y + dy)``.
        """

    def rel_move_to(self, dx: float, dy: float) -> None:
        """
        :param dx: the X offset
        :param dy: the Y offset
        :raises: :exc:`cairo.Error` if called with no current point.

        Begin a new sub-path. After this call the current point will offset by
        *(dx, dy)*.

        Given a current point of (x, y), ``ctx.rel_move_to(dx, dy)`` is logically
        equivalent to ``ctx.(x + dx, y + dy)``.
        """

    def reset_clip(self) -> None:
        """
        Reset the current clip region to its original, unrestricted state. That
        is, set the clip region to an infinitely large shape containing the
        target surface. Equivalently, if infinity is too hard to grasp, one can
        imagine the clip region being reset to the exact bounds of the target
        surface.

        Note that code meant to be reusable should not call :meth:`.reset_clip`
        as it will cause results unexpected by higher-level code which calls
        :meth:`.clip`. Consider using :meth:`.save` and :meth:`.restore` around
        :meth:`.clip` as a more robust means of temporarily restricting the clip
        region.
        """

    def restore(self) -> None:
        """
        Restores :class:`Context` to the state saved by a preceding call to
        :meth:`.save` and removes that state from the stack of saved states.
        """

    def rotate(self, angle: float) -> None:
        """
        :param angle: angle (in radians) by which the user-space axes will be
            rotated

        Modifies the current transformation matrix (CTM) by rotating the
        user-space axes by *angle* radians. The rotation of the axes takes places
        after any existing transformation of user space. The rotation direction
        for positive angles is from the positive X axis toward the positive Y
        axis.
        """

    def save(self) -> None:
        """
        Makes a copy of the current state of :class:`Context` and saves it on an
        internal stack of saved states. When :meth:`.restore` is called,
        :class:`Context` will be restored to the saved state. Multiple calls to
        :meth:`.save` and :meth:`.restore` can be nested; each call to
        :meth:`.restore` restores the state from the matching paired
        :meth:`.save`.
        """

    def scale(self, sx: float, sy: float) -> None:
        """
        :param sx: scale factor for the X dimension
        :param sy: scale factor for the Y dimension

        Modifies the current transformation matrix (CTM) by scaling the X and Y
        user-space axes by *sx* and *sy* respectively. The scaling of the axes
        takes place after any existing transformation of user space.
        """

    def select_font_face(self, family: str, slant: FontSlant = FontSlant.NORMAL, weight: FontWeight = FontWeight.NORMAL) -> None:
        """
        :param family: a font family name
        :param slant: the font slant of the font,
            defaults to :attr:`cairo.FontSlant.NORMAL`.
        :param weight: the font weight of the
            font, defaults to :attr:`cairo.FontWeight.NORMAL`.

        Note: The :meth:`.select_font_face` function call is part of what the
        cairo designers call the "toy" text API. It is convenient for short
        demos and simple programs, but it is not expected to be adequate for
        serious text-using applications.

        Selects a family and style of font from a simplified description as a
        family name, slant and weight. Cairo provides no operation to list
        available family names on the system (this is a "toy", remember), but
        the standard CSS2 generic family names, ("serif", "sans-serif",
        "cursive", "fantasy", "monospace"), are likely to work as expected.

        For "real" font selection, see the font-backend-specific
        font_face_create functions for the font backend you are using. (For
        example, if you are using the freetype-based cairo-ft font backend, see
        cairo_ft_font_face_create_for_ft_face() or
        cairo_ft_font_face_create_for_pattern().) The resulting font face could
        then be used with cairo_scaled_font_create() and
        cairo_set_scaled_font().

        Similarly, when using the "real" font support, you can call directly
        into the underlying font system, (such as fontconfig or freetype), for
        operations such as listing available fonts, etc.

        It is expected that most applications will need to use a more
        comprehensive font handling and text layout library, (for example,
        pango), in conjunction with cairo.

        If text is drawn without a call to :meth:`.select_font_face`, (nor
        :meth:`.set_font_face` nor :meth:`.set_scaled_font`), the default family
        is platform-specific, but is essentially "sans-serif".  Default slant is
        :attr:`cairo.FontSlant.NORMAL`, and default weight is
        :attr:`cairo.FontWeight.NORMAL`.

        This function is equivalent to a call to :class:`ToyFontFace`
        followed by :meth:`.set_font_face`.
        """

    def set_antialias(self, antialias: Antialias) -> None:
        """
        :param antialias: the new antialias mode

        Set the antialiasing mode of the rasterizer used for drawing shapes.
        This value is a hint, and a particular backend may or may not support a
        particular value.  At the current time, no backend supports
        :attr:`cairo.Antialias.SUBPIXEL` when drawing shapes.

        Note that this option does not affect text rendering, instead see
        :meth:`FontOptions.set_antialias`.
        """

    def set_dash(self, dashes: Sequence[float], offset: float = 0) -> None:
        """
        :param dashes: a sequence specifying alternate lengths of on and off
            stroke portions as float.
        :param offset: an offset into the dash pattern at which the stroke
            should start, defaults to 0.
        :raises: :exc:`cairo.Error` if any value in *dashes* is negative, or if
            all values are 0.

        Sets the dash pattern to be used by :meth:`.stroke`. A dash pattern is
        specified by *dashes* - a sequence of positive values. Each value
        provides the length of alternate "on" and "off" portions of the
        stroke. The *offset* specifies an offset into the pattern at which the
        stroke begins.

        Each "on" segment will have caps applied as if the segment were a
        separate sub-path. In particular, it is valid to use an "on" length of
        0.0 with :attr:`cairo.LineCap.ROUND` or :attr:`cairo.LineCap.SQUARE`
        in order to distributed dots or squares along a path.

        Note: The length values are in user-space units as evaluated at the time
        of stroking. This is not necessarily the same as the user space at the
        time of :meth:`.set_dash`.

        If the number of dashes is 0 dashing is disabled.

        If the number of dashes is 1 a symmetric pattern is assumed with
        alternating on and off portions of the size specified by the single
        value in *dashes*.
        """

    def set_fill_rule(self, fill_rule: FillRule) -> None:
        """
        :param fill_rule: a fill rule to set the
            within the cairo context. The fill rule is used to determine which
            regions are inside or outside a complex (potentially
            self-intersecting) path. The current fill rule affects both
            :meth:`.fill` and :meth:`.clip`.

        The default fill rule is :attr:`cairo.FillRule.WINDING`.
        """

    def set_font_face(self, font_face: Optional[FontFace]) -> None:
        """
        :param font_face: a :class:`FontFace`, or None to restore to the
            default :class:`FontFace`

        Replaces the current :class:`FontFace` object in the :class:`Context`
        with *font_face*.
        """

    def set_font_matrix(self, matrix: Matrix) -> None:
        """
        :param matrix: a :class:`Matrix` describing a transform to be applied to
            the current font.

        Sets the current font matrix to *matrix*. The font matrix gives a
        transformation from the design space of the font (in this space, the
        em-square is 1 unit by 1 unit) to user space. Normally, a simple scale
        is used (see :meth:`.set_font_size`), but a more complex font matrix can
        be used to shear the font or stretch it unequally along the two axes
        """

    def set_font_options(self, options: FontOptions) -> None:
        """
        :param options: :class:`FontOptions` to use

        Sets a set of custom font rendering options for the :class:`Context`.
        Rendering options are derived by merging these options with the options
        derived from underlying surface; if the value in *options* has a default
        value (like :attr:`cairo.Antialias.DEFAULT`), then the value from the
        surface is used.
        """

    def set_font_size(self, size: float) -> None:
        """
        :param size: the new font size, in user space units

        Sets the current font matrix to a scale by a factor of *size*, replacing
        any font matrix previously set with :meth:`.set_font_size` or
        :meth:`.set_font_matrix`. This results in a font size of *size* user
        space units. (More precisely, this matrix will result in the font's
        em-square being a *size* by *size* square in user space.)

        If text is drawn without a call to :meth:`.set_font_size`, (nor
        :meth:`.set_font_matrix` nor :meth:`.set_scaled_font`), the default font
        size is 10.0.
        """

    def set_hairline(self, set_hairline: bool) -> None:
        """
        :param set_hairline: whether or not to set hairline mode

        Sets lines within the cairo context to be hairlines. Hairlines are
        logically zero-width lines that are drawn at the thinnest renderable
        width possible in the current context. On surfaces with native hairline
        support, the native hairline functionality will be used. Surfaces that
        support hairlines include:

        - pdf/ps: Encoded as 0-width line.
        - win32_printing: Rendered with PS_COSMETIC pen.
        - svg: Encoded as 1px non-scaling-stroke.
        - script: Encoded with set-hairline function.

        Cairo will always render hairlines at 1 device unit wide, even if an
        anisotropic scaling was applied to the stroke width. In the wild,
        handling of this situation is not well-defined. Some PDF, PS, and SVG
        renderers match Cairo's output, but some very popular implementations
        (Acrobat, Chrome, rsvg) will scale the hairline unevenly. As such, best
        practice is to reset any anisotropic scaling before calling
        :meth:`.stroke`. See https://cairographics.org/cookbook/ellipses/ for an
        example.

        .. versionadded:: 1.23 Only available with cairo 1.17.6+
        """

    def set_line_cap(self, line_cap: LineCap) -> None:
        """
        :param line_cap: a line cap style

        Sets the current line cap style within the :class:`Context`.

        As with the other stroke parameters, the current line cap style is
        examined by :meth:`.stroke` and :meth:`.stroke_extents`, but does not
        have any effect during path construction.

        The default line cap style is :attr:`cairo.LineCap.BUTT`.
        """

    def set_line_join(self, line_join: LineJoin) -> None:
        """
        :param line_join: a line join style

        Sets the current line join style within the :class:`Context`.

        As with the other stroke parameters, the current line join style is
        examined by :meth:`.stroke` and :meth:`.stroke_extents`, but does not
        have any effect during path construction.

        The default line join style is :attr:`cairo.LineJoin.MITER`.
        """

    def set_line_width(self, width: float) -> None:
        """
        :param width: a line width

        Sets the current line width within the :class:`Context`. The line width
        value specifies the diameter of a pen that is circular in user space,
        (though device-space pen may be an ellipse in general due to
        scaling/shear/rotation of the CTM).

        Note: When the description above refers to user space and CTM it refers
        to the user space and CTM in effect at the time of the stroking
        operation, not the user space and CTM in effect at the time of the call
        to :meth:`.set_line_width`. The simplest usage makes both of these
        spaces identical. That is, if there is no change to the CTM between a
        call to :meth:`.set_line_width` and the stroking operation, then one can
        just pass user-space values to :meth:`.set_line_width` and ignore this
        note.

        As with the other stroke parameters, the current line width is examined
        by :meth:`.stroke` and :meth:`.stroke_extents`, but does not have any
        effect during path construction.

        The default line width value is 2.0.
        """

    def set_matrix(self, matrix: Matrix) -> None:
        """
        :param matrix: a transformation :class:`Matrix` from user space to
            device space.

        Modifies the current transformation matrix (CTM) by setting it equal to
        *matrix*.
        """

    def set_miter_limit(self, limit: float) -> None:
        """
        :param limit: miter limit to set

        Sets the current miter limit within the :class:`Context`.

        If the current line join style is set to :attr:`cairo.LineJoin.MITER`
        (see :meth:`.set_line_join`), the miter limit is used to determine
        whether the lines should be joined with a bevel instead of a miter.
        Cairo divides the length of the miter by the line width. If the result
        is greater than the miter limit, the style is converted to a bevel.

        As with the other stroke parameters, the current line miter limit is
        examined by :meth:`.stroke` and :meth:`.stroke_extents`, but does not
        have any effect during path construction.

        The default miter limit value is 10.0, which will convert joins with
        interior angles less than 11 degrees to bevels instead of miters. For
        reference, a miter limit of 2.0 makes the miter cutoff at 60 degrees,
        and a miter limit of 1.414 makes the cutoff at 90 degrees.

        A miter limit for a desired angle can be computed as::

            miter limit = 1/math.sin(angle/2)
        """

    def set_operator(self, op: Operator) -> None:
        """
        :param op: the compositing operator to set
            for use in all drawing operations.

        The default operator is :attr:`cairo.Operator.OVER`.
        """

    def set_scaled_font(self, scaled_font: ScaledFont) -> None:
        """
        :param scaled_font: a :class:`ScaledFont`

        Replaces the current font face, font matrix, and font options in the
        :class:`Context` with those of the :class:`ScaledFont`. Except for some
        translation, the current CTM of the :class:`Context` should be the same
        as that of the :class:`ScaledFont`, which can be accessed using
        :meth:`ScaledFont.get_ctm`.

        .. versionadded:: 1.2
        """

    def set_source(self, source: Pattern) -> None:
        """
        :param source: a :class:`Pattern` to be used as the source for
            subsequent drawing operations.

        Sets the source pattern within :class:`Context` to *source*. This
        pattern will then be used for any subsequent drawing operation until a
        new source pattern is set.

        Note: The pattern's transformation matrix will be locked to the user
        space in effect at the time of :meth:`.set_source`. This means that
        further modifications of the current transformation matrix will not
        affect the source pattern. See :meth:`Pattern.set_matrix`.

        The default source pattern is a solid pattern that is opaque black,
        (that is, it is equivalent to ``set_source_rgb(0.0, 0.0, 0.0)``.
        """

    def set_source_rgb(self, red: float, green: float, blue: float) -> None:
        """
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color

        Sets the source pattern within :class:`Context` to an opaque color. This
        opaque color will then be used for any subsequent drawing operation
        until a new source pattern is set.

        The color components are floating point numbers in the range 0 to
        1. If the values passed in are outside that range, they will be
        clamped.

        The default source pattern is opaque black, (that is, it is
        equivalent to ``set_source_rgb(0.0, 0.0, 0.0)``.
        """

    def set_source_rgba(self, red: float, green: float, blue: float, alpha: float = 1.0) -> None:
        """
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color
        :param alpha: alpha component of color

        Sets the source pattern within :class:`Context` to a translucent
        color. This color will then be used for any subsequent drawing operation
        until a new source pattern is set.

        The color and alpha components are floating point numbers in the range 0
        to 1. If the values passed in are outside that range, they will be
        clamped.

        The default source pattern is opaque black, (that is, it is
        equivalent to ``set_source_rgba(0.0, 0.0, 0.0, 1.0)``.
        """

    def set_source_surface(self, surface: Surface, x: float = 0.0, y: float = 0.0) -> None:
        """
        :param surface: a :class:`Surface` to be used to set the source pattern
        :param x: User-space X coordinate for surface origin
        :param y: User-space Y coordinate for surface origin

        This is a convenience function for creating a pattern from a
        :class:`Surface` and setting it as the source in :class:`Context` with
        :meth:`.set_source`.

        The *x* and *y* parameters give the user-space coordinate at which the
        surface origin should appear. (The surface origin is its upper-left
        corner before any transformation has been applied.) The *x* and *y*
        patterns are negated and then set as translation values in the pattern
        matrix.

        Other than the initial translation pattern matrix, as described above,
        all other pattern attributes, (such as its extend mode), are set to the
        default values as in :class:`SurfacePattern`.  The resulting pattern can
        be queried with :meth:`.get_source` so that these attributes can be
        modified if desired, (eg. to create a repeating pattern with
        :meth:`.Pattern.set_extend`).
        """

    def set_tolerance(self, tolerance: float) -> None:
        """
        :param tolerance: the tolerance, in device units (typically pixels)

        Sets the tolerance used when converting paths into trapezoids.  Curved
        segments of the path will be subdivided until the maximum deviation
        between the original path and the polygonal approximation is less than
        *tolerance*. The default value is 0.1. A larger value will give better
        performance, a smaller value, better appearance. (Reducing the value
        from the default value of 0.1 is unlikely to improve appearance
        significantly.)  The accuracy of paths within Cairo is limited by the
        precision of its internal arithmetic, and the prescribed *tolerance* is
        restricted to the smallest representable internal value.
        """

    def show_glyphs(self, glyphs: Sequence[Glyph]) -> None:
        """
        :param glyphs: glyphs to show as a sequence of :class:`Glyph`

        A drawing operator that generates the shape from an array of glyphs,
        rendered according to the current font face, font size (font matrix),
        and font options.
        """

    def show_page(self) -> None:
        """
        Emits and clears the current page for backends that support multiple
        pages. Use :meth:`.copy_page` if you don't want to clear the page.

        This is a convenience function that simply calls
        ``ctx.get_target() . show_page()``
        """

    def show_text(self, text: str) -> None:
        """
        :param text: text

        A drawing operator that generates the shape from a string of text,
        rendered according to the current font_face, font_size (font_matrix),
        and font_options.

        This function first computes a set of glyphs for the string of text. The
        first glyph is placed so that its origin is at the current point. The
        origin of each subsequent glyph is offset from that of the previous
        glyph by the advance values of the previous glyph.

        After this call the current point is moved to the origin of where the
        next glyph would be placed in this same progression. That is, the
        current point will be at the origin of the final glyph offset by its
        advance values. This allows for easy display of a single logical string
        with multiple calls to :meth:`.show_text`.

        Note: The :meth:`.show_text` function call is part of what the cairo
        designers call the "toy" text API. It is convenient for short demos
        and simple programs, but it is not expected to be adequate for
        serious text-using applications. See :meth:`.show_glyphs` for the
        "real" text display API in cairo.
        """

    def show_text_glyphs(self, utf8: str, glyphs: List["Glyph"], clusters: List[TextCluster], cluster_flags: TextClusterFlags) -> None:
        """
        :param utf8: a string of text
        :param glyphs: list of glyphs to show
        :param clusters: list of cluster mapping information
        :param cluster_flags: cluster mapping flags
        :raises Error:

        .. versionadded:: 1.15

        This operation has rendering effects similar to
        :meth:`Context.show_glyphs` but, if the target surface supports it, uses
        the provided text and cluster mapping to embed the text for the glyphs
        shown in the output. If the target does not support the extended
        attributes, this function acts like the basic
        :meth:`Context.show_glyphs` as if it had been passed ``glyphs`` .

        The mapping between utf8 and glyphs is provided by a list of clusters.
        Each cluster covers a number of text bytes and glyphs, and neighboring
        clusters cover neighboring areas of utf8 and glyphs . The clusters
        should collectively cover utf8 and glyphs in entirety.

        The first cluster always covers bytes from the beginning of utf8 . If
        ``cluster_flags`` do not have the :attr:`TextClusterFlags.BACKWARD` set,
        the first cluster also covers the beginning of glyphs , otherwise it
        covers the end of the glyphs array and following clusters move backward.

        See :class:`TextCluster` for constraints on valid clusters.
        """

    def stroke(self) -> None:
        """
        A drawing operator that strokes the current path according to the
        current line width, line join, line cap, and dash settings. After
        :meth:`.stroke`, the current path will be cleared from the cairo
        context. See :meth:`.set_line_width`, :meth:`.set_line_join`,
        :meth:`.set_line_cap`, :meth:`.set_dash`, and :meth:`.stroke_preserve`.

        Note: Degenerate segments and sub-paths are treated specially and
        provide a useful result. These can result in two different situations:

        1. Zero-length "on" segments set in :meth:`.set_dash`. If the cap
        style is :attr:`cairo.LineCap.ROUND` or :attr:`cairo.LineCap.SQUARE`
        then these segments will be drawn as circular dots or squares
        respectively. In the case of :attr:`cairo.LineCap.SQUARE`, the
        orientation of the squares is determined by the direction of the
        underlying path.

        2. A sub-path created by :meth:`.move_to` followed by either a
        :meth:`.close_path` or one or more calls to :meth:`.line_to` to the same
        coordinate as the :meth:`.move_to`. If the cap style is
        :attr:`cairo.LineCap.ROUND` then these sub-paths will be drawn as
        circular dots. Note that in the case of :attr:`cairo.LineCap.SQUARE` a
        degenerate sub-path will not be drawn at all, (since the correct
        orientation is indeterminate).

        In no case will a cap style of :attr:`cairo.LineCap.BUTT` cause anything
        to be drawn in the case of either degenerate segments or sub-paths.
        """

    def stroke_extents(self) -> Tuple[float, float, float, float]:
        """
        :returns: (x1, y1, x2, y2), all float

        * *x1*: left of the resulting extents
        * *y1*: top of the resulting extents
        * *x2*: right of the resulting extents
        * *y2*: bottom of the resulting extents

        Computes a bounding box in user coordinates covering the area that would
        be affected, (the "inked" area), by a :meth:`.stroke` operation given
        the current path and stroke parameters. If the current path is empty,
        returns an empty rectangle (0, 0, 0, 0). Surface dimensions and
        clipping are not taken into account.

        Note that if the line width is set to exactly zero, then
        :meth:`.stroke_extents` will return an empty rectangle. Contrast with
        :meth:`.path_extents` which can be used to compute the non-empty bounds
        as the line width approaches zero.

        Note that :meth:`.stroke_extents` must necessarily do more work to
        compute the precise inked areas in light of the stroke parameters, so
        :meth:`.path_extents` may be more desirable for sake of performance if
        non-inked path extents are desired.

        See :meth:`.stroke`, :meth:`.set_line_width`, :meth:`.set_line_join`,
        :meth:`.set_line_cap`, :meth:`.set_dash`, and :meth:`.stroke_preserve`.
        """

    def stroke_preserve(self) -> None:
        """
        A drawing operator that strokes the current path according to the
        current line width, line join, line cap, and dash settings. Unlike
        :meth:`.stroke`, :meth:`.stroke_preserve` preserves the path within the
        cairo context.

        See :meth:`.set_line_width`, :meth:`.set_line_join`,
        :meth:`.set_line_cap`, :meth:`.set_dash`, and :meth:`.stroke_preserve`.
        """

    def tag_begin(self, tag_name: str, attributes: str) -> None:
        """
        :param tag_name: tag name
        :param attributes: tag attributes

        Marks the beginning of the tag_name structure. Call :meth:`tag_end`
        with the same tag_name to mark the end of the structure.

        The attributes string is of the form "key1=value2 key2=value2 ...".
        Values may be boolean (true/false or 1/0), integer, float, string, or
        an array.

        String values are enclosed in single quotes ('). Single quotes and
        backslashes inside the string should be escaped with a backslash.

        Boolean values may be set to true by only specifying the key. eg the
        attribute string "key" is the equivalent to "key=true".

        Arrays are enclosed in '[]'. eg "rect=[1.2 4.3 2.0 3.0]".

        If no attributes are required, attributes can be an empty string.

        See `Tags and Links Description
        <https://www.cairographics.org/manual/cairo-Tags-and-Links.html#cairo-Tags-and-Links.description>`__
        for the list of tags and attributes.

        Invalid nesting of tags or invalid attributes will cause the context
        to shutdown with a status of :attr:`Status.TAG_ERROR`.

        See :meth:`tag_end`.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def tag_end(self, tag_name: str) -> None:
        """
        :param tag_name: tag name

        Marks the end of the tag_name structure.

        Invalid nesting of tags will cause the context to shutdown with a
        status of :attr:`Status.TAG_ERROR`.

        See :meth:`tag_begin`.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def text_extents(self, text: str) -> TextExtents:
        """
        :param text: text to get extents for

        Gets the extents for a string of text. The extents describe a user-space
        rectangle that encloses the "inked" portion of the text, (as it would be
        drawn by :meth:`Context.show_text`). Additionally, the x_advance and
        y_advance values indicate the amount by which the current point would be
        advanced by :meth:`Context.show_text`.

        Note that whitespace characters do not directly contribute to the size
        of the rectangle (extents.width and extents.height). They do contribute
        indirectly by changing the position of non-whitespace characters. In
        particular, trailing whitespace characters are likely to not affect the
        size of the rectangle, though they will affect the x_advance and
        y_advance values.
        """

    def text_path(self, text: str) -> None:
        """
        :param text: text

        Adds closed paths for text to the current path. The generated path if
        filled, achieves an effect similar to that of :meth:`Context.show_text`.

        Text conversion and positioning is done similar to
        :meth:`Context.show_text`.

        Like :meth:`Context.show_text`, After this call the current point is
        moved to the origin of where the next glyph would be placed in this same
        progression. That is, the current point will be at the origin of the
        final glyph offset by its advance values.  This allows for chaining
        multiple calls to to :meth:`Context.text_path` without having to set
        current point in between.

        Note: The :meth:`.text_path` function call is part of what the cairo
        designers call the "toy" text API. It is convenient for short demos and
        simple programs, but it is not expected to be adequate for serious
        text-using applications. See :meth:`Context.glyph_path` for the "real"
        text path API in cairo.
        """

    def transform(self, matrix: Matrix) -> None:
        """
        :param matrix: a transformation :class:`Matrix` to be applied to the
            user-space axes

        Modifies the current transformation matrix (CTM) by applying *matrix* as
        an additional transformation. The new transformation of user space takes
        place after any existing transformation.
        """

    def translate(self, tx: float, ty: float) -> None:
        """
        :param tx: amount to translate in the X direction
        :param ty: amount to translate in the Y direction

        Modifies the current transformation matrix (CTM) by translating the
        user-space origin by *(tx, ty)*. This offset is interpreted as a
        user-space coordinate according to the CTM in place before the new call
        to :meth:`.translate`. In other words, the translation of the user-space
        origin takes place after any existing transformation.
        """

    def user_to_device(self, x: float, y: float) -> Tuple[float, float]:
        """
        :param x: X value of coordinate
        :param y: Y value of coordinate
        :returns: (x, y), both float

        * *x*: X value of coordinate
        * *y*: Y value of coordinate

        Transform a coordinate from user space to device space by multiplying
        the given point by the current transformation matrix (CTM).
        """

    def user_to_device_distance(self, dx: float, dy: float) -> Tuple[float, float]:
        """
        :param dx: X value of a distance vector
        :param dy: Y value of a distance vector
        :returns: (dx, dy), both float

        * *dx*: X value of a distance vector
        * *dy*: Y value of a distance vector

        Transform a distance vector from user space to device space. This
        function is similar to :meth:`Context.user_to_device` except that the
        translation components of the CTM will be ignored when transforming
        *(dx,dy)*.
        """

class Error(Exception):
    """This exception is raised when a cairo object returns an error status."""
    status: Status = ...

CairoError = Error
"""
An alias for :exc:`Error`

.. versionadded:: 1.12.0
"""

class Gradient(Pattern):
    """
    *Gradient* is an abstract base class from which other *Pattern* classes
    derive. It cannot be instantiated directly.
    """

    def add_color_stop_rgb(self, offset: float, red: float, green: float, blue: float) -> None:
        """
        :param offset: an offset in the range [0.0 .. 1.0]
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color

        Adds an opaque color stop to a *Gradient* pattern. The offset specifies
        the location along the gradient's control vector. For example, a
        *LinearGradient's* control vector is from (x0,y0) to (x1,y1) while a
        *RadialGradient's* control vector is from any point on the start circle
        to the corresponding point on the end circle.

        The color is specified in the same way as in :meth:`Context.set_source_rgb`.

        If two (or more) stops are specified with identical offset values, they
        will be sorted according to the order in which the stops are added,
        (stops added earlier will compare less than stops added later). This can
        be useful for reliably making sharp color transitions instead of the
        typical blend.
        """

    def add_color_stop_rgba(self, offset: float, red: float, green: float, blue: float, alpha: float) -> None:
        """
        :param offset: an offset in the range [0.0 .. 1.0]
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color
        :param alpha: alpha component of color

        Adds an opaque color stop to a *Gradient* pattern. The offset specifies
        the location along the gradient's control vector. For example, a
        *LinearGradient's* control vector is from (x0,y0) to (x1,y1) while a
        *RadialGradient's* control vector is from any point on the start circle
        to the corresponding point on the end circle.

        The color is specified in the same way as in :meth:`Context.set_source_rgb`.

        If two (or more) stops are specified with identical offset values, they
        will be sorted according to the order in which the stops are added,
        (stops added earlier will compare less than stops added later). This can
        be useful for reliably making sharp color transitions instead of the
        typical blend.
        """

    def get_color_stops_rgba(self) -> List[Tuple[float, float, float, float, float]]:
        """
        :returns: a list of (offset, red, green, blue, alpha) tuples of float

        Gets the color and offset information for all color stops specified in
        the given gradient pattern.

        .. versionadded:: 1.14
        """

class LinearGradient(Gradient):
    def __init__(self, x0: float, y0: float, x1: float, y1: float) -> None:
        """
        :param x0: x coordinate of the start point
        :param y0: y coordinate of the start point
        :param x1: x coordinate of the end point
        :param y1: y coordinate of the end point

        Create a new *LinearGradient* along the line defined by (x0, y0) and (x1,
        y1).  Before using the *Gradient* pattern, a number of color stops should
        be defined using :meth:`Gradient.add_color_stop_rgb` or
        :meth:`Gradient.add_color_stop_rgba`

        Note: The coordinates here are in pattern space. For a new *Pattern*,
        pattern space is identical to user space, but the relationship between the
        spaces can be changed with :meth:`Pattern.set_matrix`
        """

    def get_linear_points(self) -> Tuple[float, float, float, float]:
        """
        :returns: (x0, y0, x1, y1) - a tuple of float

            * x0: return value for the x coordinate of the first point
            * y0: return value for the y coordinate of the first point
            * x1: return value for the x coordinate of the second point
            * y1: return value for the y coordinate of the second point

        Gets the gradient endpoints for a *LinearGradient*.

        .. versionadded:: 1.4
        """

class MeshPattern(Pattern):
    """
    Mesh patterns are tensor-product patch meshes (type 7 shadings in PDF).
    Mesh patterns may also be used to create other types of shadings that are
    special cases of tensor-product patch meshes such as Coons patch meshes
    (type 6 shading in PDF) and Gouraud-shaded triangle meshes (type 4 and 5
    shadings in PDF).

    Mesh patterns consist of one or more tensor-product patches, which should
    be defined before using the mesh pattern. Using a mesh pattern with a
    partially defined patch as source or mask will put the context in an error
    status with a status of :attr:`cairo.Status.INVALID_MESH_CONSTRUCTION`.

    A tensor-product patch is defined by 4 Bézier curves (side 0, 1, 2, 3) and
    by 4 additional control points (P0, P1, P2, P3) that provide further
    control over the patch and complete the definition of the tensor-product
    patch. The corner C0 is the first point of the patch.

    Degenerate sides are permitted so straight lines may be used. A zero
    length line on one side may be used to create 3 sided patches.

    ::

              C1     Side 1       C2
               +---------------+
               |               |
               |  P1       P2  |
               |               |
        Side 0 |               | Side 2
               |               |
               |               |
               |  P0       P3  |
               |               |
               +---------------+
             C0     Side 3        C3

    Each patch is constructed by first calling :meth:`begin_patch`, then
    :meth:`move_to` to specify the first point in the patch (C0). Then the
    sides are specified with calls to :meth:`curve_to` and :meth:`line_to`.

    The four additional control points (P0, P1, P2, P3) in a patch can be
    specified with :meth:`set_control_point`.

    At each corner of the patch (C0, C1, C2, C3) a color may be specified with
    :meth:`set_corner_color_rgb` or :meth:`set_corner_color_rgba`. Any corner
    whose color is not explicitly specified defaults to transparent black.

    A Coons patch is a special case of the tensor-product patch where the
    control points are implicitly defined by the sides of the patch. The
    default value for any control point not specified is the implicit value
    for a Coons patch, i.e. if no control points are specified the patch is a
    Coons patch.

    A triangle is a special case of the tensor-product patch where the control
    points are implicitly defined by the sides of the patch, all the sides are
    lines and one of them has length 0, i.e. if the patch is specified using
    just 3 lines, it is a triangle. If the corners connected by the 0-length
    side have the same color, the patch is a Gouraud-shaded triangle.

    Patches may be oriented differently to the above diagram. For example the
    first point could be at the top left. The diagram only shows the
    relationship between the sides, corners and control points. Regardless of
    where the first point is located, when specifying colors, corner 0 will
    always be the first point, corner 1 the point between side 0 and side 1
    etc.

    Calling :meth:`end_patch` completes the current patch. If less than 4
    sides have been defined, the first missing side is defined as a line from
    the current point to the first point of the patch (C0) and the other sides
    are degenerate lines from C0 to C0. The corners between the added sides
    will all be coincident with C0 of the patch and their color will be set to
    be the same as the color of C0.

    Additional patches may be added with additional calls to
    :meth:`begin_patch`/:meth:`end_patch`.

    ::

        # Add a Coons patch
        pattern = cairo.MeshPattern()
        pattern.begin_patch()
        pattern.move_to(0, 0)
        pattern.curve_to(30, -30, 60, 30, 100, 0)
        pattern.curve_to(60, 30, 130, 60, 100, 100)
        pattern.curve_to(60, 70, 30, 130, 0, 100)
        pattern.curve_to(30, 70, -30, 30, 0, 0)
        pattern.set_corner_color_rgb(0, 1, 0, 0)
        pattern.set_corner_color_rgb(1, 0, 1, 0)
        pattern.set_corner_color_rgb(2, 0, 0, 1)
        pattern.set_corner_color_rgb(3, 1, 1, 0)
        pattern.end_patch()

        # Add a Gouraud-shaded triangle
        pattern = cairo.MeshPattern()
        pattern.begin_patch()
        pattern.move_to(100, 100)
        pattern.line_to(130, 130)
        pattern.line_to(130, 70)
        pattern.set_corner_color_rgb(0, 1, 0, 0)
        pattern.set_corner_color_rgb(1, 0, 1, 0)
        pattern.set_corner_color_rgb(2, 0, 0, 1)
        pattern.end_patch()

    When two patches overlap, the last one that has been added is drawn over
    the first one.

    When a patch folds over itself, points are sorted depending on their
    parameter coordinates inside the patch. The v coordinate ranges from 0 to
    1 when moving from side 3 to side 1; the u coordinate ranges from 0 to 1
    when going from side 0 to side

    Points with higher v coordinate hide points with lower v coordinate. When
    two points have the same v coordinate, the one with higher u coordinate is
    above. This means that points nearer to side 1 are above points nearer to
    side 3; when this is not sufficient to decide which point is above (for
    example when both points belong to side 1 or side 3) points nearer to side
    2 are above points nearer to side 0.

    For a complete definition of tensor-product patches, see the PDF
    specification (ISO32000), which describes the parametrization in detail.

    Note: The coordinates are always in pattern space. For a new pattern,
    pattern space is identical to user space, but the relationship between the
    spaces can be changed with :meth:`Pattern.set_matrix`.

    .. versionadded:: 1.14
    """

    def __init__(self) -> None:
        """
        Create a new mesh pattern.

        .. versionadded:: 1.14
        """

    def begin_patch(self) -> None:
        """
        :raises Error:

        Begin a patch in a mesh pattern.

        After calling this function, the patch shape should be defined with
        :meth:`move_to`, :meth:`line_to` and :meth:`curve_to`.

        After defining the patch, :meth:`end_patch` must be called before
        using pattern as a source or mask.
        """

    def curve_to(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        """
        :param x1: the X coordinate of the first control point
        :param y1: the Y coordinate of the first control point
        :param x2: the X coordinate of the second control point
        :param y2: the Y coordinate of the second control point
        :param x3: the X coordinate of the end of the curve
        :param y3: the Y coordinate of the end of the curve
        :raises Error:

        Adds a cubic Bézier spline to the current patch from the current point
        to position (x3 , y3 ) in pattern-space coordinates, using (x1 , y1 )
        and (x2 , y2 ) as the control points.

        If the current patch has no current point before the call to
        :meth:`curve_to`, this function will behave as if
        preceded by a call to ``pattern.move_to(x1, y1)``.

        After this call the current point will be (x3 , y3 ).
        """

    def end_patch(self) -> None:
        """
        :raises Error:

        Indicates the end of the current patch in a mesh pattern.

        If the current patch has less than 4 sides, it is closed with a
        straight line from the current point to the first point of the patch
        as if :meth:`line_to` was used.
        """

    def get_control_point(self, patch_num: int, point_num: int) -> Tuple[float, float]:
        """
        :param patch_num: the patch number to return data for
        :param point_num: he control point number to return data for
        :returns: a (x, y) tuple of float - coordinates of the control point
        :raises Error:

        Gets the control point point_num of patch patch_num for a mesh
        pattern.

        ``patch_num`` can range from 0 to n-1 where n is the number returned
        by :meth:`get_patch_count`.

        Valid values for ``point_num`` are from 0 to 3 and identify the control
        points as explained in :class:`MeshPattern`.
        """

    def get_corner_color_rgba(self, patch_num: int, corner_num: int) -> Tuple[float, float, float, float]:
        """
        :param patch_num: the patch number to return data for
        :param corner_num: the corner number to return data for
        :returns: a (red, green, blue, alpha) tuple of float
        :raises Error:

        Gets the color information in corner ``corner_num`` of patch
        ``patch_num`` for a mesh pattern.

        ``patch_num`` can range from 0 to n-1 where n is the number returned
        by :meth:`get_patch_count`.

        Valid values for ``corner_num`` are from 0 to 3 and identify the
        corners as explained in :class:`MeshPattern`.
        """

    def get_patch_count(self) -> int:
        """
        :returns: number of patches

        Gets the number of patches specified in the given mesh pattern.

        The number only includes patches which have been finished by calling
        :meth:`end_patch`. For example it will be 0 during the definition of
        the first patch.
        """

    def line_to(self, x: float, y: float) -> None:
        """
        :param x: the X coordinate of the end of the new line
        :param y: the Y coordinate of the end of the new line
        :raises Error:

        Adds a line to the current patch from the current point to position (x
        , y ) in pattern-space coordinates.

        If there is no current point before the call to :meth:`line_to` this
        function will behave as ``pattern.move_to(x ,y)``.

        After this call the current point will be (x , y ).
        """

    def move_to(self, x: float, y: float) -> None:
        """
        :param x: the X coordinate of the new position
        :param y: the Y coordinate of the new position
        :raises Error:

        Define the first point of the current patch in a mesh pattern.

        After this call the current point will be (x , y ).
        """

    def set_control_point(self, point_num: int, x: float, y: float) -> None:
        """
        :param point_num: the control point to set the position for
        :param x: the X coordinate of the control point
        :param y: the Y coordinate of the control point
        :raises Error:

        Set an internal control point of the current patch.

        Valid values for point_num are from 0 to 3 and identify the control
        points as explained in :class:`MeshPattern`.
        """

    def set_corner_color_rgb(self, corner_num: int, red: float, green: float, blue: float) -> None:
        """
        :param corner_num: the corner to set the color for
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color
        :raises Error:

        Sets the color of a corner of the current patch in a mesh pattern.

        The color is specified in the same way as in
        :meth:`Context.set_source_rgb`.

        Valid values for corner_num are from 0 to 3 and identify the corners
        as explained in :class:`MeshPattern`.
        """

    def set_corner_color_rgba(self, corner_num: int, red: float, green: float, blue: float, alpha: float) -> None:
        """
        :param corner_num: the corner to set the color for
        :param red: red component of color
        :param green: green component of color
        :param blue: blue component of color
        :param alpha: alpha component of color
        :raises Error:

        Sets the color of a corner of the current patch in a mesh pattern.

        The color is specified in the same way as in
        :meth:`Context.set_source_rgba`.

        Valid values for corner_num are from 0 to 3 and identify the corners
        as explained in :class:`MeshPattern`.
        """

    def get_path(self, patch_num: int) -> Path:
        """
        :param patch_num: the patch number to return data for
        :returns: the path defining the patch
        :raises Error:

        Gets path defining the patch ``patch_num`` for a mesh pattern.

        ``patch_num`` can range from 0 to n-1 where n is the number returned
        by :meth:`get_patch_count`.
        """

class PDFSurface(Surface):
    """
    The PDFSurface is used to render cairo graphics to Adobe PDF files and is a
    multi-page vector surface backend.

    .. versionadded:: 1.2
    """

    def __init__(self, fobj: Union[_PathLike, _FileLike], width_in_points: float, height_in_points: float) -> None:
        """
        :param fobj: a filename or writable file object. None may be used to
            specify no output. This will generate a *PDFSurface* that may be
            queried and used as a source, without generating a temporary file.
        :param width_in_points: width of the surface, in points (1 point ==
            1/72.0 inch)
        :param height_in_points: height of the surface, in points (1 point ==
            1/72.0 inch)
        :returns: a new *PDFSurface* of the specified size in points to be
            written to *fobj*.

        .. versionadded:: 1.2
        """

    def set_custom_metadata(self, name: str, value: Optional[str]) -> None:
        """
        :param name: The name of the custom metadata item to set.
        :param value: The value of the metadata.

        Set custom document metadata. *name* may be any string except for the
        following names reserved by PDF: "Title", "Author", "Subject",
        "Keywords", "Creator", "Producer", "CreationDate", "ModDate", "Trapped".

        If *value* is :obj:`None` or an empty string, the *name* metadata will
        not be set.

        For example::

            surface.set_custom_metadata("ISBN", "978-0123456789")

        .. versionadded:: 1.23.0 Only available with cairo 1.17.6+
        """

    def set_size(self, width_in_points: float, height_in_points: float) -> None:
        """
        :param width_in_points: new surface width, in points
            (1 point == 1/72.0 inch)
        :param height_in_points: new surface height, in points
            (1 point == 1/72.0 inch)

        Changes the size of a *PDFSurface* for the current (and subsequent) pages.

        This function should only be called before any drawing operations have
        been performed on the current page. The simplest way to do this is to
        call this function immediately after creating the surface or immediately
        after completing a page with either :meth:`Context.show_page` or
        :meth:`Context.copy_page`.

        .. versionadded:: 1.2
        """

    def restrict_to_version(self, version: PDFVersion) -> None:
        """
        :param version: PDF version

        Restricts the generated PDF file to version . See :meth:`get_versions`
        for a list of available version values that can be used here.

        This function should only be called before any drawing operations have
        been performed on the given surface. The simplest way to do this is to
        call this function immediately after creating the surface.

        .. versionadded:: 1.12.0
        """

    @staticmethod
    def get_versions() -> List[PDFVersion]:
        """
        :returns: supported version list

        Retrieve the list of supported versions. See
        :meth:`restrict_to_version`.

        .. versionadded:: 1.12.0
        """

    @staticmethod
    def version_to_string(version: PDFVersion) -> str:
        """
        :param version: PDF version
        :returns: the string associated to the given version
        :raises ValueError: if version isn't valid

        Get the string representation of the given version id. See
        :meth:`get_versions` for a way to get the list of valid version ids.

        .. versionadded:: 1.12.0
        """

    def add_outline(self, parent_id: int, utf8: str, link_attribs: str, flags: PDFOutlineFlags) -> int:
        """
        :param parent_id:
            the id of the parent item or :data:`PDF_OUTLINE_ROOT` if this is a top
            level item.
        :param utf8:
            the name of the outline
        :param link_attribs:
            the link attributes specifying where this outline links to
        :param flags:
            outline item flags
        :returns: the id for the added item.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def set_metadata(self, metadata: PDFMetadata, utf8: str) -> None:
        """
        :param metadata: The metadata item to set.
        :param utf8: metadata value

        Set document metadata. The :attr:`PDFMetadata.CREATE_DATE` and
        :attr:`PDFMetadata.MOD_DATE` values must be in ISO-8601 format:
        YYYY-MM-DDThh:mm:ss. An optional timezone of the form "[+/-]hh:mm" or
        "Z" for UTC time can be appended. All other metadata values can be any
        UTF-8 string.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def set_page_label(self, utf8: str) -> None:
        """
        :param utf8: metadata value

        Set page label for the current page.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def set_thumbnail_size(self, width: int, height: int) -> None:
        """
        :param width: Thumbnail width.
        :param height: Thumbnail height

        Set the thumbnail image size for the current and all subsequent pages.
        Setting a width or height of 0 disables thumbnails for the current and
        subsequent pages.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

class PSSurface(Surface):
    """
    The *PSSurface* is used to render cairo graphics to Adobe PostScript files and
    is a multi-page vector surface backend.
    """

    def __init__(self, fobj: Union[_FileLike, _PathLike], width_in_points: float, height_in_points: float) -> None:
        """
        :param fobj: a filename or writable file object. None may be used to specify no output. This will generate a *PSSurface* that may be queried and used as a source, without generating a temporary file.
        :param width_in_points: width of the surface, in points
            (1 point == 1/72.0 inch)
        :param height_in_points: height of the surface, in points
            (1 point == 1/72.0 inch)
        :returns: a new *PDFSurface* of the specified size in points to be written
            to *fobj*.
        :raises: :exc:`MemoryError` in case of no memory

        Note that the size of individual pages of the PostScript output can
        vary. See :meth:`.set_size`.
        """

    def dsc_begin_page_setup(self) -> None:
        """
        This method indicates that subsequent calls to
        :meth:`.dsc_comment` should direct comments to the PageSetup
        section of the PostScript output.

        This method call is only needed for the first page of a surface. It
        should be called after any call to :meth:`.dsc_begin_setup` and
        before any drawing is performed to the surface.

        See :meth:`.dsc_comment` for more details.

        .. versionadded:: 1.2
        """

    def dsc_begin_setup(self) -> None:
        """
        This function indicates that subsequent calls to :meth:`.dsc_comment`
        should direct comments to the Setup section of the PostScript output.

        This function should be called at most once per surface, and must be
        called before any call to :meth:`.dsc_begin_page_setup` and before any
        drawing is performed to the surface.

        See :meth:`.dsc_comment` for more details.

        .. versionadded:: 1.2
        """

    def dsc_comment(self, comment: str) -> None:
        """
        :param comment: a comment string to be emitted into the PostScript output

        Emit a comment into the PostScript output for the given surface.

        The comment is expected to conform to the PostScript Language
        Document Structuring Conventions (DSC). Please see that manual for
        details on the available comments and their meanings. In
        particular, the %%IncludeFeature comment allows a
        device-independent means of controlling printer device features. So
        the PostScript Printer Description Files Specification will also be
        a useful reference.

        The comment string must begin with a percent character (%) and the
        total length of the string (including any initial percent
        characters) must not exceed 255 characters. Violating either of
        these conditions will place *PSSurface* into an error state. But
        beyond these two conditions, this function will not enforce
        conformance of the comment with any particular specification.

        The comment string should not have a trailing newline.

        The DSC specifies different sections in which particular comments
        can appear. This function provides for comments to be emitted
        within three sections: the header, the Setup section, and the
        PageSetup section.  Comments appearing in the first two sections
        apply to the entire document while comments in the BeginPageSetup
        section apply only to a single page.

        For comments to appear in the header section, this function should
        be called after the surface is created, but before a call to
        :meth:`.dsc_begin_setup`.

        For comments to appear in the Setup section, this function should be
        called after a call to :meth:`.dsc_begin_setup` but before a call to
        :meth:`.dsc_begin_page_setup`.

        For comments to appear in the PageSetup section, this function should be
        called after a call to :meth:`.dsc_begin_page_setup`.

        Note that it is only necessary to call :meth:`.dsc_begin_page_setup` for
        the first page of any surface. After a call to :meth:`Context.show_page`
        or :meth:`Context.copy_page` comments are unambiguously directed to the
        PageSetup section of the current page. But it doesn't hurt to call this
        function at the beginning of every page as that consistency may make the
        calling code simpler.

        As a final note, cairo automatically generates several comments on
        its own. As such, applications must not manually generate any of
        the following comments:

        Header section: %!PS-Adobe-3.0, %Creator, %CreationDate, %Pages,
        %BoundingBox, %DocumentData, %LanguageLevel, %EndComments.

        Setup section: %BeginSetup, %EndSetup

        PageSetup section: %BeginPageSetup, %PageBoundingBox,
        %EndPageSetup.

        Other sections: %BeginProlog, %EndProlog, %Page, %Trailer, %EOF

        Here is an example sequence showing how this function might be used::

            surface = PSSurface (filename, width, height)
            ...
            surface.dsc_comment (surface, "%%Title: My excellent document")
            surface.dsc_comment (surface, "%%Copyright: Copyright (C) 2006 Cairo Lover")
            ...
            surface.dsc_begin_setup (surface)
            surface.dsc_comment (surface, "%%IncludeFeature: *MediaColor White")
            ...
            surface.dsc_begin_page_setup (surface)
            surface.dsc_comment (surface, "%%IncludeFeature: *PageSize A3")
            surface.dsc_comment (surface, "%%IncludeFeature: *InputSlot LargeCapacity")
            surface.dsc_comment (surface, "%%IncludeFeature: *MediaType Glossy")
            surface.dsc_comment (surface, "%%IncludeFeature: *MediaColor Blue")
            ... draw to first page here ..
            ctx.show_page (cr)
            ...
            surface.dsc_comment (surface, "%%IncludeFeature:  PageSize A5");
            ...

        .. versionadded:: 1.2
        """

    def get_eps(self) -> bool:
        """
        :returns: True iff the *PSSurface* will output Encapsulated PostScript.

        .. versionadded:: 1.6
        """

    @staticmethod
    def level_to_string(level: PSLevel) -> str:
        """
        :param level: a PS level
        :returns: the string associated to given level.

        Get the string representation of the given *level*.  See
        :meth:`get_levels` for a way to get the list of valid level
        ids.

        .. note:: Prior to 1.12 this was available under
            :meth:`ps_level_to_string`

        .. versionadded:: 1.12.0
        """

    ps_level_to_string = level_to_string
    """
    Alias for :meth:`level_to_string`

    .. versionadded:: 1.6
    """

    def restrict_to_level(self, level: PSLevel) -> None:
        """
        :param level: a PS level

        Restricts the generated PostSript file to *level*. See
        :meth:`get_levels` for a list of available level values that
        can be used here.

        This function should only be called before any drawing operations have
        been performed on the given surface. The simplest way to do this is to
        call this function immediately after creating the surface.

        .. versionadded:: 1.6
        """

    def set_eps(self, eps: bool) -> None:
        """
        :param eps: True to output EPS format PostScript

        If *eps* is True, the PostScript surface will output Encapsulated
        PostScript.

        This function should only be called before any drawing operations have
        been performed on the current page. The simplest way to do this is to
        call this function immediately after creating the surface. An
        Encapsulated PostScript file should never contain more than one page.

        .. versionadded:: 1.6
        """

    def set_size(self, width_in_points: float, height_in_points: float) -> None:
        """
        :param width_in_points: new surface width, in points (1 point == 1/72.0 inch)
        :param height_in_points: new surface height, in points (1 point == 1/72.0 inch)

        Changes the size of a PostScript surface for the current (and
        subsequent) pages.

        This function should only be called before any drawing operations
        have been performed on the current page. The simplest way to do
        this is to call this function immediately after creating the
        surface or immediately after completing a page with either
        :meth:`Context.show_page` or :meth:`Context.copy_page`.

        .. versionadded:: 1.2
        """

    @staticmethod
    def get_levels() -> List[PSLevel]:
        """
        :returns: supported level list

        Retrieve the list of supported levels. See
        :meth:`restrict_to_level`.

        .. versionadded:: 1.12.0
        """

class SVGSurface(Surface):
    """
    The *SVGSurface* is used to render cairo graphics to SVG files and is a
    multi-page vector surface backend
    """

    def __init__(self, fobj: "Union[_PathLike, _FileLike]", width_in_points: float, height_in_points: float) -> None:
        """
        :param fobj: a filename or writable file object. None may be used to specify no output. This will generate a *SVGSurface* that may be queried and used as a source, without generating a temporary file.
        :param width_in_points: width of the surface, in points (1 point == 1/72.0 inch)
        :param height_in_points: height of the surface, in points (1 point == 1/72.0 inch)
        """

    def restrict_to_version(self, version: SVGVersion) -> None:
        """
        :param version: SVG version

        Restricts the generated SVG file to version . See :meth:`get_versions`
        for a list of available version values that can be used here.

        This function should only be called before any drawing operations have
        been performed on the given surface. The simplest way to do this is to
        call this function immediately after creating the surface.

        .. versionadded:: 1.12.0
        """

    @staticmethod
    def get_versions() -> List[SVGVersion]:
        """
        :returns: supported version list

        Retrieve the list of supported versions. See
        :meth:`restrict_to_version`.

        .. versionadded:: 1.12.0
        """

    @staticmethod
    def version_to_string(version: SVGVersion) -> str:
        """
        :param version: SVG version
        :returns: the string associated to the given version
        :raises ValueError: if version isn't valid

        Get the string representation of the given version id. See
        :meth:`get_versions` for a way to get the list of valid version ids.

        .. versionadded:: 1.12.0
        """

    def get_document_unit(self) -> SVGUnit:
        """
        :returns: the SVG unit of the SVG surface.
        :rtype: SVGUnit

        Get the unit of the SVG surface.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

    def set_document_unit(self, unit: SVGUnit) -> None:
        """
        :param SVGUnit unit: SVG unit

        Use the specified unit for the width and height of the generated SVG
        file. See :class:`SVGUnit` for a list of available unit values that can
        be used here.

        This function can be called at any time before generating the SVG file.

        However to minimize the risk of ambiguities it's recommended to call it
        before any drawing operations have been performed on the given surface,
        to make it clearer what the unit used in the drawing operations is.

        The simplest way to do this is to call this function immediately after
        creating the SVG surface.

        Note if this function is never called, the default unit for SVG
        documents generated by cairo will be "pt". This is for historical
        reasons.

        .. versionadded:: 1.18.0 Only available with cairo 1.15.10+
        """

class RadialGradient(Gradient):

    def __init__(self, cx0: float, cy0: float, radius0: float, cx1: float, cy1: float, radius1: float) -> None:
        """
        :param cx0: x coordinate for the center of the start circle
        :param cy0: y coordinate for the center of the start circle
        :param radius0: radius of the start circle
        :param cx1: x coordinate for the center of the end circle
        :param cy1: y coordinate for the center of the end circle
        :param radius1: radius of the end circle

        Creates a new *RadialGradient* pattern between the two circles defined by
        (cx0, cy0, radius0) and (cx1, cy1, radius1).  Before using the gradient
        pattern, a number of color stops should be defined using
        :meth:`Gradient.add_color_stop_rgb` or :meth:`Gradient.add_color_stop_rgba`.

        Note: The coordinates here are in pattern space. For a new pattern, pattern
        space is identical to user space, but the relationship between the spaces
        can be changed with :meth:`Pattern.set_matrix`.
        """

    def get_radial_circles(self) -> Tuple[float, float, float, float, float, float]:
        """
        :returns: (x0, y0, r0, x1, y1, r1) - a tuple of float

            * x0: return value for the x coordinate of the center of the first circle
            * y0: return value for the y coordinate of the center of the first circle
            * r0: return value for the radius of the first circle
            * x1: return value for the x coordinate of the center of the second circle
            * y1: return value for the y coordinate of the center of the second circle
            * r1: return value for the radius of the second circle

        Gets the *Gradient* endpoint circles for a *RadialGradient*, each
        specified as a center coordinate and a radius.

        .. versionadded:: 1.4
        """

_AcquireCallback = Callable[[Surface, RectangleInt], Surface]
_ReleaseCallback = Callable[[Surface], None]

class RasterSourcePattern(Pattern):
    """
    The raster source provides the ability to supply arbitrary pixel data whilst
    rendering. The pixels are queried at the time of rasterisation by means of
    user callback functions, allowing for the ultimate flexibility. For example,
    in handling compressed image sources, you may keep a MRU cache of decompressed
    images and decompress sources on the fly and discard old ones to conserve
    memory.

    For the raster source to be effective, you must at least specify the acquire
    and release callbacks which are used to retrieve the pixel data for the region
    of interest and demark when it can be freed afterwards. Other callbacks are
    provided for when the pattern is copied temporarily during rasterisation, or
    more permanently as a snapshot in order to keep the pixel data available for
    printing.

    .. versionadded:: 1.15
    """

    def __init__(self, content: Content, width: int, height: int) -> None:
        """
        :param content:
            content type for the pixel data that will be returned. Knowing the
            content type ahead of time is used for analysing the operation and
            picking the appropriate rendering path.
        :param width:
            maximum size of the sample area
        :param height:
            maximum size of the sample area

        Creates a new user pattern for providing pixel data.

        Use the setter functions to associate callbacks with the returned pattern.

        .. versionadded:: 1.15
        """

    def set_acquire(self, acquire: Optional[_AcquireCallback], release: Optional[_ReleaseCallback]) -> None:
        """
        :param acquire:
            acquire callback or :obj:`None` to unset it
        :type acquire: :obj:`callable`
        :param release:
            (optional) release callback or :obj:`None`
        :type release: :obj:`callable`
        :raises Error:

        Specifies the callbacks used to generate the image surface for a
        rendering operation (acquire) and the function used to cleanup that
        surface afterwards.

        The acquire callback should create a surface (preferably an image
        surface created to match the target using
        :meth:`Surface.create_similar_image`) that defines at least the region
        of interest specified by extents. The surface is allowed to be the
        entire sample area, but if it does contain a subsection of the sample
        area, the surface extents should be provided by setting the device
        offset (along with its width and height) using
        :meth:`Surface.set_device_offset`.

        .. function:: acquire(target, extents)

            :param Surface target:
                the rendering target surface
            :param RectangleInt extents:
                rectangular region of interest in pixels in sample space
            :rtype: Surface

            This function is called when a pattern is being rendered from. It
            should create a surface that provides the pixel data for the
            region of interest as defined by extents, though the surface
            itself does not have to be limited to that area. For convenience
            the surface should probably be of image type, created with
            :meth:`Surface.create_similar_image` for the target (which enables
            the number of copies to be reduced during transfer to the device).
            Another option, might be to return a similar surface to the target
            for explicit handling by the application of a set of cached
            sources on the device. The region of sample data provided should
            be defined using :meth:`Surface.set_device_offset` to specify the
            top-left corner of the sample data (along with width and height of
            the surface).

        .. function:: release(surface)

            :param Surface surface:
                the surface created during acquire

            This function is called when the pixel data is no longer being
            accessed by the pattern for the rendering operation.

        .. versionadded:: 1.15
        """

    def get_acquire(self) -> Tuple[Optional[_AcquireCallback], Optional[_ReleaseCallback]]:
        """
        :returns: a (acquire, release) tuple of callables or None as set
            through :meth:`set_acquire`

        Queries the current acquire and release callbacks.

        .. versionadded:: 1.15
        """

class RecordingSurface(Surface):
    """
    A *RecordingSurface* is a surface that records all drawing operations at the
    highest level of the surface backend interface, (that is, the level of paint,
    mask, stroke, fill, and show_text_glyphs). The recording surface can then be
    "replayed" against any target surface by using it as a source surface.

    If you want to replay a surface so that the results in target will be
    identical to the results that would have been obtained if the original
    operations applied to the recording surface had instead been applied to the
    target surface, you can use code like this::

        cr = cairo.Context(target)
        cr.set_source_surface(recording_surface, 0.0, 0.0)
        cr.paint()

    A *RecordingSurface* is logically unbounded, i.e. it has no implicit
    constraint on the size of the drawing surface. However, in practice this is
    rarely useful as you wish to replay against a particular target surface with
    known bounds. For this case, it is more efficient to specify the target
    extents to the recording surface upon creation.

    The recording phase of the recording surface is careful to snapshot all
    necessary objects (paths, patterns, etc.), in order to achieve accurate
    replay.

    .. versionadded:: 1.11.0
    """

    def __init__(self, content: Content, rectangle: Rectangle) -> None:
        """
        :param content: the content for the new  surface
        :param rectangle: or None to record unbounded operations.

        Creates a *RecordingSurface* which can be used to record all drawing
        operations at the highest level (that is, the level of paint, mask, stroke,
        fill and show_text_glyphs). The *RecordingSurface* can then be "replayed"
        against any target surface by using it as a source to drawing operations.

        The recording phase of the *RecordingSurface* is careful to snapshot all
        necessary objects (paths, patterns, etc.), in order to achieve accurate
        replay.

        .. versionadded:: 1.11.0
        """

    def ink_extents(self) -> Tuple[float, float, float, float]:
        """
        * x0: the x-coordinate of the top-left of the ink bounding box
        * y0: the y-coordinate of the top-left of the ink bounding box
        * width: the width of the ink bounding box
        * height: the height of the ink bounding box

        Measures the extents of the operations stored within the
        *RecordingSurface*. This is useful to compute the required size of an
        *ImageSurface* (or equivalent) into which to replay the full sequence of
        drawing operations.

        .. versionadded:: 1.11.0
        """

    def get_extents(self) -> Optional[Rectangle]:
        """
        :returns: a rectangle or :obj:`None` if the surface is unbounded.

        Get the extents of the recording-surface.

        .. versionadded:: 1.12.0
        """

class Region:
    """
    Region is a simple graphical data type representing an area of
    integer-aligned rectangles. They are often used on raster surfaces to track
    areas of interest, such as change or clip areas.

    .. versionadded:: 1.11.0
    """

    def __init__(self, rectangle: Union[RectangleInt, List[RectangleInt]]) -> None:
        """
        :param rectangle_int: a rectangle or a list of rectangle

        Allocates a new empty region object or a region object with the
        containing rectangle(s).
        """

    def copy(self) -> "Region":
        """
        :returns: A newly allocated :class:`Region`.

        Allocates a new *Region* object copying the area from original.
        """

    def get_extents(self) -> RectangleInt:
        """
        :returns: The bounding rectangle of region
        """

    def num_rectangles(self) -> int:
        """
        :returns: The number of rectangles contained in region
        """

    def get_rectangle(self, nth: int) -> RectangleInt:
        """
        :param nth: a number indicating which rectangle should be returned
        :returns: The *nth* rectangle from the region
        """

    def is_empty(self) -> bool:
        """
        :returns: Whether region is empty
        """

    def contains_point(self, x: int, y: int) -> bool:
        """
        :param x: The x coordinate of a point
        :param y: The y coordinate of a point
        :returns: Whether (x , y) is contained in the region
        """

    def contains_rectangle(self, rectangle: RectangleInt) -> RegionOverlap:
        """
        :param rectangle: a region
        :returns: region overlap

        Checks whether rectangle is inside, outside or partially contained in
        region
        """

    def equal(self, region: "Region") -> bool:
        """
        :param region: a region
        :returns: Whether both regions contained the same coverage
        """

    def translate(self, dx: int, dy: int) -> None:
        """
        :param dx: Amount to translate in the x direction
        :param dy: Amount to translate in the y direction

        Translates region by (dx , dy ).
        """

    def intersect(self, other: "Union[Region, RectangleInt]") -> "Region":
        """
        :param other: region or rectangle
        :returns: The intersection of the region and the passed region or
            rectangle
        """

    def subtract(self, other: "Union[Region, RectangleInt]") -> "Region":
        """
        :param other: region or rectangle
        :returns: The result of the subtraction of the region and the passed
            region or rectangle
        """

    def union(self, other: "Union[Region, RectangleInt]") -> "Region":
        """
        :param other: region or rectangle
        :returns: The union of the region and the passed region or rectangle
        """

    def xor(self, other: "Union[Region, RectangleInt]") -> "Region":
        """
        :param other: region or rectangle
        :returns: The exclusive difference of the region and the passed region
            or rectangle
        """

class ScriptDevice(Device):
    """
    .. versionadded:: 1.14
    """

    def __init__(self, fobj: Union[_FileLike, _PathLike]) -> None:
        """
        :param fobj: a filename or writable file object.

        Creates a output device for emitting the script, used when creating the
        individual surfaces.
        """

    def set_mode(self, mode: ScriptMode) -> None:
        """
        :param mode: the new mode

        Change the output mode of the script
        """

    def get_mode(self) -> ScriptMode:
        """
        :returns: the current output mode of the script

        Queries the script for its current output mode.
        """

    def write_comment(self, comment: str) -> None:
        """
        :param comment: the string to emit

        Emit a string verbatim into the script.
        """

    def from_recording_surface(self, recording_surface: RecordingSurface) -> None:
        """
        :param recording_surface:
            the recording surface to replay
        :raises cairo.Error:

        Converts the record operations in recording_surface into a script.
        """

class ScriptSurface(Surface):
    """
    The script surface provides the ability to render to a native script that
    matches the cairo drawing model. The scripts can be replayed using tools
    under the util/cairo-script directory, or with cairo-perf-trace.

    .. versionadded:: 1.14
    """

    def __init__(self, script: ScriptDevice, content: Content, width: float, height: float) -> None:
        """
        :param script: the script (output device)
        :param content: the content of the surface
        :param width: width in pixels
        :param height: height in pixels
        :raises cairo.Error:

        Create a new surface that will emit its rendering through ``script``.
        """

    @classmethod
    def create_for_target(cls, script: ScriptDevice, target: Surface) -> "ScriptSurface":
        """
        :param script: the script (output device)
        :param target: a target surface to wrap
        :raises cairo.Error:

        Create a proxy surface that will render to ``target`` and record the
        operations to ``device``.

        .. versionadded:: 1.14
        """

class Win32Surface(Surface):
    """
    The Microsoft Windows surface is used to render cairo graphics to Microsoft
    Windows windows, bitmaps, and printing device contexts.
    """

    def __init__(self, hdc: int) -> None:
        """
        :param hdc: the DC to create a surface for
        :type hdc: int

        Creates a cairo surface that targets the given DC. The DC will be
        queried for its initial clip extents, and this will be used as the size
        of the cairo surface. The resulting surface will always be of format
        cairo.FORMAT_RGB24, see :class:`cairo.Format`.
        """

class Win32PrintingSurface(Surface):
    """
    The Win32PrintingSurface is a multi-page vector surface type.
    """

    def __init__(self, hdc: int) -> None:
        """
        :param hdc: the DC to create a surface for
        :returns: the newly created surface

        Creates a cairo surface that targets the given DC. The DC will be queried
        for its initial clip extents, and this will be used as the size of the
        cairo surface. The DC should be a printing DC; antialiasing will be
        ignored, and GDI will be used as much as possible to draw to the surface.

        The returned surface will be wrapped using the paginated surface to provide
        correct complex rendering behaviour; :meth:`cairo.Surface.show_page` and
        associated methods must be used for correct output.
        """

class SolidPattern(Pattern):

    def __init__(self, red: float, green: float, blue: float, alpha: float=1.0) -> None:
        """
        :param red: red component of the color
        :param green: green component of the color
        :param blue: blue component of the color
        :param alpha: alpha component of the color

        Creates a new *SolidPattern* corresponding to a translucent color. The
        color components are floating point numbers in the range 0 to 1. If the
        values passed in are outside that range, they will be clamped.
        """

    def get_rgba(self) -> Tuple[float, float, float, float]:
        """
        :returns: (red, green, blue, alpha) a tuple of float

        Gets the solid color for a *SolidPattern*.

        .. versionadded:: 1.4
        """

class SurfaceObserverMode(_IntEnum):
    """
    Whether operations should be recorded.

    .. versionadded:: 1.14
    """

    NORMAL: "SurfaceObserverMode" = ...
    """no recording is done"""

    RECORD_OPERATIONS: "SurfaceObserverMode" = ...
    """operations are recorded"""

class TeeSurface(Surface):
    """
    This surface supports redirecting all its input to multiple surfaces.

    .. versionadded:: 1.14
    """

    def __init__(self, master: Surface) -> None: ...

    def add(self, target: Surface) -> None:
        """
        :param target:
        :raises cairo.Error:

        Add the surface

        .. versionadded:: 1.14
        """

    def remove(self, target: Surface) -> None:
        """
        :param target:
        :raises cairo.Error:

        Remove the surface

        .. versionadded:: 1.14
        """

    def index(self, index: int) -> Surface:
        """
        :param index:
        :raises cairo.Error:

        Returns the surface at index ``index``. The master surface is
        at index 0.

        .. versionadded:: 1.14
        """

class ToyFontFace(FontFace):
    """
    The *cairo.ToyFontFace* class can be used instead of :meth:`Context.select_font_face` to create a toy font independently of a context.

    .. versionadded:: 1.8.4
    """

    def __init__(self, family: str, slant: FontSlant=..., weight: FontWeight=...) -> None:
        """
        :param family: a font family name
        :param slant: the font slant of the font,
            defaults to :attr:`cairo.FontSlant.NORMAL`.
        :param weight: the font weight of the font,
            defaults to :attr:`cairo.FontWeight.NORMAL`.

        Creates a *ToyFontFace* from a triplet of family, slant, and weight. These
        font faces are used in implementation of the the "toy" font API.

        If family is the zero-length string "", the platform-specific default
        family is assumed. The default family then can be queried using
        :meth:`.get_family`.

        The :meth:`Context.select_font_face` method uses this to create font
        faces. See that function for limitations of toy font faces.
        """

    def get_family(self) -> str:
        """
            :returns: the family name of a toy font

            .. versionadded:: 1.8.4
        """

    def get_slant(self) -> FontSlant:
        """
            :returns: the font slant value

            .. versionadded:: 1.8.4
        """

    def get_weight(self) -> FontWeight:
        """
            :returns: the font weight value

            .. versionadded:: 1.8.4
        """

class XCBSurface(Surface):
    """
    The XCB surface is used to render cairo graphics to X Window System windows
    and pixmaps using the XCB library.

    Note that the XCB surface automatically takes advantage of the X render
    extension if it is available.
    """

    def __init__(self, connection: Any, drawable: Any, visualtype: Any, width: int, height: int) -> None:
        """
        :param connection: an XCB connection
        :param drawable: a X drawable
        :param visualtype: a X visualtype
        :param width: The surface width
        :param height: The surface height

        Creates a cairo surface that targets the given drawable (pixmap or window).

        .. note:: This type isn't implemented. Please file a bug if you need it.
        """

    def set_size(self, width: int, height: int) -> None:
        """
        :param width: The width of the surface
        :param height: The height of the surface

        Informs cairo of the new size of the X Drawable underlying the surface.
        For a surface created for a Window (rather than a Pixmap), this function
        must be called each time the size of the window changes. (For a
        subwindow, you are normally resizing the window yourself, but for a
        toplevel window, it is necessary to listen for ConfigureNotify events.)

        A Pixmap can never change size, so it is never necessary to call this
        function on a surface created for a Pixmap.
        """

class XlibSurface(Surface):
    """
    The XLib surface is used to render cairo graphics to X Window System windows
    and pixmaps using the XLib library.

    Note that the XLib surface automatically takes advantage of X render
    extension if it is available.

    .. note:: *XlibSurface* cannot be instantiated directly because Python
      interaction with Xlib would require open source Python bindings to Xlib
      which provided a C API.
      However, an *XlibSurface* instance can be returned from a function call
      when using pygtk http://www.pygtk.org/.
    """

    def get_depth(self) -> int:
        """
        :returns: the number of bits used to represent each pixel value.

        .. versionadded:: 1.2
        """

    def get_height(self) -> int:
        """
        :returns: the height of the X Drawable underlying the surface in pixels.

        .. versionadded:: 1.2
        """

    def get_width(self) -> int:
        """
        :returns: the width of the X Drawable underlying the surface in pixels.

        .. versionadded:: 1.2
        """

def get_include() -> str:
    """
    :returns: a path to the directory containing the C header files

    Gives the include path which should be passed to the compiler.

    .. versionadded:: 1.16.0
    """

MIME_TYPE_JP2: str = ...
"""
The Joint Photographic Experts Group (JPEG) 2000 image coding standard
(ISO/IEC 15444-1).

.. versionadded:: 1.12.0
"""

MIME_TYPE_JPEG: str = ...
"""
The Joint Photographic Experts Group (JPEG) image coding standard (ISO/IEC
10918-1).

.. versionadded:: 1.12.0
"""

MIME_TYPE_PNG: str = ...
"""
The Portable Network Graphics image file format (ISO/IEC 15948).

.. versionadded:: 1.12.0
"""

MIME_TYPE_URI: str = ...
"""
URI for an image file (unofficial MIME type).

.. versionadded:: 1.12.0
"""

MIME_TYPE_UNIQUE_ID: str = ...
"""
Unique identifier for a surface (cairo specific MIME type). All surfaces
with the same unique identifier will only be embedded once.

.. versionadded:: 1.12.0
"""

MIME_TYPE_CCITT_FAX: str = ...
"""
Group 3 or Group 4 CCITT facsimile encoding (International
Telecommunication Union, Recommendations T.4 and T.6.)

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

MIME_TYPE_CCITT_FAX_PARAMS: str = ...
"""
Decode parameters for Group 3 or Group 4 CCITT facsimile encoding. See
`CCITT Fax Images
<https://cairographics.org/manual/cairo-PDF-Surfaces.html#ccitt>`__.

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

MIME_TYPE_EPS: str = ...
"""
Encapsulated PostScript file. Encapsulated PostScript File Format
Specification

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

MIME_TYPE_EPS_PARAMS: str = ...
"""
Embedding parameters Encapsulated PostScript data. See Embedding EPS files.

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

MIME_TYPE_JBIG2: str = ...
"""
Joint Bi-level Image Experts Group image coding standard (ISO/IEC 11544).

.. versionadded:: 1.18.0
"""

MIME_TYPE_JBIG2_GLOBAL: str = ...
"""
Joint Bi-level Image Experts Group image coding standard (ISO/IEC 11544)
global segment.

.. versionadded:: 1.18.0
"""

MIME_TYPE_JBIG2_GLOBAL_ID: str = ...
"""
An unique identifier shared by a JBIG2 global segment and all JBIG2 images
that depend on the global segment.

.. versionadded:: 1.18.0
"""

TAG_DEST: str = ...
"""
Create a destination for a hyperlink. Destination tag attributes are
detailed at Destinations.

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

TAG_LINK: str = ...
"""
Create hyperlink. Link tag attributes are detailed at Links.

.. versionadded:: 1.18.0 Only available with cairo 1.15.10+
"""

TAG_CONTENT: str = ...
"""
Create a content tag.

.. versionadded:: 1.25.0 Only available with cairo 1.18.0+
"""

TAG_CONTENT_REF: str = ...
"""
Create a content reference tag.

.. versionadded:: 1.25.0 Only available with cairo 1.18.0+
"""

CAPI: Any = ...

ANTIALIAS_BEST = Antialias.BEST
ANTIALIAS_DEFAULT = Antialias.DEFAULT
ANTIALIAS_FAST = Antialias.FAST
ANTIALIAS_GOOD = Antialias.GOOD
ANTIALIAS_GRAY = Antialias.GRAY
ANTIALIAS_NONE = Antialias.NONE
ANTIALIAS_SUBPIXEL = Antialias.SUBPIXEL
CONTENT_ALPHA = Content.ALPHA
CONTENT_COLOR = Content.COLOR
CONTENT_COLOR_ALPHA = Content.COLOR_ALPHA
EXTEND_NONE = Extend.NONE
EXTEND_PAD = Extend.PAD
EXTEND_REFLECT = Extend.REFLECT
EXTEND_REPEAT = Extend.REPEAT
FILL_RULE_EVEN_ODD = FillRule.EVEN_ODD
FILL_RULE_WINDING = FillRule.WINDING
FILTER_BEST = Filter.BEST
FILTER_BILINEAR = Filter.BILINEAR
FILTER_FAST = Filter.FAST
FILTER_GAUSSIAN = Filter.GAUSSIAN
FILTER_GOOD = Filter.GOOD
FILTER_NEAREST = Filter.NEAREST
FONT_SLANT_ITALIC = FontSlant.ITALIC
FONT_SLANT_NORMAL = FontSlant.NORMAL
FONT_SLANT_OBLIQUE = FontSlant.OBLIQUE
FONT_WEIGHT_BOLD = FontWeight.BOLD
FONT_WEIGHT_NORMAL = FontWeight.NORMAL
FORMAT_A1 = Format.A1
FORMAT_A8 = Format.A8
FORMAT_ARGB32 = Format.ARGB32
FORMAT_INVALID = Format.INVALID
FORMAT_RGB16_565 = Format.RGB16_565
FORMAT_RGB24 = Format.RGB24
FORMAT_RGB30 = Format.RGB30
FORMAT_RGB96F = Format.RGB96F
FORMAT_RGBA128F = Format.RGBA128F
HINT_METRICS_DEFAULT = HintMetrics.DEFAULT
HINT_METRICS_OFF = HintMetrics.OFF
HINT_METRICS_ON = HintMetrics.ON
HINT_STYLE_DEFAULT = HintStyle.DEFAULT
HINT_STYLE_FULL = HintStyle.FULL
HINT_STYLE_MEDIUM = HintStyle.MEDIUM
HINT_STYLE_NONE = HintStyle.NONE
HINT_STYLE_SLIGHT = HintStyle.SLIGHT
LINE_CAP_BUTT = LineCap.BUTT
LINE_CAP_ROUND = LineCap.ROUND
LINE_CAP_SQUARE = LineCap.SQUARE
LINE_JOIN_BEVEL = LineJoin.BEVEL
LINE_JOIN_MITER = LineJoin.MITER
LINE_JOIN_ROUND = LineJoin.ROUND
OPERATOR_ADD = Operator.ADD
OPERATOR_ATOP = Operator.ATOP
OPERATOR_CLEAR = Operator.CLEAR
OPERATOR_COLOR_BURN = Operator.COLOR_BURN
OPERATOR_COLOR_DODGE = Operator.COLOR_DODGE
OPERATOR_DARKEN = Operator.DARKEN
OPERATOR_DEST = Operator.DEST
OPERATOR_DEST_ATOP = Operator.DEST_ATOP
OPERATOR_DEST_IN = Operator.DEST_IN
OPERATOR_DEST_OUT = Operator.DEST_OUT
OPERATOR_DEST_OVER = Operator.DEST_OVER
OPERATOR_DIFFERENCE = Operator.DIFFERENCE
OPERATOR_EXCLUSION = Operator.EXCLUSION
OPERATOR_HARD_LIGHT = Operator.HARD_LIGHT
OPERATOR_HSL_COLOR = Operator.HSL_COLOR
OPERATOR_HSL_HUE = Operator.HSL_HUE
OPERATOR_HSL_LUMINOSITY = Operator.HSL_LUMINOSITY
OPERATOR_HSL_SATURATION = Operator.HSL_SATURATION
OPERATOR_IN = Operator.IN
OPERATOR_LIGHTEN = Operator.LIGHTEN
OPERATOR_MULTIPLY = Operator.MULTIPLY
OPERATOR_OUT = Operator.OUT
OPERATOR_OVER = Operator.OVER
OPERATOR_OVERLAY = Operator.OVERLAY
OPERATOR_SATURATE = Operator.SATURATE
OPERATOR_SCREEN = Operator.SCREEN
OPERATOR_SOFT_LIGHT = Operator.SOFT_LIGHT
OPERATOR_SOURCE = Operator.SOURCE
OPERATOR_XOR = Operator.XOR
PATH_CLOSE_PATH = PathDataType.CLOSE_PATH
PATH_CURVE_TO = PathDataType.CURVE_TO
PATH_LINE_TO = PathDataType.LINE_TO
PATH_MOVE_TO = PathDataType.MOVE_TO
PDF_VERSION_1_4 = PDFVersion.VERSION_1_4
PDF_VERSION_1_5 = PDFVersion.VERSION_1_5
PDF_VERSION_1_6 = PDFVersion.VERSION_1_6
PDF_VERSION_1_7 = PDFVersion.VERSION_1_7
PS_LEVEL_2 = PSLevel.LEVEL_2
PS_LEVEL_3 = PSLevel.LEVEL_3
REGION_OVERLAP_IN = RegionOverlap.IN
REGION_OVERLAP_OUT = RegionOverlap.OUT
REGION_OVERLAP_PART = RegionOverlap.PART
SCRIPT_MODE_ASCII = ScriptMode.ASCII
SCRIPT_MODE_BINARY = ScriptMode.BINARY
STATUS_CLIP_NOT_REPRESENTABLE = Status.CLIP_NOT_REPRESENTABLE
STATUS_DEVICE_ERROR = Status.DEVICE_ERROR
STATUS_DEVICE_FINISHED = Status.DEVICE_FINISHED
STATUS_DEVICE_TYPE_MISMATCH = Status.DEVICE_TYPE_MISMATCH
STATUS_FILE_NOT_FOUND = Status.FILE_NOT_FOUND
STATUS_FONT_TYPE_MISMATCH = Status.FONT_TYPE_MISMATCH
STATUS_INVALID_CLUSTERS = Status.INVALID_CLUSTERS
STATUS_INVALID_CONTENT = Status.INVALID_CONTENT
STATUS_INVALID_DASH = Status.INVALID_DASH
STATUS_INVALID_DSC_COMMENT = Status.INVALID_DSC_COMMENT
STATUS_INVALID_FORMAT = Status.INVALID_FORMAT
STATUS_INVALID_INDEX = Status.INVALID_INDEX
STATUS_INVALID_MATRIX = Status.INVALID_MATRIX
STATUS_INVALID_MESH_CONSTRUCTION = Status.INVALID_MESH_CONSTRUCTION
STATUS_INVALID_PATH_DATA = Status.INVALID_PATH_DATA
STATUS_INVALID_POP_GROUP = Status.INVALID_POP_GROUP
STATUS_INVALID_RESTORE = Status.INVALID_RESTORE
STATUS_INVALID_SIZE = Status.INVALID_SIZE
STATUS_INVALID_SLANT = Status.INVALID_SLANT
STATUS_INVALID_STATUS = Status.INVALID_STATUS
STATUS_INVALID_STRIDE = Status.INVALID_STRIDE
STATUS_INVALID_STRING = Status.INVALID_STRING
STATUS_INVALID_VISUAL = Status.INVALID_VISUAL
STATUS_INVALID_WEIGHT = Status.INVALID_WEIGHT
STATUS_JBIG2_GLOBAL_MISSING = Status.JBIG2_GLOBAL_MISSING
STATUS_LAST_STATUS = Status.LAST_STATUS
STATUS_NEGATIVE_COUNT = Status.NEGATIVE_COUNT
STATUS_NO_CURRENT_POINT = Status.NO_CURRENT_POINT
STATUS_NO_MEMORY = Status.NO_MEMORY
STATUS_NULL_POINTER = Status.NULL_POINTER
STATUS_PATTERN_TYPE_MISMATCH = Status.PATTERN_TYPE_MISMATCH
STATUS_READ_ERROR = Status.READ_ERROR
STATUS_SUCCESS = Status.SUCCESS
STATUS_SURFACE_FINISHED = Status.SURFACE_FINISHED
STATUS_SURFACE_TYPE_MISMATCH = Status.SURFACE_TYPE_MISMATCH
STATUS_TEMP_FILE_ERROR = Status.TEMP_FILE_ERROR
STATUS_USER_FONT_ERROR = Status.USER_FONT_ERROR
STATUS_USER_FONT_IMMUTABLE = Status.USER_FONT_IMMUTABLE
STATUS_USER_FONT_NOT_IMPLEMENTED = Status.USER_FONT_NOT_IMPLEMENTED
STATUS_WRITE_ERROR = Status.WRITE_ERROR
SUBPIXEL_ORDER_BGR = SubpixelOrder.BGR
SUBPIXEL_ORDER_DEFAULT = SubpixelOrder.DEFAULT
SUBPIXEL_ORDER_RGB = SubpixelOrder.RGB
SUBPIXEL_ORDER_VBGR = SubpixelOrder. VBGR
SUBPIXEL_ORDER_VRGB = SubpixelOrder.VRGB
SURFACE_OBSERVER_NORMAL = SurfaceObserverMode.NORMAL
SURFACE_OBSERVER_RECORD_OPERATIONS = SurfaceObserverMode.RECORD_OPERATIONS
SVG_VERSION_1_1 = SVGVersion.VERSION_1_1
SVG_VERSION_1_2 = SVGVersion.VERSION_1_2
TEXT_CLUSTER_FLAG_BACKWARD = TextClusterFlags.BACKWARD
PDF_METADATA_TITLE = PDFMetadata.TITLE
PDF_METADATA_AUTHOR = PDFMetadata.AUTHOR
PDF_METADATA_SUBJECT = PDFMetadata.SUBJECT
PDF_METADATA_KEYWORDS = PDFMetadata.KEYWORDS
PDF_METADATA_CREATOR = PDFMetadata.CREATOR
PDF_METADATA_CREATE_DATE = PDFMetadata.CREATE_DATE
PDF_METADATA_MOD_DATE = PDFMetadata.MOD_DATE
SVG_UNIT_USER = SVGUnit.USER
SVG_UNIT_EM = SVGUnit.EM
SVG_UNIT_EX = SVGUnit.EX
SVG_UNIT_PX = SVGUnit.PX
SVG_UNIT_IN = SVGUnit.IN
SVG_UNIT_CM = SVGUnit.CM
SVG_UNIT_MM = SVGUnit.MM
SVG_UNIT_PT = SVGUnit.PT
SVG_UNIT_PC = SVGUnit.PC
SVG_UNIT_PERCENT = SVGUnit.PERCENT
STATUS_TAG_ERROR = Status.TAG_ERROR
STATUS_FREETYPE_ERROR = Status.FREETYPE_ERROR
STATUS_WIN32_GDI_ERROR = Status.WIN32_GDI_ERROR
STATUS_PNG_ERROR = Status.PNG_ERROR
STATUS_DWRITE_ERROR = Status.DWRITE_ERROR
STATUS_SVG_FONT_ERROR = Status.SVG_FONT_ERROR
PDF_OUTLINE_FLAG_OPEN = PDFOutlineFlags.OPEN
PDF_OUTLINE_FLAG_BOLD = PDFOutlineFlags.BOLD
PDF_OUTLINE_FLAG_ITALIC = PDFOutlineFlags.ITALIC
COLOR_MODE_DEFAULT = ColorMode.DEFAULT
COLOR_MODE_NO_COLOR = ColorMode.NO_COLOR
COLOR_MODE_COLOR = ColorMode.COLOR
DITHER_NONE = Dither.NONE
DITHER_DEFAULT = Dither.DEFAULT
DITHER_FAST = Dither.FAST
DITHER_GOOD = Dither.GOOD
DITHER_BEST = Dither.BEST
