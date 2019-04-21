# TianTcl - Whisper game - generator

import random

_subject    = [None,"นายท่าน","คุณพี่","คุณน้อง","ออเจ้า","เอ็ง","พวกเอ็ง","หล่อน","อ้าย","บ่าว"]
ext_sub     = [None,"ห้องน้ำ","ที่นั่งสมาธิ","ตรงท่าน้ำ","ในลานวัด","ร่องสวน","บนเรือน"]
_verb       = [None,"กำลังวิ่ง","เดิน","คุยกัน","นอนอยู่","หมอบ","คลาน","คุกเข่า"]
ext_verb    = [None,"อย่างโวยวาย","ช้าๆ","เสียงดังมาก","กรุยกราย","วูบวาบ","เหงาหงอย"]
_object     = [None,"บนดวงจันทร์","เรื่อง กรงกรรม ","บนหลังคา","ใต้ต้นมะเขิอ","บนเรือ","บนเรื่อน"]
ext_obj     = [None,"ที่ข้างๆทางช้างเผือก","ที่มีต้นไม้ใหญ่","ยักษ์ใหญ่","วัดใหญ่","ทะเลทราย","ทุ่งนา","หลังเต่างอย"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
