# state.py
import reflex as rx
import asyncio
import time
import traceback
import cv2
import websockets
from hume import HumeClientException, HumeStreamClient
from hume.models.config import FaceConfig
from twilio.rest import Client
import redis
import creds

class FormState(rx.State):
    name: str = ""
    phone: str = ""

    run = True

    threshold = [0.4, 0.8]

    #twilio Config
    account_sid = creds.twilio_sid
    auth_token = creds.twilio_token




    # Configurations
    HUME_API_KEY = creds.hume_key
    HUME_FACE_FPS = 1 / 3  # 3 FPS

    TEMP_FILE = '../temp.jpg'
    TEMP_WAV_FILE = 'temp.wav'

    def toggleRun(self):
        self.run = not self.run

    def init_session(self):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            from_=creds.twilio_phone,
            body= f'Nurture here, {self.name} has just started working!',
            to=self.phone
    )
        # asyncio.run(Hume.webcam_loop())
        return FormState.webcam_loop

    @rx.background
    async def webcam_loop(self):
        r = redis.Redis(
                host=creds.redis_host,
                port=creds.redis_port,
                password=creds.redis_password)
        cam = cv2.VideoCapture(0)
        client = Client(self.account_sid, self.auth_token)
        while True:
            try:
                if (not self.run):
                    break
                hClient = HumeStreamClient(self.HUME_API_KEY)
                config = FaceConfig(identify_faces=True)
                async with hClient.connect([config]) as socket:
                    print("Starting Session, Welcome to Nurture!")
                    while True:
                        if (not self.run):
                            break
                        _, frame = cam.read()
                        cv2.imwrite(self.TEMP_FILE, frame)
                        result = await socket.send_file(self.TEMP_FILE)
                        #print(result)  # Storing result
                        # Serializing json
                        #json_object = json.dumps(result, indent=4)
                        # Writing to sample.json
                        #with open("sample.json", "w") as outfile:
                         #   outfile.write(json_object)
                        for prediction in result['face']['predictions']:
                            for emotion in prediction['emotions']:
                                if emotion['score'] > self.threshold[1]:
                                    r.lpush(emotion['name'], emotion['score'])
                                    print("Heightened sense of ", emotion['name'], " detected, sending text")
                                    #text via twilio
                                    msg = f"{self.name} is feeling a strong sense of {emotion['name']} - Nurture"
                                    client.messages.create(
                                        from_=creds.twilio_phone,
                                        body= msg,
                                        to=self.phone
                                    )
                                    break #avoids multiple texts. (ex; joy and happyness together)
                        for prediction in result['face']['predictions']:
                            for emotion in prediction['emotions']:
                                if emotion['score'] > self.threshold[0] and emotion['score'] < self.threshold[1]:
                                    print("Slight ", emotion['name'], " detected")
                                    r.lpush(emotion['name'], emotion['score'])
                        await asyncio.sleep(1 / 3)
            except websockets.exceptions.ConnectionClosedError:
                print("Internet Connection Lost. Reconnecting.....")
                time.sleep(1)
            except HumeClientException:
                print(traceback.format_exc())
                break
            except Exception:
                print(traceback.format_exc())