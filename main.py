def main():
    
    maleStudents = int(input("Enter the number of male students: "))
    femaleStudents = int(input("Enter the number of female students: "))
    nonbinaryStudents = int(input("Enter the number of nonbinary students: "))
    totalStudents = maleStudents + femaleStudents + nonbinaryStudents
    
    m_percentage = (maleStudents / totalStudents) * 100
    f_percentage = (femaleStudents / totalStudents) * 100
    nb_percentage = (nonbinaryStudents / totalStudents) * 100
    
    
    return maleStudents, femaleStudents, nonbinaryStudents
    
    
if __name__ == "__main__":
    main()