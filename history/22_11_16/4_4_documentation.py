# https://docs.djangoproject.com/ko/4.1/


# 되게 많은 기능들이 있다..

# 4_4 Documentataion 강의를 보고 느낀점
# 1. 우선 PK를 설정하는 법을 알아야한다.
# 2. user application(pando처럼 wallet pub key 컬럼은 보유 + Google OTP CODE도 보유하는게 맞을 것 같음), wallet application(지갑키쌍 저장), 배송 후 리워드 신청
# 배송 후 리워드 신청, 일반 출금 등 따로 두고 앱에 뿌려주기 위해 totalscan에도 각각 두번 저장 user랑 배송 후 리워드 신청 테이블이랑 연관성이 있게 설계
#  
