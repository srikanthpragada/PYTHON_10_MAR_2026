class Course:
    # Static attribute
    taxrate = 12

    @staticmethod
    def get_taxrate():
        return Course.taxrate

    @staticmethod
    def set_taxrate(taxrate):
        Course.taxrate = taxrate

    def __init__(self, title, duration=20, fee=0):
        # Object attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def show(self):
        print(f'Title    : {self.title}')
        print(f'Duration : {self.duration}')
        print(f'Fee      : {self.fee}')

    def get_net_fee(self):
        return self.fee + self.fee * Course.taxrate // 100


c1 = Course("Data Science", 30, 10000)
print(c1.get_net_fee())
print(Course.get_taxrate())

Course.set_taxrate(15)
c2 = Course("Workshop on AI", 2, 2000)
print(c2.get_net_fee())

c3 = Course("JavaScript", fee=5000)
c3.show()
