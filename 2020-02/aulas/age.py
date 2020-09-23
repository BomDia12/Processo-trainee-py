def age(days):
    years = days // 360
    days = days % 360
    months = days // 30
    days = days % 30
    print(f'{years} anos, {months} meses e {days} dias')

idade1, idade2, idade3 = input('digite as idades em dias: ').split()
age(int(idade1))
age(int(idade2))
age(int(idade3))
