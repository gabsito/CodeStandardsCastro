class PopularDestinations:
    def __init__(self):
        self.popular_destination = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, destination):
        return self.popular_destination.get(destination, 0)

    def valid_destination(self, destination):
        return isinstance(destination, str)

class Passenger:
    def __init__(self, travelers):
        self.travelers = travelers
    
    def valid_number(self):
        return isinstance(self.travelers, int) and self.travelers > 0

    def travelers_discount(self):
        if 4 < self.travelers < 10:
            return 0.1
        elif self.travelers <= 10:
            return 0.2
        else:
            return 0.0

class DurationPolicies:
    def __init__(self, duration):
        self.duration = duration

    def validate_duration(self):
        return isinstance(self.duration, int) and self.duration > 0

    def duration_fee(self):
        return 200 if self.duration < 7 else 0

    def getTheBestPromoEver(self):
        return 200 if self.duration > 30 else 0

class Vacation:
    base_cost = 1000

    def __init__(self, destination, travelers, duration):
        self.popular_destinations = PopularDestinations()
        self.passenger = Passenger(travelers)
        self.duration_policies = DurationPolicies(duration)
        self.destination = destination

    def calc_price(self):
        if not self.popular_destinations.valid_destination(self.destination) or not self.utils.valid_number() or not self.duration_policies.validate_duration():
            return -1
        
        price = self.base_cost
        price += self.popular_destinations.get_extra_cost(self.destination)
        price += self.duration_policies.duration_fee()
        price -= self.duration_policies.getTheBestPromoEver()

        discount = self.passenger.travelers_discount()
        price = price - (price * discount)
        
        return max(int(price), 0)

def main():
    destination = "Paris"
    travelers = 5
    duration = 10

    vacation = Vacation(destination, travelers, duration)
    cost = vacation.calc_price()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

if __name__ == "__main__":
    main()
    