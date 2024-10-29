def calculate_team_performance(match_results):
  """
  Рассчитывает итоговый результат команды.

  Args:
    match_results: Список результатов матчей (True для победы, False для поражения).

  Returns:
    Итоговый результат команды.
  """

  wins = match_results.count(True)
  total_matches = len(match_results)
  win_rate = wins / total_matches

  if win_rate > 0.5:
    bonus = 10  
  else:
    bonus = 0

  return win_rate * 100 + bonus

def player_performance(player_scores):
  """
  Рассчитывает средний результат игрока.

  Args:
    player_scores: Список очков, набранных игроком в каждом матче.

  Returns:
    Средний результат игрока.
  """

  total_points = sum(player_scores)
  total_matches = len(player_scores)

  average_score = total_points / total_matches

  for score in player_scores:
    if score > 30:
      average_score += 1  

  return average_score

def final_report(team_result, player_averages):
  """
  Выводит итоговый отчет о выступлении команды.

  Args:
    team_result: Итоговый результат команды.
    player_averages: Список средних результатов игроков.
  """

  average_player_score = sum(player_averages) / len(player_averages)

  if team_result >= 80 and average_player_score >= 20:
    print("Отличная команда!")
  else:
    print("Есть над чем работать.")

team_results = [True, True, False, True, False]
player_a_scores = [25, 35, 20, 40, 32]
player_b_scores = [18, 22, 25, 28, 30]

team_performance = calculate_team_performance(team_results)
player_a_average = player_performance(player_a_scores)
player_b_average = player_performance(player_b_scores)

final_report(team_performance, [player_a_average, player_b_average])