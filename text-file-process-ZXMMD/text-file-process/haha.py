s = "201811123015"
count = 0

with open('text-file-process/log_files/201811123015.log',encoding='utf8') as f:
    for line in f:
        line = line[14:26]
        if s == line:
            count = count + 1

print(count)