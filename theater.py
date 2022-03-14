'''
author: garvin
date: 03/12/2022
'''


def read_file(file_name):
    # return request array like [[R001,2],[R002,4]]
    request_array = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            request_array.append(line.split())
    return request_array


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        if isinstance(content, str):
            f.write(content)
            f.write('\n')
        elif isinstance(content, list):
            for line in content:
                f.write(line)
                f.write('\n')
        else:
            pass


def seat_map(number):
    # 0 to 'A', 1 to 'B'
    return chr((ord(str(number)) + 17))


class Theater:
    def __init__(self, file_name, rows=10, columns=20, buffer_seats=3):
        self.rows = rows
        self.columns = columns
        self.number_of_seats = self.rows * self.columns
        self.file_name = file_name
        self.remain_seats = [self.columns for _ in range(self.rows)]
        self.write_file_name = 'output_'+self.file_name
        self.buffer_seats = buffer_seats
        self.safe_row = 1

    def reserve(self):
        request_array = read_file(self.file_name)
        output = []

        for request in request_array:
            line = ''
            identify, group_number = request[0], int(request[1])

            if group_number <= 0:
                line = identify + ' ' + 'seat number illegal:' + str(group_number)
            elif group_number > self.number_of_seats:
                line = identify + ' ' + 'Not enough seats left'
            elif group_number > self.columns:
                line = identify + ' ' + 'group number should be less than or equal to 20'
            else:
                line = identify + ' ' + self.allocate(identify, group_number)[:-1]
            output.append(line)

        #print(output)
        write_file(self.write_file_name, output)
        return self.write_file_name

    def allocate(self, identify, group_number):
        # return assigned seats [F16,F17,F18,F19]
        row = self.rows // 2 - 1
        up = True
        counter = self.safe_row
        res = ''

        # if this group can be allocated in one row
        while 0 <= row < self.rows:
            if group_number <= self.remain_seats[row]:
                for i in range(self.columns - self.remain_seats[row] + 1,
                               self.columns - self.remain_seats[row] + 1 + group_number):
                    res += seat_map(row) + str(i) + ','
                seats = min(group_number +self.buffer_seats, self.remain_seats[row])
                self.remain_seats[row] -= seats
                self.number_of_seats -= seats
                return res

            if up:
                row += counter
                counter += self.safe_row
                up = False
            else:
                row -= counter
                counter += self.safe_row
                up = True

        # if this group have to be allocated in different rows

        row = self.rows // 2 - 1
        up = True
        counter = self.safe_row
        res = ''
        print(self.number_of_seats,self.remain_seats)
        while group_number > 0:
            if self.remain_seats[row] > 0:
                start = self.columns - self.remain_seats[row] + 1
                for i in range(start, self.columns+1):
                    if group_number > 0:

                        res += seat_map(row) + str(i) + ','
                        group_number -= 1
                        self.remain_seats[row] -= 1
                        self.number_of_seats -= 1
            if self.remain_seats[row] != 0:
                self.remain_seats[row] -=min(self.remain_seats[row], self.buffer_seats)
                self.number_of_seats -= min(self.remain_seats[row], self.buffer_seats)

            if up:
                row += counter
                counter += self.safe_row
                up = False
            else:
                row -= counter
                counter += self.safe_row
                up = True
        return res
