# FastAPI Best Practice

## 아키텍처 설계 컨셉

### 모든 것이 이벤트 핸들러다

아래의 두 작업을 모두 이벤트 핸들러가 처리한다.

- 서비스 계층 함수에 의해 처리되는 API
- 내부 이벤트와 그 이벤트에 대한 핸들러

### 각 레어어간의 종속성을 위배하지 않는다.

![Onion-architecture-image](https://user-images.githubusercontent.com/58972963/134830910-84b80f3a-b882-412a-b554-627a892acf11.png)

- 위의 그림의 **화살표 방향으로만** 종속성을 가질 수 있다.
- 도메인 모델에는 **그 어떤 종속성도 있어선 안된다**.

### 트랜잭션은 작업 단위(Unit of Work)패턴으로 관리한다.

- 파이썬의 [컨텍스트 매니저](https://ddanggle.gitbooks.io/interpy-kr/content/ch24-context-manager.html) 를 사용해 작업 단위를 구현했다.
- 작업 도중에 예외가 발생한다면 `__exit__`메서드에서 **rollback** 시켜 트랜잭션을 유지할 수 있다.
```python
with uow:
    user = uow.users.get_by_username(input_dto.username)
    if not user:
        raise NotFoundUserException()  # 예외가 발생할 경우 __exit__() 메서드를 실행한다.
    user.change_password(password)  # user의 변경사항
    uow.commit()  # 원할 때 변경 사항을 DB에 반영한다.


# uow 가 무사히 종료되어도 __exit__() 가 실행된다.

# UnitOfWork class의 __exit__() 메서드
def __exit__(self):
    self.session.rollback()
    self.session.close()
```

### Application Service 는 비즈니스 로직을 담지 않는다.

- Application Service는 단지 외부의 요청을 **도메인 모델**과 **도메인 서비스**에 위임하는 역할을 한다.
- 비즈니스 로직은 **도메인 모델**과 **도메인 서비스**에 담는다.