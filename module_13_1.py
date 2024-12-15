# Домашнее задание по теме "Асинхронность на практике"
import asyncio


# Функция start_strongman имитирует процесс поднятия шаров силачем
async def start_strongman(name, power):
    # Выводим сообщение о старте соревнований для данного силача
    print(f"Силач {name} начал соревнования.")

    # Поднимаем 5 шаров
    for i in range(1, 6):
        # Задержка перед поднятием следующего шара обратно пропорциональна мощности силача
        await asyncio.sleep(1 / power)

        # Выводим сообщение о том, что силач поднял очередной шар
        print(f"Силач {name} поднял {i} шар")

    # После того как все шары подняты, выводим сообщение об окончании соревнований
    print(f"Силач {name} закончил соревнования.")


# Функция start_tournament запускает три задачи для разных силачей
async def start_tournament():
    # Создаем три задачи для трех силачей с разными именами и мощностями
    task_pasha = asyncio.create_task(start_strongman("Pasha", 3))
    task_denis = asyncio.create_task(start_strongman("Denis", 4))
    task_apollon = asyncio.create_task(start_strongman("Apollon", 5))

    # Ожидаем завершения каждой задачи
    await task_pasha
    await task_denis
    await task_apollon


# Запускаем турнир
asyncio.run(start_tournament())