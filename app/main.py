from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
) -> None:
    custs = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        custs.append(cust)
        CinemaBar.sell_product(cust.food, cust)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, custs, clean)
