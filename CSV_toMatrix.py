class CSV_Reader:
    def __init__(self, fileName):
        # Open and read file
        with open(fileName) as file:
            text = file.read()

        # Convert to rows
        all_row = text.split("\n")

        # First Row is only names
        name = all_row[0].split(",")[1:] # 1: to remove lead comma.

        # Rest is matrix data
        matrix_info = all_row[1:]

        self._next_id = 0
        self._id_to_label, self._label_to_id = self._set_up_labels(name)
        self._matrix = self._set_up_matrix(matrix_info)

    def _set_up_matrix(self, matrix_data):
        size_of_matrix = len(self._id_to_label.keys())
        matrix = [[0 for _ in range(size_of_matrix)] for _ in range(size_of_matrix)]

        # remove lead label every entry
        for i in range(len(matrix_data)):
            matrix[i] = list(map(int, matrix_data[i].split(",")[1:]))

        return matrix


    def _get_next_id(self):
        value = self._next_id
        self._next_id = self._next_id + 1
        return value


    def _set_up_labels(self, labels):
        id_to_label = {}
        label_to_id = {}

        for label in labels:
            i = self._get_next_id()
            id_to_label[i] = label
            label_to_id[label] = i

        return id_to_label,label_to_id

    def id_to_label(self, id):
        return self._id_to_label[id]

    def label_to_id(self, label):
        return self._label_to_id[label]

    def get_matrix(self):
        return self._matrix

    def get_labels(self):
        return self._label_to_id.keys()

    def get_cell_value(self,id1,id2):
        return self._matrix[id1][id2]

    def display_matrix(self):
        space_size = max(map(lambda i: len(i),self.get_labels())) + 5
        EMPTY = " "
        text ="".rjust(space_size,EMPTY) + "".join(map(lambda i : i.ljust(space_size, EMPTY),self.get_labels())) + "\n"
        for i,row in enumerate(self.get_matrix()):
            text = text + self._id_to_label[i].ljust(space_size,EMPTY) + "".join(map(lambda i : i.ljust(space_size, EMPTY),map(str,row))) + "\n"

        print(text)


    def set_value(self, id1, id2, value):
        name1 = self._id_to_label[id1]
        name2 = self._id_to_label[id2]
        print(f"Setting value of name1={name1} and name2={name2}")
        str_value = str(value)
        self._matrix[id1][id2] = str_value
        self._matrix[id2][id1] = str_value

    def increment_edge(self, id1,id2):
        name1 = self._id_to_label[id1]
        name2 = self._id_to_label[id2]
        print(f"Incrementing value of name1={name1} and name2={name2} by one")
        prev = self._matrix[id1][id2]
        self._matrix[id1][id2] = prev + 1
        self._matrix[id2][id1] = prev + 1


    def add_new_label(self, label):
        id = self._get_next_id()
        self._label_to_id[label] = id
        self._id_to_label[id] = label

        for row in self._matrix:
            row.append(0)

        self._matrix.append([0 for _ in range(len(self.get_labels()))])
        self.display_matrix()


    def save_to_file(self, fileName):
        text = "," + ",".join(self.get_labels()) + "\n"
        for i, row in enumerate(self.get_matrix()):
            text = text + self._id_to_label[i] + "," + ",".join(map(str,row)) + "\n"

        with open(fileName, "w") as file:
            file.write(text)




