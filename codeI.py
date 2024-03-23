if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Find the second lowest grade
    scores = [student[1] for student in students]
    second_lowest_score = sorted(set(scores))[1]
    
    # Collect names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    # Sort names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name)
