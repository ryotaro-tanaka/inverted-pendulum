# curtain pole

AI learning for a game where you move the pedestal left and right to prevent the pole from falling.

## Summary

I will summarize the code and execution steps for the AI reinforcement learning introduction provided by volunteers on YouTube for study purposes. 
The YouTube videos by the volunteers are described below.

[たったの10行！AI強化学習してみた！カートポール！#ai #python](https://www.youtube.com/shorts/nupxtLfLX7s)

## Steps to Execute

#### 1. Checking Python version

```bash
$ python --version
Python 3.13.2
```

#### 2. Creating a Virtual Environment for Python

Because I want to install packages in a virtual environment rather than in the global environment.

```bash
$ python -m venv venv
```

#### 3. Activating the Virtual Environment

```bash
$ source venv/Scripts/activate
```

#### 4. Verify that the virtual environment is active

```bash
$ which pip
~/pg0029.py/venv/Scripts/pip
```

#### 5. Installing Packages

```bash
$ pip install gymnasium stable-baselines3 pygame opencv-python
```

#### 6. Execute

```bash
$ python pg0029.py
```

#### 7. Deactivating the Virtual Environment

```bash
$deactivate
```

## Supplement

To change the number of steps, adjust the value of X."

```py
model.learn(total_timesteps=X)
```