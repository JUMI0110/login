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



signup - create기능 
login id,pw 입력시 검증 후 같다면 로그인 (key발급) create기능
 -> 발급된 session key를 쿠키에 저장

cookie 일정한작은정보 key=value로 이루어진 정보를 임시로 저장하는 공간
sessionid -create 발급

login ModelForm 이 아닌 Form을 사용
주는 정보와 생성하는 정보가 다름 



로그인 기능 CRUD (R-사용자의 정보불러오기, U-사용자정보 업데이트)
signup User Create
login  session Create
logout session Delete



decorators login_required
로그인을 했는지 확인과 동시에 next인자 넣어줌 (?next=/url)
@login_required 로그인 하지 않으면 함수 동작 X
def detail():



로그인한 계정이 아닌 다른계정의 댓글도 삭제할 수 없게 코드