
# Django_tut2_cafe

카페 키오스크 시스템을 구현한 Django 프로젝트입니다. View, Template, Model 패턴을 학습하기 위한 프로젝트입니다.

## 프로젝트 구조

```
django_tut2_cafe/
├── manager/
│   ├── models.py      # 메뉴와 옵션 모델
│   ├── views.py       # 뷰 로직
│   └── templates/     # 템플릿 파일들
├── config/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## 주요 기능

- 메뉴 관리 (추가/조회)
- 옵션 관리 (추가/조회)
- 데이터베이스 모델링
- POST/GET 요청 처리

## 설치 및 실행

1. 저장소 클론
```bash
git clone https://github.com/2zm00/django_tut2_cafe.git
cd django_tut2_cafe
```

2. Conda 가상환경 생성 및 활성화
```bash
conda create -n dj2 python=3.11 
conda activate dj2
```

3. Django 설치
```bash
pip install django
```

4. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 서버 실행
```bash
python manage.py runserver
```

## 모델 구조

```python
# models.py
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Option(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
```

## 개발 과정

1. 초기 설정
   - Github 저장소 생성
   - Django 프로젝트 및 앱 생성

2. 기능 구현
   - 페이지 라우팅 설정
   - 뷰 로직 구현
   - 모델 설계 및 구현
   - 템플릿 제작

3. 연결 구성
   - View-Model-Template 연결
   - 데이터 모델링
   - CRUD 기능 구현

## 학습 내용

- Django MVT 패턴
- 데이터베이스 모델링
- HTTP 메소드 (GET/POST) 처리
- 템플릿 시스템 활용

## 라이센스

This project is licensed under the MIT License
