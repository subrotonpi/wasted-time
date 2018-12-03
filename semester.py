import datetime as dt
import json
start = end = delta =0 

#--------------------------------------------------------------------------
def calculate_dates(day_1, day_2, semester):
    global start, end , delta
    class_dates=[]
    if day_1 == day_2 :
        flag = True #flag is true when lab
    else:
        flag = False

    for _ in  range(((end-start).days+1)//7):
        if not (day_1 >= semester['mid_s'] and day_1 <= semester['mid_e']):
            class_dates.append(str(day_1))
        day_1 +=delta

        if not flag :
            if not (day_2 >= semester['mid_s'] and day_2 <= semester['mid_e']):
                class_dates.append(str(day_2))
            day_2 +=delta
        
    return class_dates
#--------------------------------------------------------------------------
def all_course(courses):
    all_course_date = {}

    for course in courses:
        day_1 = courses[course][0]#dt.date(2018, 9, 15)
        day_2 = courses[course][1]#dt.date(2018, 9, 18)
        #find all dates
        li = (calculate_dates(day_1, day_2, semester))
         

        #adding to all course dates dictionary
        all_course_date[course] = li
    return all_course_date
#--------------------------------------------------------------------------
def prepare_semester():
    global start, end , delta, courses, semester
    #for lab day1 and day2 are same
    #edit day1 , day2 , course name 
    courses={
        'CSE122_G' : [dt.date(2018, 9, 18), dt.date(2018, 9, 19)], #day1 day2
        'CSE123_G' : [dt.date(2018, 9, 17), dt.date(2018, 9, 17)], #day1 day2
        'CSE331_G' : [dt.date(2018, 9, 16), dt.date(2018, 9, 19)], #day1 day2
        'CSE332_G' : [dt.date(2018, 9, 18), dt.date(2018, 9, 18)], #day1 day2
        'CSE331_H' : [dt.date(2018, 9, 15), dt.date(2018, 9, 17)], #day1 day2
        'CSE332_H' : [dt.date(2018, 9, 16), dt.date(2018, 9, 16)], #day1 day2
    }

    semester = {
        'year': 2018, 
        'start_month' : 9, 
        'end_month' : 12,
        'start_date' : 15, 
        'end_date' : 11, 
        'mid_s': dt.date(2018,11, 11),
        'mid_e': dt.date(2018,11, 20),
    }

    delta = dt.timedelta(days = 7)

    start = dt.date(semester['year'], semester['start_month'], semester['start_date'])
    end = dt.date(semester['year'], semester['end_month'], semester['end_date'])
    print('Semester Beings: {},  Ends: {}'.format(start, end) )

    return courses, semester
#------------------------
print('Date Format here: Year/Month/Day')
courses, semester = prepare_semester()

all_classes = all_course(courses)

print(json.dumps(all_classes, indent=6, sort_keys=True))
