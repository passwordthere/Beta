import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 假设你已经有你的投资组合和沪深300指数的价格数据，格式如下：
# data = pd.DataFrame({'portfolio': [你的组合价格数据], 'index': [沪深300指数价格数据]})
# 例如，可以使用从CSV文件加载数据：
# data = pd.read_csv('your_data.csv')

# 生成一些模拟数据，实际使用时请用你的数据
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')
np.random.seed(42)
data = pd.DataFrame({
    'portfolio': np.random.normal(1.001, 0.02, len(dates)).cumprod(),  # 模拟组合价格
    'index': np.random.normal(1.001, 0.015, len(dates)).cumprod()      # 模拟沪深300价格
}, index=dates)
print(data)
# 计算对数收益率
data['portfolio_return'] = np.log(data['portfolio'] / data['portfolio'].shift(1))
data['index_return'] = np.log(data['index'] / data['index'].shift(1))

# 删除NaN值
data = data.dropna()

# 回归分析
X = data['index_return']
y = data['portfolio_return']

# 添加常数项alpha
X = sm.add_constant(X)

# 线性回归模型
model = sm.OLS(y, X).fit()

# 输出回归结果
print(model.summary())

# 获取Beta值
beta = model.params['index_return']
alpha = model.params['const']

print(f"Beta: {beta}")
print(f"Alpha: {alpha}")

# 可视化投资组合和沪深300指数的收益率关系
plt.scatter(data['index_return'], data['portfolio_return'], alpha=0.5)
plt.plot(data['index_return'], model.predict(X), color='red', label=f'Beta = {beta:.2f}')
plt.title('Portfolio Returns vs Index Returns')
plt.xlabel('Index Returns (沪深300)')
plt.ylabel('Portfolio Returns (投资组合)')
plt.legend()
plt.show()
