import pickle


class Cars:
    def __init__(self):
        self.engine = 0
        self.price = 0
        self.name = ''
        self.seats = 0


car_1 = Cars
file1 = open('cars.DAT', 'wb')
pickle.dump(car_1, file1)

file1.close()
file2 = open('cars.DAT', 'rb')
Car = []
Car.append(pickle.load(file2))
file2.close()
print(hash(Car[0]))