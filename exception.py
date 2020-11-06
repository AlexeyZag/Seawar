class IndexException(IndexError):
    def __init__(self, coordinate, allow_list):
        self.coordinate = coordinate
        self.allow_list = allow_list

    def check_coor(self):
        try:
            if int(self.coordinate) not in self.allow_list:
                raise ValueError
        except ValueError:
            return 1
