# main.py -- put your code here!

import pyb

from pyb import Timer, Pin

tim1 = Timer(1, freq=1000)
tim2 = Timer(2, freq=1000)
tim4 = Timer(4, freq=1000)
tim5 = Timer(5, freq=1000)
tim8 = Timer(8, freq=1000)
tim9 = Timer(9, freq=1000)
tim10 = Timer(10, freq=1000)
tim11 = Timer(11, freq=1000)
tim12 = Timer(12, freq=1000)

ch_pins = []
ch_pins.append(Pin('CH1', mode=Pin.AF_PP, af=Pin.AF2_TIM5))
ch_pins.append(Pin('CH2', mode=Pin.AF_PP, af=Pin.AF2_TIM5))
ch_pins.append(Pin('CH3', mode=Pin.AF_PP, af=Pin.AF1_TIM1)) 
ch_pins.append(Pin('CH4', mode=Pin.AF_PP, af=Pin.AF1_TIM1)) 
ch_pins.append(Pin('CH5', mode=Pin.AF_PP, af=Pin.AF9_TIM12)) 
ch_pins.append(Pin('CH6', mode=Pin.AF_PP, af=Pin.AF9_TIM12)) 
ch_pins.append(Pin('CH7', mode=Pin.AF_PP, af=Pin.AF2_TIM4)) 
ch_pins.append(Pin('CH8', mode=Pin.AF_PP, af=Pin.AF3_TIM8)) 
ch_pins.append(Pin('CH9', mode=Pin.AF_PP, af=Pin.AF1_TIM1)) 
ch_pins.append(Pin('CH10', mode=Pin.AF_PP, af=Pin.AF1_TIM1)) 
ch_pins.append(Pin('CH11', mode=Pin.AF_PP, af=Pin.AF1_TIM2)) 
ch_pins.append(Pin('CH12', mode=Pin.AF_PP, af=Pin.AF1_TIM2)) 
ch_pins.append(Pin('CH13', mode=Pin.AF_PP, af=Pin.AF2_TIM4)) 
ch_pins.append(Pin('CH14', mode=Pin.AF_PP, af=Pin.AF2_TIM4)) 
ch_pins.append(Pin('CH15', mode=Pin.AF_PP, af=Pin.AF2_TIM4)) 
ch_pins.append(Pin('CH16', mode=Pin.AF_PP, af=Pin.AF3_TIM8)) 
ch_pins.append(Pin('CH17', mode=Pin.AF_PP, af=Pin.AF2_TIM5)) 
ch_pins.append(Pin('CH18', mode=Pin.AF_PP, af=Pin.AF3_TIM9))
ch_pins.append(Pin('CH19', mode=Pin.AF_PP, af=Pin.AF3_TIM11))
ch_pins.append(Pin('CH20', mode=Pin.AF_PP, af=Pin.AF1_TIM2)) 
ch_pins.append(Pin('CH21', mode=Pin.AF_PP, af=Pin.AF2_TIM5)) 
ch_pins.append(Pin('CH22', mode=Pin.AF_PP, af=Pin.AF3_TIM9)) 
ch_pins.append(Pin('CH23', mode=Pin.AF_PP, af=Pin.AF3_TIM10)) 
ch_pins.append(Pin('CH24', mode=Pin.AF_PP, af=Pin.AF1_TIM2))

ch1 = tim5.channel(3, Timer.PWM)
ch2 = tim5.channel(4, Timer.PWM)
ch3 = tim1.channel(3, Timer.PWM)
ch4 = tim1.channel(4, Timer.PWM)
ch5 = tim12.channel(1, Timer.PWM)
ch6 = tim12.channel(2, Timer.PWM)
ch7 = tim4.channel(3, Timer.PWM)
ch8 = tim8.channel(1, Timer.PWM)
ch9 = tim1.channel(1, Timer.PWM)
ch10 = tim1.channel(2, Timer.PWM)
ch11 = tim2.channel(3, Timer.PWM)
ch12 = tim2.channel(4, Timer.PWM)
ch13 = tim4.channel(1, Timer.PWM)
ch14 = tim4.channel(2, Timer.PWM)
ch15 = tim4.channel(4, Timer.PWM)
ch16 = tim8.channel(2, Timer.PWM)
ch17 = tim5.channel(1, Timer.PWM)
ch18 = tim9.channel(1, Timer.PWM)
ch19 = tim11.channel(1, Timer.PWM)
ch20 = tim2.channel(2, Timer.PWM)
ch21 = tim5.channel(2, Timer.PWM)
ch22 = tim9.channel(2, Timer.PWM)
ch23 = tim10.channel(1, Timer.PWM)
ch24 = tim2.channel(1, Timer.PWM)

def hsv2rgb(h, s, v):
    import math
    r, g, b = 0, 0, 0
    i = math.floor(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    m = i % 6
    if m == 0:
        r, g, b = v, t, p
    elif m == 1:
        r, g, b = q, v, p
    elif m == 2:
        r, g, b = p, v, t
    elif m == 3:
        r, g, b = p, q, v
    elif m == 4:
        r, g, b = t, p, v
    elif m == 5:
        r, g, b = v, p, q
    return r, g, b

def fade(delay):
    h = 0.0
    while h <= 1.0:
        r, g, b = hsv2rgb(h, 1.0, 1.0)
        ch1.pulse_width_percent(g * 100)
        ch2.pulse_width_percent(r * 100)
        ch3.pulse_width_percent(b * 100)
        pyb.udelay(delay)
        h += 0.0005

fade(1000)
