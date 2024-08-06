model정의 하지 않고 migrate 하면 django가 가지고 있는 파일로만 표를 만들어줌


상속관계
models.Model -> AbstractBaseUser(pw) -> AbstractUser(id,name) -> User 
기능을 포함하고 있는 AbstractUser 상속받아서 새로운 myUser 생성
AbstractUser -> myUser

settings.py 사용할 모델 정의
AUTH_USER_MODEL = "myapp.MyUser"

현재테이블 초기화(처음에 한 migrate): db.sqlite 파일 삭제


해싱
문자열 -> 무작위의 숫자로 변환
단방향 해시 문자열마다 나오는 값이 같음 약간의 변형을 주면 다른 값을 반환해줌
sha -1: 암호화 해시 함수
django -> sha256 
password 만들 때 django만 알고있는 약간의 문자 첨가하여 암호화
