import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

# 1. 한글 폰트 설정 (Windows 기본 폰트)
rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False 

# 2. 삼차함수 정의
def cubic_function(x):
    return (x + 4) * (x + 1) * (x - 3)

# 3. 데이터 생성
x_data = np.linspace(-6, 5, 500)
y_data = cubic_function(x_data)

# 4. 극값 및 기준점 x_b 찾기
gradients = np.gradient(y_data, x_data)
extremas_indices = np.where(np.diff(np.sign(gradients)))[0]

idx_max = extremas_indices[0]
idx_min = extremas_indices[1]
y_local_min = y_data[idx_min]

low_y_indices_left = np.where((y_data < y_local_min) & (x_data < x_data[idx_max]))[0]
if low_y_indices_left.any():
    idx_b = low_y_indices_left[-1]

x_b = x_data[idx_b]
y_b = y_data[idx_b]

# 5. 데이터 구간 나누기
mask_dashed = x_data <= x_b - 0.1
mask_solid = x_data > x_b - 0.1

x_dashed = x_data[mask_dashed]
y_dashed = y_data[mask_dashed]

x_solid = x_data[mask_solid]
y_solid = y_data[mask_solid]

# 6. 그래프 그리기
plt.figure(figsize=(5, 4))
plt.plot(x_dashed, y_dashed, linestyle='--', color='blue', label='x <= x_b - 0.1')
plt.plot(x_solid, y_solid, linestyle='-', color='blue', label='x > x_b - 0.1')
plt.title('How can find minimum point?')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()