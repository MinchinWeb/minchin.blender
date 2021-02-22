"""Measurements; i.e. lengths.

The inch is used internally as the base unit."""

inch = 1  # "in" is a keyword in Python, and so not used here
# 1 inch = 2.54 cm exactly
foot = ft = 12 * inch
yard = yd = 3 * ft
mile = mi = 5280 * ft

hand = 4 * inch
rod = rd = 16.5 * ft
chain = ch = 4 * rod
furlong = fur = 10 * ch
league = 3 * mi  # traditionally, how long someone could walk in a hour

meter = metre = m = 39.370 * inch
kilometer = kilometre = km = 10**3 * m
centimeter = centimetre = cm = 1/10**2 * m
millimeter = millimetre = mm = 1/10**3 * m
micrometer = micrometre = um = 1/10**6 * m
nanometer = nanometre = nm = 1/10**9 * m

nautical_mile = nmi = 1852 * m

# Points are used in typography
point = pt = 1/12 * inch
