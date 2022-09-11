"""
Plots dust covers in scribus. Provides interface to allow custom dust covers
"""

from dataclasses import dataclass
import abc

def main():
    """
    1. setup document
    2. get param.csv and config filepaths
    3. match plotter class to config spec (hardcoded?)
    4. loop over params:
          4.1 setup new page
          4.2 with the params from row, run all the plotter methods using
              the plotter class
    """

@dataclass(order=True)
class Point:
    """
    Pair of Cartesian coordinates. Abscissa is x/horizontal, Ordinate
    is y/vertical.
    """
    abscissa: float
    ordinate: float
    _index: float = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return (self.ordinate, self.abscissa)[self._index]

@dataclass(init=False)
class Canvas:
    """
    Non-rotated rectangular drawing area, defined by origin < termination
    """
    origin: Point
    termination: Point

    def __init__(self, origin: Point, termination: Point) -> None:
        assert origin < termination
        self.origin = origin
        self.termination = termination

@dataclass(frozen=True)
class DustJacket:
    """
    Dust jacket object used for attaining measurements and book variables
    """
    book_height: float
    book_width: float
    book_thickness: float
    flap_width: float
    book_vars: dict

    def _component_measurement(self,
                               orig_abscissa: float,
                               component_width: float) -> Canvas:
        """
        Generate canvas for components based on leftmost and rightmost points
        """
        origin = Point(orig_abscissa, 0)
        termination = [x + y for x, y in
                       zip(origin, Point(component_width, self.book_height))]
        return Canvas(origin, Point(*termination))

    @property
    def left_fold(self) -> Canvas:
        """
        return the left fold coordinates
        """
        return self._component_measurement(0, self.book_width)

    @property
    def left_trim(self) -> Canvas:
        """
        return the left trim coordinates
        """
        return self._component_measurement(
            self.left_fold.termination.abscissa,
            self.flap_width)

    @property
    def spine(self) -> Canvas:
        """
        return the spine coordinates
        """
        return self._component_measurement(
            self.left_trim.termination.abscissa,
            self.book_thickness)

    @property
    def right_trim(self) -> Canvas:
        """
        return the right trim coordinates
        """
        return self._component_measurement(
            self.spine.termination.abscissa,
            self.book_width)

    @property
    def right_fold(self) -> Canvas:
        """
        return the right fold coordinates
        """
        return self._component_measurement(
            self.right_trim.termination.abscissa,
            self.flap_width)

class DustJacketComponentPlotterInterface(metaclass=abc.ABCMeta):
    """
    Interface for plotting dust jacket components
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'plot_left_fold') and
                callable(subclass.plot_left_fold) and
                hasattr(subclass, 'plot_left_trim') and
                callable(subclass.plot_left_trim) and
                hasattr(subclass, 'plot_spine') and
                callable(subclass.plot_spine) and
                hasattr(subclass, 'plot_right_trim') and
                callable(subclass.plot_right_trim) and
                hasattr(subclass, 'plot_right_fold') and
                callable(subclass.plot_right_fold) and
                hasattr(subclass, 'plot_outer') and
                callable(subclass.plot_outer) or
                NotImplemented)

    @abc.abstractmethod
    def plot_left_fold(self, canvas: Canvas) -> None:
        """Plot the left fold using the given canvas in Scribus"""
        raise NotImplementedError

    @abc.abstractmethod
    def plot_left_trim(self, canvas: Canvas) -> None:
        """Plot the left trim using the given canvas in Scribus"""
        raise NotImplementedError

    @abc.abstractmethod
    def plot_spine(self, canvas: Canvas) -> None:
        """Plot the spine using the given canvas in Scribus"""
        raise NotImplementedError

    @abc.abstractmethod
    def plot_right_trim(self, canvas: Canvas) -> None:
        """Plot the right trim using the given canvas in Scribus"""
        raise NotImplementedError

    @abc.abstractmethod
    def plot_right_fold(self, canvas: Canvas) -> None:
        """Plot the right fold using the given canvas in Scribus"""
        raise NotImplementedError

    @abc.abstractmethod
    def plot_outer(self, canvas: Canvas) -> None:
        """
        Plot the outer jacket of the dust cover using the given canvas in
        Scribus. Examples of use is for bands or other spanning objects
        """
        raise NotImplementedError

@dataclass
class SimpleDustJacketPlotter(DustJacketComponentPlotterInterface):
    """
    Plots dust jacket components in a simple style
    """
    dust_jacket: DustJacket
    config: dict

    def plot_left_fold(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_left_fold()"""
    def plot_left_trim(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_left_trim()"""
    def plot_spine(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_spine()"""
    def plot_right_trim(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_right_trim()"""
    def plot_right_fold(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_right_fold()"""
    def plot_outer(self, canvas: Canvas) -> None:
        """Overrides DustJacketPlotterInterface.plot_outer()"""
