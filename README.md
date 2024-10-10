# Streamlit 튜토리얼 😁

`Streamlit`을 활용하여 파이썬 코드로 빠르게 웹앱(WebApp)을 생성할 수 있습니다.
사용법도 굉장히 쉽고, 무료 호스팅 기능도 지원해주기 때문에, 데모 앱을 만들어 볼 때 굉장히 유용합니다.

anaconda 설치

vscode 설치

ctrl + shift + p  > Python:Select Interpreter


**설치**
```python
## 가상환경 설치 및 라이브러리 설치 
conda create -n streamlit-app python=3.8
conda activate streamlit-app
pip install streamlit pandas numpy matplotlib seaborn finance-datareader

## git 설치
winget install --id Git.Git -e --source winget

## 샘플 소스 다운로드
git clone https://github.com/kunkin2024ai/streamlit-tutorial.git

cd streamlit-tutorial
streamlit run 00-text.py
```

- 실습파일: https://github.com/teddylee777/streamlit-tutorial
- 도큐먼트: https://docs.streamlit.io/

## YouTube 튜토리얼 영상

- [EP01. Streamlit으로 빠르게 웹앱 생성하기 - 설치, 환경설정, 실습파일](https://www.youtube.com/watch?v=Gr5Vuo7TCaE)
- [EP02. 텍스트 컴포넌트](https://youtu.be/CiOfNvp-KmA)
- [EP03. 데이터프레임(DataFrame), 테이블 출력](https://youtu.be/C73XAQJFa1E)
- [EP04. 자주 사용하는 위젯(Widgets)들](https://youtu.be/3CWpFR-EkQc)
- [EP05. 로또 생성기 웹사이트 만들기](https://youtu.be/2mER-EvDWzo)
- [EP06. 그래프, 차트 그리기](https://youtu.be/2424N7ITZvo)
- [EP07. 파일 업로드 기능 & 업로드된 파일 처리](https://youtu.be/L3ExMrinu20)
- [EP08. 주식 데이터 조회, 주가 차트 그리기](https://youtu.be/0PA3XsPwPDg)
- [EP09. 사이드바, 탭 추가하기](https://youtu.be/frdggOd5eNQ)
- [EP10. MBTI 대백과사전 웹앱 만들기 (NAVER Clova API 활용)](https://youtu.be/2tT8-peVTLw)
- [EP11. Naver Clova Studio API를 활용한 챗봇 서비스 만들기](https://youtu.be/sLTe2jMGdYU)
- [EP12. 기업의 평균 월급여, 연봉 추정하기 (국민연금 데이터 활용)](https://youtu.be/-CMZKaoX5Og)
- [EP13. 기업의 월급여, 연봉 추정 서비스 제작 & 웹으로 배포 (무료 호스팅)](https://youtu.be/OpeECxk5c-Q)
