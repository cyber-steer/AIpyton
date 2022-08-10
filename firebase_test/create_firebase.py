import pyrebase
import datetime

firebaseConfig = {"apiKey": "AIzaSyBETK45cbP1g2ZYC03ras5UYys5fXAqV_4",
  "authDomain": "fir-course-edb8c.firebaseapp.com",
  # "databaseURL": "https://fir-course-edb8c.firebaseio.com",
  "databaseURL": "https://fir-course-edb8c-default-rtdb.firebaseio.com/",
  "projectId": "fir-course-edb8c",
  "storageBucket": "fir-course-edb8c.appspot.com",
  "messagingSenderId": "760960563313",
  "appId": "1:760960563313:web:eb3b145202888f8a3c83d0",
  "measurementId": "G-336MJ5MK72"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()


sample =[
  {"웹 프로그래밍":{
    "week1":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week2":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week3":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      }
    }
  }},
  {"자바 앱 개발":{
    "week1":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week2":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week3":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      }
    }
  }},
  {"클라우드 컴퓨팅 실습":{
    "week1":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week2":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
    },
    "week3":{
      "class1":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      },
      "class2":{
        "김건우":"05:30:19",
        "설재혁":"06:30:19",
        "손옥무":"07:30:19",
        "장성익":"08:30:19",
      }
    }
  }},
]
timetable = [
  {"0":{
    "class2":{"subject":"웹 프로그래밍"},
    "class3":{"subject":"웹 프로그래밍"},
    "class6":{"subject":"클라우드 컴퓨팅 실습"},
    "class7":{"subject":"클라우드 컴퓨팅 실습"},
    "class8":{"subject":"라이프가이드"}
  }},
  {"1":{
    "class2":{"subject":"웹 프로그래밍"},
    "class3":{"subject":"웹 프로그래밍"},
    "class6":{"subject":"모바일 앱 개발"},
    "class7":{"subject":"모바일 앱 개발"}
  }},
  {"2":{
    "class2": {"subject": "최신 IT기술 특강"},
    "class3": {"subject": "최신 IT기술 특강"},
    "class6": {"subject": "모바일 앱 개발"},
    "class7": {"subject": "모바일 앱 개발"}
  }},
  {"3":{
    "class2": {"subject": "시스템 분석 및 설계"},
    "class3": {"subject": "시스템 분석 및 설계"},
    "class4": {"subject": "시스템 분석 및 설계"},
    "class6": {"subject": "클라우드 컴퓨팅 실습"},
    "class7": {"subject": "클라우드 컴퓨팅 실습"}
  }},
  {"4":{
    "class2": {"subject": "자료구조"},
    "class3": {"subject": "자료구조"},
    "class4": {"subject": "자료구조"}
  }}
]
schedule = [
  {"class1":9},
  {"class2":10},
  {"class3":11},
  {"class4":12},
  {"class5":13},
  {"class6":14},
  {"class7":15},
  {"class8":16}
]

# for subject in sample:
#   for week in subject.items():
#     for classes in week[1].items():
#       for name in classes[1].items():
#         for time in name[1].items():
#           db.child("attendance").child(week[0]).child(classes[0]).child(name[0]).child(time[0]).set(time[1])
          # print(week[0], classes[0], name[0], time[0], time[1])

# for week in timetable:
#   for classes in week.items():
#     for subject in classes[1].items():
#       for unit in subject[1].items():
#         db.child("timetable").child(classes[0]).child(subject[0]).child(unit[0]).set(unit[1])
        # print(classes[0], subject[0], unit[0],unit[1])

# for classes in schedule:
#   for time in classes.items():
#     db.child("schedule").child(time[0]).set(time[1])

now = datetime.datetime.now()
print(now)