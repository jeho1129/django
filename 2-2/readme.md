# DJANGO 실습 2-2

## 요구사항
  1. url을 통해 입력받은 두 수에 대한 사칙연산 결과를 출력
  2. 입력받은 두 수에 대한 형 변환은 path converter를 사용
  3. +의 경우 DTL의 add filter를 사용하여 계산
  4. 나머지 연산의 경우, views.py에서 계산한 값을 template로 전달하여 사용
  5. 두 번째 숫자가 0일 경우, 나머지 연산은 "계산할 수 없습니다"라는 결과를 대신 출력하도록 함.
  6. url mapping을 사용하여 url path에 app의 이름이 포함되도록 설정
  7. 함수, html 파일 이름은 calculator로 작성