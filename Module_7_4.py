# Использование %:

team1 = 'Мастер кода'
team2 = 'Волшебники данных'

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = round(float(team1_time/score_1+team2_time/score_2)/2,1)



def challenge_result():
    if score_1 >= score_2 and team1_time>team2_time:
        print(f'Победа команды {team1}!')
    elif score_1 <= score_2 and team1_time<team2_time:
        print(f'Победа команды {team2}!')
    else:
        print('Ничья!')

print('В команде %s участников: %s!' % (team1, team1_num))
print('Итого сегодня в командах учатников: %s и %s!' %(team1_num, team2_num))

# Использование format():
print('Команда {} решила задач:{}!'.format(team2, score_2))

print('{} решили задачи за {} с!'.format(team2,team2_time))

# Использование  f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено задач {tasks_total}, в среднем по {time_avg} секунду на задачу!')

print(challenge_result())
