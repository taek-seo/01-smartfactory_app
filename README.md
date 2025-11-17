# 01-smartfactory_app

# 🤖 SmartFactory AI Analyzer  
OPC-UA 기반 설비·센서 데이터를 생성형 AI(OpenAI API)를 이용해  
웹에서 자동으로 **요약 / 이상행 검출 / 보고서 생성** 하는 Streamlit 앱입니다.

이 프로젝트는  
- 스마트팩토리 센서데이터 활용  
- 생성형 AI를 통한 자동 진단  
- 실습 중심 교육(폴리텍 인공지능과 / 직업훈련)  
을 목표로 구성되었습니다.

---

## 📂 폴더 구조

```
01-smartfactory_app/
│
├── app.py                # Streamlit 메인 앱(UI)
├── ai_analysis.py        # OpenAI API 분석 모듈
├── data_samples.py       # 샘플 데이터 생성 모듈
├── requirements.txt      # 의존성 패키지 목록
└── README.md
```

(샘플 CSV 파일은 실행 시 data_samples.py에서 자동 생성합니다.)

---

## 🧠 주요 기능

### 1) CSV 업로드 or 샘플 데이터 선택  
- 직접 업로드한 설비 로그 데이터 분석  
- 제공된 샘플(5종) 중 선택하여 실습 가능  

### 2) 생성형 AI 기반 자동 분석  
- **센서 이상행(Anomaly) 탐지**  
- **설비 상태 요약(전류/온도/진동/압력)**  
- **설비 점검 보고서 자동 생성**  
- **사용자 정의 프롬프트 기반 분석도 가능**  

### 3) 멀티센서 & 비지도 데이터 지원  
- 3상(Phase) 전류  
- 3축(축별) 진동  
- 2채널 압력  
- 온도 등 복합 데이터 구조도 AI 분석 가능  

### 4) 교육·시연에 최적화  
- 학생들이 직접 CSV를 올려 분석 결과 확인  
- 프롬프트를 수정하며 생성형 AI 활용 실습  
- 산업 현장형 스마트팩토리 교육 콘텐츠

---

## 🧪 제공되는 샘플 데이터

`data_samples.py` 내부에서 자동 생성:

| 샘플명 | 설명 |
|--------|------|
| 샘플 1 | 정상 → 과부하 → 진동이상 구간 포함된 센서 통합 데이터 |
| 샘플 2 | 설비 온도(Time-series) 로그 |
| 샘플 3 | 공압 압력 누설 시나리오 |
| 샘플 4 | **라벨 없는 비지도 학습용 데이터** |
| 샘플 5 | **멀티센서 데이터(3상 전류·3축 진동·2채널 압력·온도)** |

Streamlit UI에서 자동으로 선택 가능.

---

## 🚀 실행 방법

### 0. 프로젝트 클론
```bash
git clone https://github.com/taek-seo/01-smartfactory_app.git
cd 01-smartfactory_app
```

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. OpenAI API Key 설정

#### 방법 1) Streamlit UI에서 입력  
앱 실행 후 사이드바에서 직접 입력

#### 방법 2) `.streamlit/secrets.toml` 파일 생성  
(원한다면 강의용으로 더 안전한 방식)

```
# .streamlit/secrets.toml
openai_api_key = "YOUR_API_KEY"
```

---

## 3. 앱 실행
```bash
streamlit run app.py
```

브라우저가 자동으로 열립니다:

```
http://localhost:8501
```

---

## 🧭 앱 사용 절차 (요약)

1. 사이드바에서 API Key 입력  
2. 데이터 선택  
   - CSV 업로드  
   - 샘플 데이터 선택  
3. 분석 모드 선택  
   - 센서 이상 탐지  
   - 설비 점검 보고서 생성  
   - 사용자 정의 프롬프트  
4. **분석 실행 버튼 클릭 → AI 결과 출력**

---

## 📘 예시 스크린 흐름

1) 데이터 미리보기  
2) AI 분석 결과 (Bullet 기반 요약)  
3) 위험 구간 / 패턴 탐지  
4) 권장 조치 자동 생성  

---

## 🔒 주의사항

- API Key는 절대 GitHub에 올리지 말 것  
- `.env`, `secrets.toml`, 환경변수 사용 권장  
- 데이터 파일에 개인정보 포함 금지(실습 목적)

---

## 📄 License

MIT License (자유롭게 수정·확장 가능)

---

## ⭐ 앞으로 확장 가능한 기능

- RPA 연동(보고서 자동 전송 / Slack 알림)
- OPC-UA 실시간 데이터 스트리밍 연결
- 간단한 ML 기반 이상탐지 모델 추가
- 시각화(D3.js / Plotly)로 확장
- Streamlit Cloud / HuggingFace Space 배포

---

### 📬 문의  
교육 세팅 / 확장 개발 / 오류 해결 모두 도와드릴 수 있어요 😄

