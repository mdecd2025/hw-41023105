from controller import Robot, Keyboard

# 初始化 Robot 和 Keyboard
robot = Robot()
keyboard = Keyboard()

# 時間步長
TIME_STEP = 32

# 啟用鍵盤監聽
keyboard.enable(TIME_STEP)

# 獲取車輪馬達設備
motor1 = robot.getDevice("motor1")  # 左前輪
motor2 = robot.getDevice("motor2")  # 左後輪
motor3 = robot.getDevice("motor3")  # 右前輪
motor4 = robot.getDevice("motor4")  # 右後輪

# 設置馬達為速度模式
for motor in [motor1, motor2, motor3, motor4]:
    motor.setPosition(float('inf'))  # 無限旋轉模式（速度控制）
    motor.setVelocity(0)  # 初始速度為 0

# 設定速度
SPEED = 5.0  # 前進/後退速度
TURN_SPEED = 5.0  # 左右鍵特定行為的速度

# 主循環
while robot.step(TIME_STEP) != -1:
    # 偵測鍵盤輸入
    key = keyboard.getKey()

    if key == Keyboard.UP:  # 向上鍵：四輪正向旋轉，車子前進
        motor1.setVelocity(SPEED)   # 左前輪
        motor2.setVelocity(SPEED)   # 左後輪
        motor3.setVelocity(SPEED)   # 右前輪
        motor4.setVelocity(SPEED)   # 右後輪
    elif key == Keyboard.DOWN:  # 向下鍵：四輪反向旋轉，車子後退
        motor1.setVelocity(-SPEED)  # 左前輪
        motor2.setVelocity(-SPEED)  # 左後輪
        motor3.setVelocity(-SPEED)  # 右前輪
        motor4.setVelocity(-SPEED)  # 右後輪
    elif key == Keyboard.LEFT:  # 左鍵：左邊前後輪後退，右邊前後輪前進
        motor1.setVelocity(-TURN_SPEED)  # 左前輪後退
        motor2.setVelocity(-TURN_SPEED)  # 左後輪後退
        motor3.setVelocity(TURN_SPEED)   # 右前輪前進
        motor4.setVelocity(TURN_SPEED)   # 右後輪前進
    elif key == Keyboard.RIGHT:  # 右鍵：左邊前後輪前進，右邊前後輪後退
        motor1.setVelocity(TURN_SPEED)   # 左前輪前進
        motor2.setVelocity(TURN_SPEED)   # 左後輪前進
        motor3.setVelocity(-TURN_SPEED)  # 右前輪後退
        motor4.setVelocity(-TURN_SPEED)  # 右後輪後退
    else:  # 沒有按鍵：所有輪子停止
        motor1.setVelocity(0)
        motor2.setVelocity(0)
        motor3.setVelocity(0)
        motor4.setVelocity(0)