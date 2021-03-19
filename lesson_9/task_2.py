class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, thickness=1):
        mass_per_sqm = 25
        result_mass = mass_per_sqm * thickness * self._width * self._length
        return result_mass


road_1 = Road(20, 5)
print(road_1.mass(5))

road_2 = Road(3, 1)
print(road_2.mass())