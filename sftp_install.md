# 파일 전송 통신 규약
- FTP(File Transfer Protocol): 파일을 전송하는 통신 규약. 기본 포트 21

- SFTP(Secure File Transfer Protocol): FTP에 보안기능이 추가. Ssh(Secure SHell)와 같은 방식을 이용하여 안전하게 암호화된 구간에서 FTP기능 사용. 

# sftp 설정방법
## 1. 설치된 패키지 업그레이드 


![image](https://user-images.githubusercontent.com/44438752/62205910-84d81f00-b3cb-11e9-8ee9-22c619ae7c41.png)
<br/><br/>

## 2. 설치된 패키지 리스트 확인
- 여기서는 openssh-server가 설치되지 않았음을 확인할 수 있음


![image](https://user-images.githubusercontent.com/44438752/62205588-be5c5a80-b3ca-11e9-96ec-f31045fd04d5.png)
<br/>
deb 파일 설치 : dpkg -i <file name.deb> 
<br/>
패키지 제거 : dpkg -P <package nae>
<br/>
설치된 패키지 리스트: dpkg -l
<br/>
설치된 패키지에 포함된 파일 보기 dpkg -L <package name>
<br/>
deb 파일 포함된 파일들 보기 : dpkg -c <file name.deb>
<br/>
deb 파일의 정보보기 : dpkg -l <file name.deb>
<br/>
파일의 패키지명 알아내기: dpkg -S <file name>
<br/>
grep openssh -> openssh라는 문자 검색

<br/><br/>

## 3. ssh 서버 설치


![image](https://user-images.githubusercontent.com/44438752/62206089-fadc8600-b3cb-11e9-94dd-596fb9682817.png)

<br/><br/>

## 4. ssh 서버 시작


![image](https://user-images.githubusercontent.com/44438752/62206129-10ea4680-b3cc-11e9-8d4e-2dd4ee0af354.png)

<br/><br/>
## 5. 네트워크 상태 알아보기(어떤 포트가 열려있고 어떤 이름으로 어떻게 사용되는지)

![image](https://user-images.githubusercontent.com/44438752/62206176-2a8b8e00-b3cc-11e9-9f19-1688a5cd10e6.png)

-a : 모든 연결 및 수신 대기 포트를 표시한다.
-c : 현재 실행 명령을 매 초마다 실행한다.
-l : LISTEN 하고 있는 포트를 보여준다.
-t : TCP로 연결된 포트를 보여준다.
-u : UDP로 연결된 포트를 보여준다.
-n : 주소나 포트 형식을 숫자로 표현한다.
-p : 해당 프로세스를 사용하고 있는 프로그램 이름을 보여준다.
-r : 라우팅 테이블을 보여준다.

## 6. 모든 서비스 목록 출력. +는 실행중, -는 실행중이 아닌 서비스
- ssh 실행되고 있음을 확인할 수 있음.


![image](https://user-images.githubusercontent.com/44438752/62206286-6b83a280-b3cc-11e9-83d4-4f7a71892090.png)

<br/><br/>

## 7. ssh 서버 설치됬음을 확인


![image](https://user-images.githubusercontent.com/44438752/62206313-7b9b8200-b3cc-11e9-93d9-ceb0baaf16a1.png)

## 8. ssh 포트번호 수정
