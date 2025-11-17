# data_samples.py
"""
스마트팩토리 실습용 샘플 데이터 모음 모듈.

포함 내용:
- 단일 센서 통합 샘플 (scenario 라벨 포함)
- 온도 로그 샘플
- 압력 누설 시나리오 샘플
- 비지도 학습용 샘플 (라벨 없음)
- 멀티센서 샘플 (3상 전류, 3축 진동, 2채널 압력, 온도)

SAMPLE_DATASETS 딕셔너리를 통해 Streamlit 등에서 쉽게 선택 가능.
"""

import pandas as pd


def make_sample_smartfactory_sensor() -> pd.DataFrame:
    """
    전류/온도/진동/압력 + scenario 라벨이 포함된 스마트팩토리 센서 샘플 데이터.

    구간:
    - 0~9  : normal_run
    - 10~19: overload_trend
    - 20~29: vibration_issue
    """
    data = [
        # normal 구간 (0~9)
        *[
            {
                "time_s": t,
                "motor_current_A": 1.0 + (t % 3) * 0.02,
                "motor_temp_C": 42.0 + t * 0.15,
                "vibration_rms_g": 0.08 + (t % 2) * 0.01,
                "pressure_bar": 6.55 - (t % 3) * 0.01,
                "scenario": "normal_run",
            }
            for t in range(0, 10)
        ],
        # overload 구간 (10~19)
        *[
            {
                "time_s": 10 + i,
                "motor_current_A": 1.05 + i * 0.05,
                "motor_temp_C": 45.0 + i * 1.5,
                "vibration_rms_g": 0.11 + i * 0.01,
                "pressure_bar": 6.54 - i * 0.01,
                "scenario": "overload_trend",
            }
            for i in range(0, 10)
        ],
        # vibration issue 구간 (20~29)
        *[
            {
                "time_s": 20 + i,
                "motor_current_A": 1.05 + (i % 2) * 0.01,
                "motor_temp_C": 45.5 + i * 0.2,
                "vibration_rms_g": 0.25 + i * 0.05,
                "pressure_bar": 6.55 - i * 0.01,
                "scenario": "vibration_issue",
            }
            for i in range(0, 10)
        ],
    ]
    return pd.DataFrame(data)


def make_sample_temperature_only() -> pd.DataFrame:
    """
    온도만 있는 간단한 설비 온도 로그 샘플.

    - 0~29분까지 시간에 따른 온도 변화
    - 15~20분 구간에서 과열 경향이 나타나도록 구성
    """
    rows = []
    temp = 40.0
    for t in range(0, 30):
        if 15 <= t <= 20:
            temp += 1.5  # 과열 구간
        else:
            temp += 0.2
        rows.append({"time_min": t, "temp_C": round(temp, 1)})
    return pd.DataFrame(rows)


def make_sample_pressure_leak() -> pd.DataFrame:
    """
    압력센서 누설을 가정한 샘플 데이터.

    - 0~9초   : 정상 범위에서 미세 감소
    - 10~19초 : 누설 진행 구간 (감소 속도 증가)
    - 20~29초 : 급격한 누설 구간
    """
    data = []
    pressure = 7.0
    for t in range(0, 30):
        if t < 10:
            pressure -= 0.01  # 정상 미세 감소
        elif 10 <= t < 20:
            pressure -= 0.05  # 누설 진행
        else:
            pressure -= 0.1   # 급격 누설
        data.append({"time_s": t, "pressure_bar": round(pressure, 2)})
    return pd.DataFrame(data)


def make_sample_unsupervised_sensor() -> pd.DataFrame:
    """
    라벨이 없는 비지도 학습용 센서 데이터 샘플.

    - scenario 컬럼 없음 (라벨 X)
    - time_s, motor_current_A, motor_temp_C, vibration_rms_g, pressure_bar
    - 0~9  : 비교적 정상
    - 10~19: 과부하 경향
    - 20~29: 진동 이상 경향
    """
    data = [
        # normal-ish 구간 (0~9)
        *[
            {
                "time_s": t,
                "motor_current_A": 1.0 + (t % 3) * 0.01,
                "motor_temp_C": 42.0 + t * 0.15,
                "vibration_rms_g": 0.08 + (t % 2) * 0.01,
                "pressure_bar": 6.55 - (t % 2) * 0.01,
            }
            for t in range(0, 10)
        ],
        # overload 경향 구간 (10~19)
        *[
            {
                "time_s": 10 + i,
                "motor_current_A": 1.05 + i * 0.05,
                "motor_temp_C": 45.0 + i * 1.3,
                "vibration_rms_g": 0.11 + i * 0.01,
                "pressure_bar": 6.54 - i * 0.01,
            }
            for i in range(0, 10)
        ],
        # vibration issue 경향 구간 (20~29)
        *[
            {
                "time_s": 20 + i,
                "motor_current_A": 1.05 + (i % 2) * 0.01,
                "motor_temp_C": 45.5 + i * 0.2,
                "vibration_rms_g": 0.24 + i * 0.05,
                "pressure_bar": 6.55 - i * 0.01,
            }
            for i in range(0, 10)
        ],
    ]
    return pd.DataFrame(data)


def make_sample_multisensor() -> pd.DataFrame:
    """
    여러 센서(3상 전류, 3축 진동, 2채널 압력, 온도)가 포함된 멀티센서 샘플 데이터.

    구간:
    - 0~14 : normal
    - 15~24: overload (전류/온도 증가)
    - 25~39: vibration issue (진동 급증)
    """
    rows = []
    base_temp = 42.0
    base_pressure_main = 6.8
    base_pressure_sub = 6.5

    for t in range(0, 40):
        if t < 15:
            # Normal
            cur1 = 1.0 + 0.02 * (t % 3)
            cur2 = 1.0 + 0.01 * (t % 4)
            cur3 = 1.0 + 0.015 * (t % 5)
            vib_x = 0.08 + 0.005 * (t % 2)
            vib_y = 0.09 + 0.004 * (t % 3)
            vib_z = 0.07 + 0.006 * (t % 2)
            temp = base_temp + 0.15 * t
            p_main = base_pressure_main - 0.01 * (t % 3)
            p_sub = base_pressure_sub - 0.01 * (t % 2)
        elif 15 <= t < 25:
            # Overload (전류/온도 증가)
            i = t - 15
            cur1 = 1.1 + 0.07 * i
            cur2 = 1.08 + 0.05 * i
            cur3 = 1.12 + 0.06 * i
            vib_x = 0.12 + 0.01 * i
            vib_y = 0.13 + 0.012 * i
            vib_z = 0.11 + 0.011 * i
            temp = base_temp + 0.2 * t + 1.0 * i
            p_main = base_pressure_main - 0.02 * i
            p_sub = base_pressure_sub - 0.015 * i
        else:
            # Vibration issue (진동만 크게 증가)
            i = t - 25
            cur1 = 1.15 + 0.01 * (i % 3)
            cur2 = 1.13 + 0.01 * (i % 4)
            cur3 = 1.14 + 0.01 * (i % 5)
            vib_x = 0.3 + 0.05 * i
            vib_y = 0.28 + 0.045 * i
            vib_z = 0.32 + 0.055 * i
            temp = base_temp + 0.25 * t
            p_main = base_pressure_main - 0.03 * i
            p_sub = base_pressure_sub - 0.02 * i

        rows.append(
            {
                "time_s": t,
                "motor_current_A1": round(cur1, 3),
                "motor_current_A2": round(cur2, 3),
                "motor_current_A3": round(cur3, 3),
                "vib_x_g": round(vib_x, 3),
                "vib_y_g": round(vib_y, 3),
                "vib_z_g": round(vib_z, 3),
                "pressure_main_bar": round(p_main, 3),
                "pressure_sub_bar": round(p_sub, 3),
                "temp_C": round(temp, 2),
            }
        )
    return pd.DataFrame(rows)


SAMPLE_DATASETS = {
    "샘플 1) 스마트팩토리 센서 통합 데이터": make_sample_smartfactory_sensor,
    "샘플 2) 설비 온도 로그": make_sample_temperature_only,
    "샘플 3) 공압 압력 누설 시나리오": make_sample_pressure_leak,
    "샘플 4) 비지도 학습용 센서 데이터(라벨 없음)": make_sample_unsupervised_sensor,
    "샘플 5) 멀티센서 데이터(3상 전류·3축 진동·2채널 압력)": make_sample_multisensor,
}
