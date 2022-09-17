from dataclasses import dataclass
from dust_jacket import Canvas
import dust_jacket

@dataclass
class SimpleDustJacketPlotter(DustJacketComponentPlotterInterface):
    """
    Plots dust jacket components in a simple style
    """
    dust_jacket: DustJacket

    def __enter__(self):
        newDocument(self.dust_jacket.right_fold.termination,
            (0,0,0,0), LANDSCAPE, 1, UNIT_MILLIMETERS, PAGE_1, 0, 1)
        setBleeds(15,15,15,15)
        saveDocAs(self.dust_jacket.name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def plot_left_fold(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the left fold of the dust cover using the given canvas in
        Scribus
        """
    def plot_left_trim(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the left trim of the dust cover using the given canvas in
        Scribus
        """
    def plot_spine(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the spine of the dust cover using the given canvas in
        Scribus
        """
    def plot_right_trim(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the right trim of the dust cover using the given canvas in
        Scribus
        """
    def plot_right_fold(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the right fold of the dust cover using the given canvas in
        Scribus
        """
    def plot_outer(self, canvas: dust_jacket.Canvas) -> None:
        """
        Plot the outer jacket of the dust cover using the given canvas in
        Scribus. Examples of use is for background as well as bands or
        other spanning objects
        """
