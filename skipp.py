start_point = int(input("Enter a starting point: "))
end_point = int(input("Enter a end point: "))
skipp_point = int(input("Enter a skipp point: "))
while start_point < end_point:
    if start_point == skipp_point:
        start_point = start_point + 1
        continue
    print(start_point)
    start_point = start_point + 1




