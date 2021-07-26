# 3rd-project-apt-payment

# 아파트 현관 출입 시스템의 보고서 API

## Description

Django Rest Framework를 사용한 아파트 관리비 조회 api입니다. 관리자(admin)는 모든 세대의 관리비를 조회, 추가, 수정, 삭제 가능하며, 세대(public)는 해당 세대의 내역만 조회 가능합니다.

### Service Url

1. http://127.0.0.1/api/admin/
2. http://127.0.0.1/api/admin/<int:pk>
3. http://127.0.0.1/api/public/

### Default Account

1. admin / 0000
2. 0101 / 0000
3. 0102 / 0000
4. 0103 / 0000
5. 0104 / 0000
6. 0105 / 0000

## Environment

Docker-compose로 구성하여 Docker-compose 환경에서 `docker-compose up -d` 명령어를 통해 사용.

## 화면

![스크린샷 2021-07-25 오후 5 23 53](https://user-images.githubusercontent.com/77102285/126892763-712bc2cb-842e-4991-bd17-eeb98b5e6e0b.png)
