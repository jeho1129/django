# DJANGO 실습 5-1

## 요구사항
  1. 맛집 정보를 관리하는 서비스를 제공하는 프로젝트 생성
  2. Restaurant Model을 정의
  3. '/restaurants/' 경로로 요청 시 전체 식당 목록을 확인할 수 있어야 한다.(식당의 이름과 주소를 보여준다, 새로운 식당을 생성할 수 있는 링크를 작성)
  4. '/restaurants/new/' 경로로 요청 시 식당 생성을 위한 form을 보여준다.(데이터를 POST Methods로 전송, 작성한 데이터는 '/restaurants/create/' 경로로 전송)
  5. '/restaurants/create/' 경로에서는 데이터를 저장하고 '/restaurants/' 경로로 redirect한다.

# DJANGO 실습 5-2

## 요구사항
  1. '/restaurants/{restaurant_pk}/' 경로로 요청 시 식당 상세 정보를 확인할 수 있어야 한다.(식당이 가진 모든 field를 보여준다, 식당 정보 수정 페이지로 이동할 수 있는 링크를 제공, 식당 정보를 삭제할 수 있는 버튼을 제공)
  2. '/restaurants/{restaurant_pk}/edit/' 경로로 요청 시 식당 정보 수정을 위한 form을 보여준다.(데이터를 POST Methods로 전송, 기존 식당 정보를 포함하고 있어야 한다.)
  3. '/restaurants/{restaurant_pk}/update/' 경로에서는 데이터를 수정하고 '/restaurants/' 경로로 redirect한다.