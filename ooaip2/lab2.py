from abc import ABC, abstractmethod


class AbstractTask(ABC):
    def __init__(self):
        self.files_info = []
        self.file_names = []
        self.result = ''
        self.read_files()
        self.execute_task()
        self.write_result()
        print("Finished!")

    def read_files(self):
        print("Reading files...")
        print("Please, enter the number of files and then - file names")
        print("Please note, that the last file is output")
        self.file_amount = int(input())
        #for i in range(self.file_amount):
        #    self.file_names.append(input())
        self.file_names = open("files.txt").read().split(" ")
        for i in range(self.file_amount-1):
            # f = open(self.file_names[i])
            f = open(self.file_names[i])
            self.files_info.append(f.read())

    @abstractmethod
    def execute_task(self):
        pass

    def write_result(self):
        print("Writing the result into output file...")
        f = open(self.file_names[self.file_amount-1], 'w')
        f.write(self.result)


class Task1(AbstractTask):
    def execute_task(self):
        for i in range(self.file_amount-1):
            self.result += self.file_names[i] + "\n"
            self.result += self.files_info[i].upper() + "\n"

class Task2(AbstractTask):
    def execute_task(self):
        self.first_file_data = self.files_info[0]
        for i in range(self.file_amount-1):
            if i == 0: continue
            current_file_words = self.files_info[i].split(' ')
            for j in range(len(current_file_words)):
                if self.first_file_data.find(current_file_words[j]) != -1:
                    self.result += self.file_names[i] + "\n"
                    break

if __name__ == '__main__':
    task1 = Task1()
    task2 = Task2()

