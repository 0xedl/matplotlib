import enum
from matplotlib import cbook
from matplotlib.axes import Axes
from matplotlib.backend_bases import ToolContainerBase, FigureCanvasBase
from matplotlib.backend_managers import ToolManager, ToolEvent
from matplotlib.figure import Figure
from matplotlib.scale import ScaleBase
from matplotlib._pylab_helpers import Gcf

from typing import Any, Type

class Cursors(enum.IntEnum):
    POINTER: int
    HAND: int
    SELECT_REGION: int
    MOVE: int
    WAIT: int
    RESIZE_HORIZONTAL: int
    RESIZE_VERTICAL: int
cursors = Cursors

class ToolBase:
    default_keymap: list[str] | None
    description: str | None
    image: str | None
    def __init__(self, toolmanager: ToolManager, name: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def toolmanger(self) -> ToolManager: ...
    @property
    def canvas(self) -> FigureCanvasBase | None: ...
    @property
    def figure(self) -> Figure | None: ...
    @figure.setter
    def figure(self, figure: Figure | None) -> None: ...
    def set_figure(self, figure: Figure | None) -> None: ...
    def trigger(self, sender: Any, event: ToolEvent, data: Any = ...) -> None: ...
    def destroy(self) -> None: ...

class ToolToggleBase(ToolBase):
    radio_group: str | None
    cursor: Cursors | None
    default_toggled: bool
    def __init__(self, toolmanager: ToolManager, name: str, *, toggled: bool = ...) -> None: ...
    def enable(self, event: ToolEvent | None = ...) -> None: ...
    def disable(self, event: ToolEvent | None = ...) -> None: ...
    @property
    def toggled(self) -> bool: ...
    def set_figure(self, figure: Figure | None) -> None: ...

class ToolSetCursor(ToolBase):
    ...

class ToolCursorPosition(ToolBase):
    def send_message(self, event: ToolEvent) -> None: ...

class RubberbandBase(ToolBase):
    def draw_rubberband(self, *data) -> None: ...
    def remove_rubberband(self) -> None: ...

class ToolQuit(ToolBase):
    ...

class ToolQuitAll(ToolBase):
    ...

class ToolGrid(ToolBase):
    ...

class ToolMinorGrid(ToolBase):
    ...

class ToolFullScreen(ToolBase):
    ...

class AxisScaleBase(ToolToggleBase):
    def enable(self, event: ToolEvent | None = ...) -> None: ...
    def disable(self, event: ToolEvent | None = ...) -> None: ...

class ToolYScale(AxisScaleBase):
    def set_scale(self, ax: Axes, scale: str | ScaleBase) -> None: ...

class ToolXScale(AxisScaleBase):
    def set_scale(self, ax, scale: str | ScaleBase) -> None: ...

class ToolViewsPositions(ToolBase):
    views: dict[Figure | Axes, cbook.Stack]
    positions: dict[Figure | Axes, cbook.Stack]
    home_views: dict[Figure, dict[Axes, tuple[float, float, float, float]]]
    def add_figure(self, figure: Figure) -> None: ...
    def clear(self, figure: Figure) -> None: ...
    def update_view(self) -> None: ...
    def push_current(self, figure: Figure | None = ...) -> None: ...
    def update_home_views(self, figure: Figure | None = ...) -> None: ...
    def home(self) -> None: ...
    def back(self) -> None: ...
    def forward(self) -> None: ...

class ViewsPositionsBase(ToolBase):
    ...

class ToolHome(ViewsPositionsBase):
    ...

class ToolBack(ViewsPositionsBase):
    ...

class ToolForward(ViewsPositionsBase):
    ...

class ConfigureSubplotsBase(ToolBase):
    ...

class SaveFigureBase(ToolBase):
    ...

class ZoomPanBase(ToolToggleBase):
    base_scale: float
    scrollthresh: float
    lastscroll: float
    def __init__(self, *args) -> None: ...
    def enable(self, event: ToolEvent | None = ...) -> None: ...
    def disable(self, event: ToolEvent | None = ...) -> None: ...
    def scroll_zoom(self, event: ToolEvent) -> None: ...

class ToolZoom(ZoomPanBase):
    ...

class ToolPan(ZoomPanBase):
    ...

class ToolHelpBase(ToolBase):
    @staticmethod
    def format_shortcut(key_sequence: str) -> str: ...

class ToolCopyToClipboardBase(ToolBase):
    ...

default_tools: dict[str, ToolBase]
default_toolbar_tools: list[list[str | list[str]]]

def add_tools_to_manager(toolmanager: ToolManager, tools: dict[str, Type[ToolBase]]=...) -> None: ...
def add_tools_to_container(container: ToolContainerBase, tools: list[Any]) -> None: ...
