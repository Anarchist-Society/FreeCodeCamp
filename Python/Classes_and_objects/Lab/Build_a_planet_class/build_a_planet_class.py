print('Build a Planet Class:\n')

class Planet:
    def __init__(self, name, planet_type, star):
        # if not isinstance(name, str):
        #     raise TypeError('name, planet type, and star must be strings')

        # if not isinstance(planet_type, str):
        #     raise TypeError('name, planet type, and star must be strings')

        # if not isinstance(star, str):
        #     raise TypeError('name, planet type, and star must be strings')

        if not isinstance(name, str) or isinstance(planet_type, str) or isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        # if name == '' or planet_type == '' or star == '':
        #     raise ValueError('name, planet_type, and star must be non-empty strings')

        if not name or not planet_type or not star:
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1: Planet = Planet(name='Tierra', planet_type='Terrestre', star='Sol')
planet_2: Planet = Planet(name='Marte', planet_type='Terrestre', star='Sol')
planet_3: Planet = Planet(name='Júpiter', planet_type='Gaseoso', star='Sol')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
