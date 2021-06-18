times = int(input('введите время в секундах.....'))
hours = times // 3600
minute = (times % 3600) // 60
seconds = times - (hours * 3600 + minute * 60)

print(f"{hours}:{minute}:{seconds}")
