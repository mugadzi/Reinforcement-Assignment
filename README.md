# Reinforcement-Assignment
# AFourRooms.py Documentation
A.1Initialization:
FourRooms.__init__(scenario : str, stochastic : bool = False) -> FourRooms
Creates and initializes a FourRooms object. You just invoke it by creating the object
FourRooms(). The scenario property must be one of the following values: ’simple’, ’multi’
or ’rgb’. You can set stochastic=True if you want your agent to have to traverse in a
non-deterministic environment.
A.2
GetPosition:
FourRooms.getPosition() -> (int, int)
This function will return the location of the agent in the grid-world. The location is
returned as a tuple (x, y).
A.3
GetPackagesRemaining:
FourRooms.getPackagesRemaining() -> int
This function will return the number of packages left to collect. The value returned is an
int.
