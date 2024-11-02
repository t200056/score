import streamlit as st

#  기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 만든 모델로 테스트 데이터에 대해 예측하기
st.title('점수 예측')
st.subheader(' ______________________ ')
st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 총 데이터 건 수: 30건')
st.write(' - 훈련    데이터 : 21건')
st.write(' - 테스트 데이터 : 9건')
col1, col2, col3 = st.columns(3)

with col1:
      st.subheader('2. 데이터 시각화')
      st.image('시각화2.png' )   # 이미지 불러오기
with col2:
      st.subheader('3. 데이터 시각화')
      st.image('시각화3.png' )   # 이미지 불러오기
with col3:
      st.subheader('4. 상관관계')
      st.image('시각화4.png')   # 이미지 불러오기

st.subheader('3. 예측하기')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

# 사용자 입력
a = st.number_input(' 수강과목수입력 ', value=0)
b = st.number_input(' 공부시간 입력 ', value=0)
c = st.selectbox('공지확인', [0,1])

# 예측 버튼 만들기
if st.button('예측'):
        input_data = [[a,b,c]]
        p = model.predict(input_data)
        st.write('점수는',p)
