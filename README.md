# Gomgomi
Gomgomi Backend Server

## 개발 의의
- Google STT, Kakao TTS API를 활용해 서비스에 적용했습니다.
- Transformer Architecture 기반의 언어모델을 활용해 Online Serving Server를 구축, 충분한 시간 내에 실시간 처리를 할 수 있도록 기능을 개발했습니다.
- Airflow를 활용해 사용자의 대화 내용을 기반으로 한 감정 분석 결과를 Batch Serving해서 DB에 반영할 수 있도록 개발했습니다.
- GCP(Google Cloud Platform)를 활용해 다수의 Model Inference 서버를 구축했습니다.

## 앱 구조
<img width="783" alt="ㅇㅇㅇㅇㅇ" src="https://user-images.githubusercontent.com/74298527/173318965-0e97c343-7c6d-4179-887e-4ceff4d08ef5.png">
