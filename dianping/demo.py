from dianping import DianpingComment

COOKIES = ''

class Customer(DianpingComment):
    
    def _data_pipeline(self, data):
        print(data)


if __name__ == "__main__":
    dianping = Customer('3262456', cookies=COOKIES)
    dianping.run()

