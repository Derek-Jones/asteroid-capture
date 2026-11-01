Create a browser based app to help the user locate asteroids orbiting the sun that are possible candidates for moving into a stable earth orbit (any orbit within 100k miles is acceptable).

The propulsion is provided by a block 4 Starship from SpaceX, with the best figure listed on Wikipedia.  Assume that a fully fuelled StarShip can be connected to the asteroid selected.  There is no need to consider any of the issues around docking and firmly connecting the Starship to the asteroid.  The asteroid is assumed to be a rigid body.

Calculate the asteroid mass from its estimated diameter and the average density of known asteroids.  List error bounds on the calculated mass.

The app estimates whether a Startship provides enough propulsion to move the selected asteroid to an earth orbit.  Multiple burns are possible, with burns selected to optimise time to earth orbit.  Suggest the possible sequence of burns.

Estimate flight time from first Starship burn to approaching within 100k miles of the earth.

Asteroids that are rotating faster than once per day are not considered.  If the rotation rate is unknown, ignored the asteroid.

The main page shows the inner planets of the solar system and a selection of
asteroids that are dues to pass close to the earth.
an example page is available here
https://www.spacereference.org/solar-system#ob=2001-einstein-1973-eb,7672-hawking-1995-uo2,2709-sagan-1982-fh

The user clicks on an asteroid and the app shows the trajectory of the asteroid when the Starship engines are fired to put it on a trajectory towards Earth orbit.  Show the possible impact area on the earth, if the rocket insertion burn fails.

Orbital information on known asteroids is available at
https://asteroid.lowell.edu/astorb/

spacewkit.js is a javascript library for creating interactive 3D visualizations
https://asteroid.lowell.edu/astorb/

Move the Starship configuration options to the bottom of the page.

Add a speed control to the INNER SOLAR SYSTEM player and allow the start/end dates to be set by the user.

Make the Not feasible with one Starship window collapsable.

Make the Earth approach window zoomable and playable, like INNER SOLAR SYSTEM

Highlight the path of the selected astroid in red and the orbit of the earth in blue.

Add an option to order asteroids by date and then by size low to high or high to low.

A burn is calculated, even when the rotation rate is unknown.

Extend the possible range in the Earth approach window to 2 million miles.

If the asteroid is rotating, the Starship engines can be gimbaled to eliminate rotation.  Add support for asteroids smaller than 200m that are rotating slower than once per hour.  Include the fuel needed to eliminate rotation into the viability calculation.

When the rotation rate is unknown, assume that it is slightly slower than once per hour.


The track of the selected asteroid and the planets is correct.  The tack of the other asteroids needs to be fainter, so they do not dominate the image.

Make the path of the Earth appear in bright green and the path of the selected asteroid in bright red.

