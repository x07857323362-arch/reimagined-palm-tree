from setuptools import setup, find_packages

setup(
    name='trading-system',
    version='0.1.0',
    description='Professional trading system with AI integration',
    author='Trading Team',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scipy>=1.7.0',
        'ccxt>=1.90.0',
        'scikit-learn>=1.0.0',
    ],
    python_requires='>=3.8',
)
