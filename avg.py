class Student:
    def __init__(self):
        self.my_dict = {}

    def Add(self):
        for i in range(int(input("Enter the number of students: "))):
            key = str(input("Enter student name: "))
            value = input("Enter scores (separated by spaces): ").split()
            self.my_dict[key] = value
        print(self.my_dict)

    def Delete(self):
        key_to_delete = input("Enter key to delete: ")
        if key_to_delete in self.my_dict:
            del self.my_dict[key_to_delete]
            print(f"{key_to_delete} removed from the dictionary")
        else:
            print(f"{key_to_delete} not found in the dictionary")

    def Average(self):
        for key, value in self.my_dict.items():
            value = [float(v) for v in value]
            avg = sum(value) / len(value)
            self.my_dict[key] = avg
        print(self.my_dict)
    #def Class_Average(self):


def main():
    print("Welcome to grade Central\n[1]-Enter Grades\n[2]-remove student\n[3]-Student Average grades\n[4]-Exit")
    student = Student()
    while True:
        a = int(input("Choose an option from above: "))
        if a == 1:
            print("Welcome to Enter grades :")
            student.Add()
        elif a == 2:
            print("Please enter key to delete:")
            student.Delete()
        elif a == 3:
            print("Class Averages :")
            student.Average()
        elif a == 4:
            print("Thank you")
            break
        else:
            print("Invalid option, please try again")
def myNAma():
    x=input("Enter user Name : ")
    y=input("Enter Password : ")
    if y == "1234":
        main()
    else:
        print("Enter Correct")
        myNAma()
while True:
    user=input("enter-1111")
    Password="1111"
    if user==Password:
        myNAma()
        break
    else:
        print("ENter correct pass and try again")
