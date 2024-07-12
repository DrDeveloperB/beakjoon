"""
도커 사용시 필수 파일
Dockerfile
requirements.txt

도커 명령어

도커 이미지 빌드
이미지명 뒤에 한 칸 띄우고 마침표 필수
docker build -t 이미지명 .

컨테이너 생성 후 실행
docker run 명령어는 Docker에서 컨테이너를 생성하고 실행하는 명령어입니다.
-d : 컨테이너를 백그라운드에서 실행합니다 (detached 모드).
--name : 컨테이너명 지정 (지정하지 않으면 랜덤 이름으로 생성)
-p : 호스트의 포트와 컨테이너의 포트를 매핑합니다. 이를 통해 호스트의 포트로 접속하면 컨테이너의 포트에 연결됩니다.
-v : 호스트의 디렉토리와 컨테이너의 디렉토리를 볼륨 마운트합니다.
    이를 통해 호스트의 디렉토리와 컨테이너의 디렉토리가 연결되어 데이터를 주고받을 수 있습니다.
docker run -d --name 컨테이너명 -p 호스트포트:컨테이너포트 -v "호스트디렉토리:컨테이너디렉토리" 실행할이미지명
예시
Linux/macOS
docker run -d --name py-app-c -p 8060:8060 -v "$(pwd)/data:/data" py-app
Windows (PowerShell)
docker run -d --name py-app-c -p 8060:8060 -v "${PWD}/data:/data" py-app

컨테이너 중지
docker stop 컨테이너명

컨테이너 삭제
docker rm 컨테이너명
"""
import matplotlib.pyplot as plt
import numpy as np
import io
import os
from flask import Flask, send_file, Response, request, render_template_string
import logging
import base64
from datetime import datetime, timezone
import pytz

app = Flask(__name__)

# 로그 설정
logging.basicConfig(level=logging.DEBUG)

def draw_sun(ax):
    # 태양 그리기
    sun = plt.Circle((0.8, 0.8), 0.1, color='yellow', ec='orange', lw=3)
    ax.add_patch(sun)

def draw_cloud(ax, center_x, center_y):
    # 구름 그리기
    cloud_color = 'lightgrey'
    cloud = plt.Circle((center_x, center_y), 0.05, color=cloud_color, ec='grey', lw=2)
    cloud2 = plt.Circle((center_x + 0.07, center_y + 0.03), 0.05, color=cloud_color, ec='grey', lw=2)
    cloud3 = plt.Circle((center_x + 0.14, center_y), 0.05, color=cloud_color, ec='grey', lw=2)
    ax.add_patch(cloud)
    ax.add_patch(cloud2)
    ax.add_patch(cloud3)

def draw_bird(ax, start_x, start_y):
    # 기러기 그리기
    bird_body = np.array([[start_x, start_y], [start_x + 0.05, start_y + 0.02], [start_x + 0.1, start_y]])
    ax.plot(bird_body[:, 0], bird_body[:, 1], color='black', lw=2)

def draw_image(mode, *args):
    fig, ax = plt.subplots()

    # 하늘 배경
    ax.set_facecolor('skyblue')

    # 태양 그리기
    draw_sun(ax)

    # 구름 그리기
    draw_cloud(ax, 0.3, 0.8)
    draw_cloud(ax, 0.5, 0.7)

    # 기러기 떼 그리기
    for i in range(5):
        draw_bird(ax, 0.2 + i * 0.1, 0.6 - i * 0.05)
        draw_bird(ax, 0.3 + i * 0.1, 0.65 - i * 0.05)

    # 축 및 눈금 제거
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    if mode == 'memory':
        # 이미지를 메모리에 저장
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close(fig)
        img.seek(0)
        # return img
        # io.BytesIO 객체에서 getvalue() 메서드가 반환하는 값은 bytes 타입입니다.
        img_data = img.getvalue()
        return img_data
    else:
        path = args[0]
        # data 폴더 확인 및 생성
        if not os.path.exists(path):
            os.makedirs(path)

        # 대한민국의 시간대
        kr_timezone = pytz.timezone('Asia/Seoul')
        # 현재 시간을 대한민국 시간대로 가져오기
        now = datetime.now(kr_timezone)
        current_time = now.strftime('%Y%m%d_%H%M%S')
        # 현재 UTC 시간을 기반으로 파일명 생성
        # current_time = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        # current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'image_{current_time}.png'  # 예시: image_20240101_120000.jpg
        # 그림 저장
        file_path = os.path.join(path, filename)
        # 파일이 존재하는 경우 덮어씀
        plt.savefig(file_path)
        plt.close(fig)
        # return file_path
        # 이미지 파일을 바이너리 모드로 읽기
        with open(file_path, 'rb') as image_file:
            # read() 반환값 : bytes 타입
            img_data = image_file.read()
        return img_data

@app.route('/')
def show_image():
    # memory, save
    # get(파라미터명, 기본값)
    mode = request.args.get('mode', 'memory')
    # mode = 'save'
    if mode not in ['memory', 'save']:
        return Response("Invalid mode. Available modes: 'memory', 'save'", status=400)

    try:
        path = '/data'
        # img = draw_image(mode, path)
        img_data = draw_image(mode, path)
        if not img_data:
            return Response(f"이미지 데이터를 읽을 수 없습니다. (mode={mode})", status=400)

        # Prepare HTML template to render image and mode
        html_content = '''
        <h1>Image with Mode: {{ mode }}</h1>
        <img src="data:image/png;base64,{{ img }}" />
        '''

        # Encode image to base64 for embedding in HTML
        # 이미지 파일 바이너리 데이터를 읽어서 base64로 인코딩
        img_base64 = base64.b64encode(img_data).decode('utf-8')
        # img_base64 = img.getvalue().encode('base64').strip()

        # Render HTML with mode and embedded image
        # HTML 템플릿을 생성하고, 이미지와 mode를 함께 렌더링
        rendered_html = render_template_string(html_content, mode=mode, img=img_base64)

        return rendered_html
        # return send_file(img, mimetype='image/png')

    except Exception as e:
        app.logger.error(f"Error generating image: {e}")
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8060, debug=True)
