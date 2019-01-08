# 大众点评商家评论爬虫
  
### Requirements
python3.5+  
  
lxml  
requests
  
### Process
1. 请求商家评论页，获取请求成功后的结果，解析出字体样式所对应css的url
2. 请求css的url，获取请求成功后的结果，获取字体背景svg所对应的url，并解析出class样式对应的偏移坐标
3. 请求svg的url，获取请求成功后的结果，解析出偏移坐标所对应的字体，并与class的偏移坐标做映射
4. 将原html的字体span标签替换
  
### Demo
![image](https://github.com/longxiaofei/markdown_img/blob/master/dianping/1.png?raw=true)  
![image](https://github.com/longxiaofei/markdown_img/blob/master/dianping/2.jpeg?raw=true)
  
### Use
```
from dianping import DianpingComment

COOKIES = ''

class Customer(DianpingComment):
    
    def _data_pipeline(self, data):
        print(data)

if __name__ == "__main__":
    dianping = Customer('6232395', cookies=COOKIES)
    dianping.run()
```
  
### Tip
1. 一些异常没有特殊处理，只是打了断言，请自行改进
2. 如果程序开始时报错，可以用浏览器打开商家详情页，手动跳过验证
3. 默认爬取速度为7秒1页
4. 登录后将cookie存入COOKIES变量
  
### Todo
1. 
  
### Update
1. 2019/01/07 上传代码
