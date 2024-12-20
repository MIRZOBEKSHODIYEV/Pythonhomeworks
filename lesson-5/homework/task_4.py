universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(University):
    enrollment=[university[1] for university in University]
    pay= [university[2] for university in University]
    return enrollment, pay

def mean(value):
    return sum(value)/ len(value)
    
def median(value):
    sorted_value=sorted(value)
    n=len(sorted_value)
    mid= n//2
    if n%2 == 0:
        return (sorted_value[mid - 1] + sorted_value[mid]) / 2
    else:  
        return sorted_value[mid]
enrollment, pay = enrollment_stats(universities)
total_students = sum(enrollment)
total_tuition = sum(pay)
mean_students = mean(enrollment)
median_students = median(enrollment)
mean_tuition = mean(pay)
median_tuition = median(pay)

print(f"Total students: {total_students}")
print(f"Total tuition: ${total_tuition}")
print(f"Mean number of students: {mean_students}")
print(f"Median number of students: {median_students}")
print(f"Mean tuition: ${mean_tuition}")
print(f"Median tuition: ${median_tuition}")