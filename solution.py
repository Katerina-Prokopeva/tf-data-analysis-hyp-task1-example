import pandas as pd
import numpy as np


chat_id = 345280072 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Пропорции успехов
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Стандартная ошибка разности долей
    se_diff = np.sqrt(p1 * (1 - p1) / x_cnt + p2 * (1 - p2) / y_cnt)
    
    # Z-статистика
    z_stat = (p1 - p2) / se_diff
    
    # Критическое значение для уровня значимости 0.05
    critical_value = norm.ppf(1 - 0.05 / 2)
    
    # Проверяем условие для отклонения нулевой гипотезы
    reject_null = abs(z_stat) > critical_value
    
    return reject_null
   
