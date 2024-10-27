from sqlalchemy.orm import Session
from BackEnd.entity import User
from BackEnd.dto import UserDto


# 유저 목록 가져오기
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User.User).offset(skip).limit(limit).all()

# 유저 생성
def create_user(db: Session, user: UserDto.UserCreate):
    db_user = User.User(
        이름=user.이름,
        아이디=user.아이디,
        비밀번호=user.비밀번호,
        이메일=user.이메일,
        생년월일="2000-01-01",  # 기본 값 사용
        성별_남성여부=True,
        결혼여부=False,
        자녀유무=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user