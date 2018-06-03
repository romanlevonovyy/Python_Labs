import re




def NASA_search_in_log_file():
    count = 0
    file = open('access.log.txt')
    for line in file:
        if re.search('2[3-5]/Mar/2009:0[0-9]:[0-5][0-9]:[0-5][0-9].*OPTIONS', str(line)):
            count+=1
            print(line)
    print(count)



    file.close()


if __name__ == "__main__":
    NASA_search_in_log_file()



