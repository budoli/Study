# DevOps 30일 로드맵

## 1주차: DevOps 기본기와 Linux

| Day | 주제 | 학습 목표 | 실습 |
| --- | --- | --- | --- |
| 01 | DevOps 개념 | DevOps, CI, CD, 배포, 운영의 관계 이해 | DevOps 용어 10개 정리 |
| 02 | Git 워크플로우 | commit, branch, merge, PR 흐름 이해 | 새 브랜치 생성 후 커밋하기 |
| 03 | Linux 기본 명령어 | 파일, 디렉터리, 프로세스 명령어 익히기 | `ls`, `cd`, `cat`, `ps`, `top` 실행 |
| 04 | 권한과 사용자 | chmod, chown, sudo 이해 | 실행 권한이 있는 스크립트 만들기 |
| 05 | 네트워크 기초 | IP, port, DNS, HTTP 이해 | `curl`, `ping`, `netstat` 또는 `ss` 사용 |
| 06 | Shell Script | 반복 작업 자동화 기초 | 백업용 `.sh` 스크립트 작성 |
| 07 | 1주차 복습 | Linux와 Git 흐름 정리 | 1주차 문제 풀이 |

## 2주차: CI/CD와 Docker

| Day | 주제 | 학습 목표 | 실습 |
| --- | --- | --- | --- |
| 08 | CI/CD 개념 | CI와 CD의 차이 이해 | 배포 파이프라인 그림 그리기 |
| 09 | GitHub Actions | workflow, job, step 이해 | push 시 테스트 실행 workflow 작성 |
| 10 | 빌드 자동화 | 테스트와 빌드 분리 | Java/Gradle 또는 Node 프로젝트 빌드 자동화 |
| 11 | 환경변수와 Secret | 민감 정보 관리 방식 이해 | GitHub Secrets 개념 정리 |
| 12 | Docker 기본 | image, container, registry 이해 | `hello-world` 컨테이너 실행 |
| 13 | Dockerfile | 앱을 이미지로 패키징 | 간단한 Dockerfile 작성 |
| 14 | Docker Compose | 여러 컨테이너 실행 | 앱 + DB compose 구성 읽기 |

## 3주차: 서버 배포와 운영

| Day | 주제 | 학습 목표 | 실습 |
| --- | --- | --- | --- |
| 15 | 클라우드 기초 | VM, region, security group 이해 | AWS EC2 기준 배포 구조 정리 |
| 16 | SSH 접속 | 서버 접속과 키 기반 인증 이해 | SSH 접속 명령어 정리 |
| 17 | 서버에 앱 실행 | 서버에서 프로세스 실행 | 백엔드 앱을 서버 실행 기준으로 정리 |
| 18 | Nginx | 리버스 프록시 개념 이해 | Nginx 설정 예시 작성 |
| 19 | HTTPS | TLS 인증서와 Let's Encrypt 이해 | HTTPS 적용 흐름 정리 |
| 20 | 배포 스크립트 | 반복 배포 자동화 | pull, build, restart 스크립트 설계 |
| 21 | 3주차 복습 | 서버 운영 흐름 정리 | 장애 상황별 대응 노트 작성 |

## 4주차: Kubernetes, 모니터링, 최종 프로젝트

| Day | 주제 | 학습 목표 | 실습 |
| --- | --- | --- | --- |
| 22 | Kubernetes 개념 | Pod, Node, Cluster 이해 | Kubernetes 구성요소 정리 |
| 23 | Deployment | 원하는 개수만큼 앱 실행 | Deployment YAML 작성 |
| 24 | Service | Pod 접근 방식 이해 | Service YAML 작성 |
| 25 | ConfigMap/Secret | 설정과 비밀값 분리 | 환경변수 주입 예시 작성 |
| 26 | Ingress | 외부 트래픽 라우팅 이해 | Ingress 구조 정리 |
| 27 | 로그 | 로그 확인과 원인 분석 | 앱 로그 확인 명령어 정리 |
| 28 | 모니터링 | metric, alert, dashboard 이해 | Prometheus/Grafana 개념 정리 |
| 29 | 최종 프로젝트 1 | CI/CD + Docker 배포 구성 | 전체 배포 흐름 작성 |
| 30 | 최종 프로젝트 2 | 결과물 정리와 회고 | README, 아키텍처, 문제 풀이 정리 |

## 최종 프로젝트 기준

다음 구조를 목표로 한다.

```text
devops-project
├─ app
├─ Dockerfile
├─ docker-compose.yml
├─ .github/workflows/ci.yml
├─ deploy.sh
├─ k8s
│  ├─ deployment.yaml
│  ├─ service.yaml
│  └─ ingress.yaml
└─ README.md
```

