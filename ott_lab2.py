import numpy as np

# Функція для побудови матриці Мюллера фазової пластинки (λ/4 або λ/2)
def waveplate_matrix(delta, alpha):
    """Створює матрицю Мюллера для фазової пластинки з фазовим зсувом delta і нахилом осі alpha"""
    cos2a = np.cos(2 * alpha)
    sin2a = np.sin(2 * alpha)
    cosd = np.cos(delta)
    sind = np.sin(delta)
    
    return np.array([
        [1, 0, 0, 0],
        [0, cos2a**2 + sin2a**2 * cosd, cos2a * sin2a * (1 - cosd), -sin2a * sind],
        [0, cos2a * sin2a * (1 - cosd), sin2a**2 + cos2a**2 * cosd, cos2a * sind],
        [0, sin2a * sind, -cos2a * sind, cosd]
    ])

# Вхідний і вихідний вектори Стокса
S_in = np.array([1, -0.245, -0.363, 0.899])
S_out_expected = np.array([1, -0.03, -0.171, 0.985])

# Кути фазових пластинок (λ/4, λ/2, λ/4) у градусах
alpha1, alpha2, alpha3 = -62, -60, -50

# Перетворення у радіани
alpha1_rad = np.radians(alpha1)
alpha2_rad = np.radians(alpha2)
alpha3_rad = np.radians(alpha3)

# Побудова матриць фазових пластинок
M1 = waveplate_matrix(np.pi / 2, alpha1_rad)  # λ/4 пластинка
M2 = waveplate_matrix(np.pi, alpha2_rad)      # λ/2 пластинка
M3 = waveplate_matrix(np.pi / 2, alpha3_rad)  # λ/4 пластинка

# Обчислення загальної передавальної матриці
M_total = M3 @ M2 @ M1

# Обчислення вихідного вектора Стокса
S_calc = M_total @ S_in

# Обчислення похибки для кожного компонента окремо
errors = np.abs(S_out_expected - S_calc)

# Вивід результатів
print("Обчислений вихідний вектор Стокса:")
print(S_calc)

print("\nОчікуваний вихідний вектор Стокса:")
print(S_out_expected)

print("\nПохибка для кожного компонента:")
for i in range(len(S_calc)):
    print(f"ΔS[{i}] = {errors[i]:.6f}")
