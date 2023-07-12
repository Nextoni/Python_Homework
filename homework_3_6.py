def gas_station(distance, tank_size, stations):
    result = []
    temp = 0
    tank_size_temp = tank_size

    for st in range(len(stations)):
        if tank_size < stations[st] and tank_size < distance and tank_size_temp == tank_size:
            tank_size_temp = stations[st - 1] + tank_size
            temp = stations[st - 1]
            result.append(temp)

        elif tank_size_temp < stations[st] and tank_size_temp < distance:
            tank_size_temp = stations[st - 1] + tank_size
            temp = stations[st - 1]
            result.append(temp)

    if tank_size_temp > stations[len(stations) - 1] and tank_size_temp < distance:
        result.append(stations[len(stations) - 1])

    return result

print(gas_station(390, 80, [70, 90, 140, 210, 240, 280, 350]))