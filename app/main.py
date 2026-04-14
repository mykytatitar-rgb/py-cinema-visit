from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    custs = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        custs.append(cust)
        CinemaBar.sell_product(cust.food, cust)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    CinemaHall.movie_session(hall, movie, custs, clean)
