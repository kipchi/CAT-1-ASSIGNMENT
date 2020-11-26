# question a
def csc_217_attendance():
    attendance_30 = open("CSC_217_attendance_ week1_30.txt", 'r').readlines()
    attendance_end = open("CSC_217_attendance_ week1_end.txt", "r").readlines()
    attendance_30 += attendance_end
    uniques = set(attendance_30)
    csc_attendance = open("CSC_217_attendance_ week1.txt", "w")

    for line in uniques:
        csc_attendance.write(line)


csc_217_attendance()
