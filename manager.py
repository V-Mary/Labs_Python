from models.enums.film_type import FilmType
from models.enums.sort import Sort
from operator import attrgetter


class StudioManager:
    def __init__(self, employees: []):
        self.employees = employees

    def search_by_film_type(self, film_type: FilmType):
        new_list = list()
        for item in self.employees:
            if item.film_type == film_type:
                new_list.append(item)
                print(item.name)
        return new_list

    def sort_by_salery(self, sort: Sort):
            if sort == Sort.ASC:
                s = sorted(self.employees, key=attrgetter('salery'))
                for x in range(len(s)):
                    print(s[x].name,"-", s[x].salery, "$")
            if sort == Sort.DESC:
                s = sorted(self.employees, key=attrgetter('salery'),  reverse=True)
                for x in range(len(s)):
                    print(s[x].name,"-", s[x].salery, "$")

    def sort_by_hours(self, sort: Sort):
        if sort == Sort.ASC:
            s = sorted(self.employees, key=attrgetter('working_hours'))
            for x in range(len(s)):
                print(s[x].name, "-", s[x].working_hours, "hours")
        if sort == Sort.DESC:
            s = sorted(self.employees, key=attrgetter('working_hours'), reverse=True)
            for x in range(len(s)):
                print(s[x].name, "-", s[x].working_hours, "hours")
