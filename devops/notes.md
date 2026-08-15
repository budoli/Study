# DevOps 핵심 노트

## 1. DevOps란?

DevOps는 개발과 운영을 분리하지 않고, 소프트웨어를 더 빠르고 안정적으로 전달하기 위한 문화와 기술 방식이다.

핵심은 다음 세 가지다.

- 자동화: 테스트, 빌드, 배포를 사람이 매번 직접 하지 않게 만든다.
- 반복 가능성: 같은 방식으로 언제든 다시 배포할 수 있어야 한다.
- 관측 가능성: 장애가 났을 때 로그, 지표, 알림으로 원인을 찾을 수 있어야 한다.

## 2. CI와 CD

CI는 Continuous Integration, 지속적 통합이다.

개발자가 코드를 push하면 자동으로 테스트와 빌드가 실행된다. 목적은 문제가 있는 코드를 빠르게 발견하는 것이다.

CD는 Continuous Delivery 또는 Continuous Deployment다.

- Continuous Delivery: 언제든 배포 가능한 상태를 자동으로 만든다. 실제 배포는 사람이 승인할 수 있다.
- Continuous Deployment: 테스트를 통과하면 운영 환경까지 자동 배포한다.

## 3. Linux 기본

DevOps에서 Linux는 서버 운영의 기본 환경이다.

자주 쓰는 명령어:

```bash
pwd
ls -al
cd
cat file.txt
tail -f app.log
ps aux
top
df -h
free -m
curl http://localhost:8080
```

권한 확인:

```bash
chmod +x deploy.sh
```

## 4. Git 워크플로우

일반적인 협업 흐름:

```text
main 브랜치
-> feature 브랜치 생성
-> 코드 수정
-> commit
-> push
-> Pull Request
-> CI 테스트
-> merge
-> 배포
```

좋은 커밋 메시지는 무엇을 왜 바꿨는지 알려준다.

## 5. Docker

Docker는 애플리케이션과 실행 환경을 이미지로 묶어 어디서든 비슷하게 실행할 수 있게 해준다.

중요 개념:

- Image: 실행 가능한 패키지
- Container: 이미지가 실행된 상태
- Dockerfile: 이미지를 만드는 설명서
- Registry: 이미지를 저장하는 저장소
- Volume: 컨테이너 밖에 데이터를 저장하는 방법
- Network: 컨테이너 간 통신 방법

기본 명령어:

```bash
docker build -t my-app .
docker run -p 8080:8080 my-app
docker ps
docker logs container_id
docker stop container_id
```

## 6. Docker Compose

Docker Compose는 여러 컨테이너를 하나의 파일로 실행하게 해준다.

예를 들어 백엔드 앱과 데이터베이스를 함께 실행할 때 사용한다.

```bash
docker compose up -d
docker compose logs -f
docker compose down
```

## 7. 서버 배포

서버 배포의 기본 흐름:

```text
서버 준비
-> 런타임 설치
-> 코드 또는 이미지 가져오기
-> 환경변수 설정
-> 앱 실행
-> 포트 확인
-> Nginx 연결
-> 로그 확인
```

운영에서 중요한 질문:

- 앱이 죽으면 다시 살아나는가?
- 로그는 어디에 남는가?
- 비밀값은 코드에 들어가 있지 않은가?
- 배포를 되돌릴 수 있는가?

## 8. Nginx

Nginx는 주로 리버스 프록시로 사용한다.

사용자가 `https://example.com`으로 접속하면 Nginx가 내부 앱인 `localhost:8080`으로 요청을 전달한다.

장점:

- 외부 포트와 내부 앱 포트를 분리한다.
- HTTPS 설정을 담당할 수 있다.
- 여러 서비스로 라우팅할 수 있다.

## 9. Kubernetes

Kubernetes는 컨테이너를 여러 서버에서 안정적으로 실행하고 관리하는 플랫폼이다.

핵심 리소스:

- Pod: 컨테이너가 실행되는 최소 단위
- Deployment: Pod 개수와 배포 전략 관리
- Service: Pod에 안정적인 접근 경로 제공
- ConfigMap: 일반 설정값 관리
- Secret: 민감 정보 관리
- Ingress: 외부 HTTP 요청을 서비스로 라우팅

기본 명령어:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl logs pod_name
kubectl describe pod pod_name
kubectl apply -f deployment.yaml
```

## 10. 로그와 모니터링

로그는 사건의 기록이고, 메트릭은 상태를 숫자로 표현한 것이다.

예시:

- 로그: 에러 메시지, 요청 경로, 예외 stack trace
- 메트릭: CPU 사용량, 메모리 사용량, 요청 수, 응답 시간, 에러율

좋은 운영자는 장애가 났을 때 다음 순서로 본다.

```text
서비스 살아 있는가?
-> 최근 배포가 있었는가?
-> 로그에 에러가 있는가?
-> CPU/메모리/디스크가 부족한가?
-> 외부 의존성 DB/API가 정상인가?
```

## 11. IaC

IaC는 Infrastructure as Code의 약자다.

서버, 네트워크, 데이터베이스 같은 인프라를 코드로 관리한다.

대표 도구:

- Terraform
- Ansible
- CloudFormation

장점:

- 인프라 변경 이력을 Git으로 관리할 수 있다.
- 같은 환경을 반복해서 만들 수 있다.
- 수동 설정 실수를 줄일 수 있다.

