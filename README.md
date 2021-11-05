## Билдим
`docker-compose up --build -d`
## Входим в конейнер для тестов
`docker exec -ti painter bash`
## Пока можно посмотреть рисование линий и прямоугольников, примеры команд:
```
python script.py -c 'C 20 10'
python script.py -c 'L 14 9 20 9'
python script.py -c 'L 14 10 14 10'
python script.py -c 'L 1 9 5 9'
python script.py -c 'L 5 10 5 10'
python script.py -c 'L 18 1 18 4'
python script.py -c 'L 18 4 20 4'
python script.py -c 'L 1 2 3 2'
python script.py -c 'L 3 1 3 1'
python script.py -c 'R 8 5 11 8'
python script.py -c 'B 1 20 c' # еще не реализовано
```
Результат - файл picture.txt