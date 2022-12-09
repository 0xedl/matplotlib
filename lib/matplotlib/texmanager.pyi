from .backend_bases import RendererBase

from matplotlib import cbook as cbook, dviread as dviread
from matplotlib._typing import Color

import numpy as np

class TexManager:
    texcache: str
    @classmethod
    def get_basefile(cls, tex: str, fontsize: float, dpi: float | None = ...) -> str: ...
    @classmethod
    def get_font_preamble(cls) -> str: ...
    @classmethod
    def get_custom_preamble(cls) -> str: ...
    @classmethod
    def make_tex(cls, tex: str, fontsize: float) -> str: ...
    @classmethod
    def make_dvi(cls, tex: str, fontsize: float) -> str: ...
    @classmethod
    def make_png(cls, tex: str, fontsize: float, dpi: float) -> str: ...
    @classmethod
    def get_grey(cls, tex: str, fontsize: float | None = ..., dpi: float | None = ...) -> np.ndarray: ...
    @classmethod
    def get_rgba(cls, tex: str, fontsize: float | None = ..., dpi: float | None = ..., rgb: Color=...) -> np.ndarray: ...
    @classmethod
    def get_text_width_height_descent(cls, tex: str, fontsize, renderer: RendererBase | None = ...) -> tuple[int, int, int]: ...
