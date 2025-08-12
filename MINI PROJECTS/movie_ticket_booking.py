class movie:
    def __init__(self, title, total_seats, booked_seats=0):
        self.title = title
        self.total_seats = total_seats
        self.booked_seats = booked_seats

    def availible_seats(self):
        return self.total_seats - self.booked_seats

    def book_ticket(self, num):
        if self.availible_seats() >= num:
            print(f"{num} seats got booked.")
            self.total_seats -= num
            print(f"Remaining Seats : {self.availible_seats()}")
        else:
            print(
                f"Can't book {num} seats! Only {self.availible_seats()} seats are availible."
            )


m1 = movie("Shawshank Redemption", 24)
m1.book_ticket(4)
m1.book_ticket(15)
m1.book_ticket(10)
