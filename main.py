from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("키움 클래스 실행")

        #이벤트 루프
        self.event_loop = QEventLoop()

        #실행 함수
        self.get_ocx_instance()
        self.connect_event_slots()
        self.comm_connect()

    def get_ocx_instance(self):
        """ 키움 API 불러오기 """
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')


    def connect_event_slots(self):
        """ 이벤트 슬롯 연결 """
        self.OnEventConnect.connect(self.login_slot)

    def comm_connect(self):
        """ 로그인 요청 """
        self.CommConnect()

        self.event_loop.exec_()

    def login_slot(self,error_code):
        """ 로그인 결과 """

        print(error_code)

        self.event_loop.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    app.exec_()
