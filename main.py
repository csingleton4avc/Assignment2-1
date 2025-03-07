def main():
    
    maleStudents = int(input("Enter the number of male students: "))
    femaleStudents = int(input("Enter the number of female students: "))
    nonbinaryStudents = int(input("Enter the number of nonbinary students: "))
    totalStudents = maleStudents + femaleStudents + nonbinaryStudents
    
    m_percentage = (maleStudents / totalStudents) * 100
    f_percentage = (femaleStudents / totalStudents) * 100
    nb_percentage = (nonbinaryStudents / totalStudents) * 100
    
    print(f"The total number of students is: \t{totalStudents}")
    print(f"The number of males, females and non-binary: \t{maleStudents}, \t{femaleStudents}, \t{nonbinaryStudents}")
    print(f"The percentage of males, females and non-binary: \t{m_percentage:.2f}%, \t{f_percentage:.2f}%, \t{nb_percentage:.2f}%")
    
    
    return maleStudents, femaleStudents, nonbinaryStudents
    
    
if __name__ == "__main__":
    main()