# Write your code here
def cakes(eggs, butter, flour):
    answer = 0
    while(eggs >= 5 and butter >= 250 and flour >= 250):
        eggs -= 5
        butter -= 250
        flour -= 250
        answer += 1
        print(eggs , butter , flour)
    return answer

print(cakes(8 , 500 ,300))