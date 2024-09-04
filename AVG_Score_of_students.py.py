import csv
# For the average
from statistics import mean 
from typing import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    average=OrderedDict()
    with open(input_file_name,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            name=row[0]
            grades=[int(x) for x in row[1:] if x] # this line make a list for each row with integers
            if grades:
                avg_grade=mean(grades)
                average[name]=avg_grade
        file.close()
    ######Now we should open output file for task 1 and then write the output on it
    with open(output_file_name,'w',newline='') as task1file:
        writer=csv.writer(task1file)
        for key,value in average.items():
            writer.writerow([key,value])
        task1file.close()
        return average


def calculate_sorted_averages(input_file_name, output_file_name):
    x=calculate_averages(input_file_name,output_file_name)
    sorted_avg=OrderedDict(sorted(x.items(),key=lambda x: (x[1],x[0])))
    with open(output_file_name,'w',newline='') as task2file:
        writer=csv.writer(task2file)
        for key,value in sorted_avg.items():
            writer.writerow([key,value])
        task2file.close()
    return sorted_avg


def calculate_three_best(input_file_name, output_file_name):
    x=calculate_sorted_averages(input_file_name,output_file_name)
    count=0
    y=OrderedDict()
    for name,avg_grade in reversed(list(x.items())):
        count+=1
        y[name]=avg_grade
        if count==3:
            break
    with open(output_file_name,'w',newline='') as task3file:
        writer=csv.writer(task3file)
        for name,avg_grade in y.items():
            writer.writerow([name,avg_grade])
        task3file.close()
    return count


def calculate_three_worst(input_file_name, output_file_name):
    x=calculate_sorted_averages(input_file_name,output_file_name)
    countx=0
    with open (output_file_name,'w',newline='') as task4file:
        writer=csv.writer(task4file)
        for name,avg_grade in x.items():
            countx+=1
            writer.writerow([avg_grade])
            if countx==3:
                break
        task4file.close()
    return countx


def calculate_average_of_averages(input_file_name, output_file_name):
    x=calculate_sorted_averages(input_file_name,output_file_name)
    with open(output_file_name,'w',newline='')as task5file:
        writer=csv.writer(task5file)
        avgavg=mean(x.values())
        writer.writerow([avgavg])
        task5file.close()
    return avgavg