# _*_ coding:utf-8 _*_
import requests
url = 'https://api.weixin.qq.com/cgi-bin/message/mass/send?access_token=' \
      '10_sY5qC1yapr-BuXA_rhhpfFDxPpDi0du31g6GtK6ctg3T5-o0s21AYE1aLL40y2cFFxkLD' \
      'H9qlgQG8Lps3iUnVVmGrTB3xPiVW23mS_6youA6SD-3AGMzFCG5RA7G_5-UevhgTzLaaFOp1aHBYGHcABAHPQ'

data = {
   "touser":[
    "o-u061RxikdR97aGWvjQldVwzC7o","o-u061fqa-GcBFKZhyhhez7i3wZA"
   ],
    "msgtype": "text",
    "text": { "content": "hello from boxer."}
}
