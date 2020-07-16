class Crew():
    def __init__(self):
        self.mission = 'Area 3'


class Astronaut(Crew):
    def __init__(self, fullname):
        super().__init__()
        self.firstname, self.lastname = fullname.split()

    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.mission})'


mark = Astronaut('Mark Watney')
melissa = Astronaut('Melissa Lewis')
alex = Astronaut('Alex Vogel')

result = f"""
Astronaut crew:
- {mark}
- {melissa}
- {alex}
"""

print(result)
