"""Code for relational geometry."""

class InvalidPointError(ValueError):
    """Raised to signify a Point we can't deal with."""

class Already3DPointError(ValueError):
    """Raised when we try to add the third dimension to a 3D point."""

def north(base_tuple, delta):
    """Determine a point *north* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0]+delta, base_tuple[1])
    elif len(base_tuple) == 3:
        return (base_tuple[0]+delta, base_tuple[1], base_tuple[2])
    else:
        raise InvalidPointError(base_tuple)

def south(base_tuple, delta):
    """Determine a point *south* of the base location."""
    if len(base_tuple) == 2:
        return (base_tuple[0]-delta, base_tuple[1])
    elif len(base_tuple) == 3:
        return (base_tuple[0]-delta, base_tuple[1], base_tuple[2])
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
