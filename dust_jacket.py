from dataclasses import dataclass

@dataclass(order=True)
class Point:
    """
    Pair of Cartesian coordinates. Abscissa is x/horizontal, Ordinate
    is y/vertical.
    """
    abscissa: float
    ordinate: float

    def __iter__(self):
        yield self.abscissa
        yield self.ordinate

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
