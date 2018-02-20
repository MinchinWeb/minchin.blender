"""Code for relational geometry."""

class InvalidPointError(ValueError):
    """Raised to signify a Point we can't deal with."""

class Already3DPointError(ValueError):
    """Raised when we try to add the third dimension to a 3D point."""

class Already2DPointError(ValueError):
    """Raised when we try to remove the third dimension to a 3D point."""


def north(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0]-delta, base_tuple[1])
    elif len(base_tuple) == 3:
        return (base_tuple[0]-delta, base_tuple[1], base_tuple[2])
    else:
        raise InvalidPointError(base_tuple)

def south(base_tuple, delta):
    """Determine a point *south* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0]+delta, base_tuple[1])
    elif len(base_tuple) == 3:
        return (base_tuple[0]+delta, base_tuple[1], base_tuple[2])
    else:
        raise InvalidPointError(base_tuple)

def east(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0], base_tuple[1]+delta)
    elif len(base_tuple) == 3:
        return (base_tuple[0], base_tuple[1]+delta, base_tuple[2])
    else:
        raise InvalidPointError(base_tuple)

def west(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0], base_tuple[1]-delta)
    elif len(base_tuple) == 3:
        return (base_tuple[0], base_tuple[1]-delta, base_tuple[2])
    else:
        raise InvalidPointError(base_tuple)

def up(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 3:
        return (base_tuple[0], base_tuple[1], base_tuple[2]+delta)
    else:
        raise InvalidPointError(base_tuple)

def down(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 3:
        return (base_tuple[0], base_tuple[1], base_tuple[2]-delta)
    else:
        raise InvalidPointError(base_tuple)


def add_z(base_tuple, z=0):
    """Add the third dimension to a 2D point."""
    if len(base_tuple) == 2:
        return (base_tuple[0], base_tuple[1], z)
    elif len(base_tuple) == 3:
        raise Already3DPointError(base_tuple)
    else:
        raise InvalidPointError(base_tuple)

def drop_z(base_tuple):
    """Drops the z dimension and returns a 2D point."""
    if len(base_tuple) == 2:
        raise Already2DPointError(base_tuple)
    elif len(base_tuple) == 3:
        return (base_tuple[0], base_tuple[1])
    else:
        raise InvalidPointError(base_tuple)


def poly_area2D(poly):
    """
    Area of a 2D polynomial.
    
    Assumes that it does not self-intersect.
    """
    # https://code.activestate.com/recipes/578275-2d-polygon-area/
    # https://github.com/ActiveState/code/blob/master/recipes/Python/578275_2D_polygon_area/recipe-578275.py
    total = 0.0
    N = len(poly)
    for i in range(N):
        v1 = poly[i]
        v2 = poly[(i+1) % N]
        total += v1[0]*v2[1] - v1[1]*v2[0]
    return abs(total/2)


def add_xy(xy1, xy2):
    if len(xy1) != 2:
        raise InvalidPointError(xy1)
    if len(xy2) != 2:
        raise InvalidPointError(xy2)
    
    return (xy1[0] + xy2[0], xy1[1] + xy2[1])
