#6.a
def main():
    try:
        marks = []
        for i in range(5):
            mark = int(input("Enter the mark: "))
            if mark == 0:
                raise ValueError("Entered Zero for a student")
            marks.append(mark)
    except ValueError as e:
        print(e)
    finally:
        print("Thank You")

main()



#6.b
def main():
    try:
        cgpa = float(input("Enter a number: "))
        if cgpa < 4.5:
            raise ValueError(f"You GPA is= {cgpa}\nYou are Not promoted to next academic year")
        else:
            print("You are promoted to next academic year")
    except ValueError as e:
        print(e)
       
    finally:
        print("Thank You")
        
main()
