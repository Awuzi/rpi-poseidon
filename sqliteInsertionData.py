from sense_emu import SenseHat
import time
import sqlite3
import logging.handlers
import paho.mqtt.client as mqtt
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


def get_pression():
    # collection des donnees de la carte sensehat
    sense = SenseHat()
    pression = sense.get_pressure()
    return pression


def get_humidity():
    sense = SenseHat()
    humidity = sense.get_humidity()
    return humidity



def get_temp():
    sense = SenseHat()
    temp = sense.get_temperature()
    return temp
 

def on_publish(client,userdata,result):
    print("data publish")
    pass

def mqtt_sending_data(pression, humidity, temperature):
    topic="poseidon"
    payload=""+str(round(pression, 1))+"/"+str(round(humidity, 1))+"/"+str(round(temperature, 1))+""
    client = mqtt.Client()
    client.on_publish = on_publish
    client.connect("192.168.1.42", 1883)
    ret = client.publish(topic, payload)

def sendMail(emailSubject, emailBody):
    error_mail_subject = emailSubject
    error_mail_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587),
                                                      fromaddr="testmail.sio22@gmail.com",
                                                      toaddrs="algerinooh@gmail.com",
                                                      subject=error_mail_subject,
                                                      credentials=('testmail.sio22@gmail.com', 'testmail'),
                                                      secure=())
    error_mail_handler.setLevel(logging.ERROR)
    logger = logging.getLogger()
    logger.addHandler(error_mail_handler)
    logger.exception(Exception(emailBody))


def main():
    emailSubjectTemperature = "Temperature is wrong"
    emailSubjectPressure = "Air pressure is too high!"
    emailSubjectHumidity = "Humidity is too high!"
    db = "/home/pi/Poseidon/Poseidon.db"

    while True:
        conn = create_connection(db)
        pression = get_pression()
        humidity = get_humidity()
        temperature = get_temp()

        mqtt_sending_data(pression, humidity, temperature)

        emailBodyGeneral = "Temperature is: " + str(round(temperature, 1)) + "°C (Optimum temperature between 15 and 25°C), Pressure is: " + str(
            round(pression, 1)) + "mbar (Optimum pressure is 1030mb), Humidity is: " + str(round(humidity, 1)) + "% (Best between 30-60%)."
        # Sending data to database
        c = conn.cursor()
        c.execute("INSERT INTO data_poseidon(Pression, Humidity, Temperature) VALUES (" + str(round(pression, 1)) + ", " + str(round(humidity, 1)) + ", " + str(round(temperature, 1)) + ")")
        conn.commit()
        conn.close()
        print("sent to database")

        # send email if temp is too high
        if temperature > 25 or temperature < 15:
            sendMail(emailSubjectTemperature, emailBodyGeneral)
            print("email sent")
        if pression < 1030:
            sendMail(emailSubjectPressure, emailBodyGeneral)
            print("email sent")
        if humidity < 30 or humidity > 60:
            sendMail(emailSubjectHumidity, emailBodyGeneral)
            print("email sent")

        time.sleep(20)


if __name__ == '__main__':
    main()
