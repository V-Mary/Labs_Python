from models import *


def main():

    Mary = Position("Mary", 1, 250, 6, 1, 18)
    Ann = Position("Ann", 1, 500, 8, 5, 20)
    Bob = Position("Bob", 1, 100, 7, 3, 36)
    Andry = Maker("Andry", 3, 459, 4, 4, 40, 10, 4)
    Mark = Maker("Mark", 2, 550, 6, 5, 22, 8, 5)
    Lala = Technical("Lala", 6, 120,4, 1, 31, 7, 5, "Apple")
    Katy = Performer("Katy", 5, 630, 5, 5, 38, 10, True)
    Ivan = MainRole("Ivan", 5, 450, 8, 5, 19, 20, True, False, 3)

    List_of_employees = StudioManager([Mary, Ann, Bob, Andry, Mark, Lala, Katy, Ivan])

    print("\nEmployees needed to film historical films:")
    List_of_employees.search_by_film_type(FilmType.Historical)
    print("\nSort employees by salery:")
    List_of_employees.sort_by_salery(Sort.DESC)
    print("\nSort employees by working hours:")
    List_of_employees.sort_by_hours(Sort.ASC)

if __name__ == '__main__':
    main()
