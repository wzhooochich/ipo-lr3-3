print("Введите день(число) и месяц(название месяца), после чего программа выведет вам , какая это пора года.")
# инициализациия переменных
day=int(input("введите день:"))
month=str(input("введите месяц:"))

#проверка с помощью if else
if day<1 or day>31 :         
    print("некорректно введен день.")
    
elif month=="март" and day>=1 or month=="апрель" or month=="май" and day<=31 :
    print("Весна!")

elif month=="июнь" and day>=1 or month=="июль" or month=="август" and day<=31 :
    print("Лето!")

elif month=="сентябрь" and day>=1 or month=="октябрь" or month=="ноябрь" and day<=30 :
    print("Осень")

elif month=="декабрь" and day>=1 or month=="январь" or month=="февраль" and day<=28:
    print("Зима...")
    
else :
    print("ERROR")
