"""
author: Yth
location: XMU Xiang'an,Xiamen,Fujian
date and time: 2025/3/20 20:46
version: 2.0 (1.0原版是摘抄了抖音一个Up主的代码)
"""

import requests
import os

################################################
'''请自定义文件夹的名字(视频会放在这个文件夹里面),自主决定是否删除中间文件,爬完是否播放视频,然后请在浏览器开发者模式中获取视频音频链接及其他东西'''
name = "两当摇子"

remove_code = 1 #是否删除中间文件

video_play = 1 #是否在爬到视频之后播放视频

url_video = "https://cn-fjfz-fx-01-03.bilivideo.com/upgcxcode/21/99/26120159921/26120159921-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742487179&gen=playurlv2&os=bcache&oi=0&trid=00008212d703d3644f898bd87763dcc2c923u&mid=3494361958451790&platform=pc&og=cos&upsig=0a447038124f3ed77c5cf36c10304640&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=72803&bvc=vod&nettype=0&orderid=0,3&buvid=9369961F-1D99-E461-31BB-D17C94E3E04010723infoc&build=0&f=u_0_0&agrr=0&bw=202009&np=151371937&logo=80000000"

url_audio = "https://cn-fjfz-fx-01-04.bilivideo.com/upgcxcode/21/99/26120159921/26120159921-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742487179&gen=playurlv2&os=bcache&oi=0&trid=00008212d703d3644f898bd87763dcc2c923u&mid=3494361958451790&platform=pc&og=hw&upsig=3928ce77d3e23e7dc65e86a2c6261a67&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=72804&bvc=vod&nettype=0&orderid=0,3&buvid=9369961F-1D99-E461-31BB-D17C94E3E04010723infoc&build=0&f=u_0_0&agrr=0&bw=13916&np=151371937&logo=80000000"

wz = {"referer":"https://www.bilibili.com/video/BV1XBxSenERY/?spm_id_from=333.1387.homepage.video_card.click&vd_source=6da75ca7a9519bba64a824d502d6425a",
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"}

###############################################

#一些文件地址的命名,此处及以下的代码请勿修改
video_path = f"{name}/Video.mp4"
audio_path = f"{name}/Audio.mp3"
final_video_path = f"{name}/{name}.mp4"
current_path = os.getcwd()
final_video_absolute_path = f"{current_path}\{name}"

if not os.path.isdir(name):
     os.mkdir(name)

if not os.path.isfile(video_path):
     res = requests.get(url_video, headers = wz)
     open(video_path,"wb").write(res.content)
     print(res.status_code)

if not os.path.isfile(audio_path):
     res = requests.get(url_audio, headers = wz)
     open(audio_path,"wb").write(res.content)
     print(res.status_code)

if not os.path.isfile(final_video_path):
     return_code = os.system(f"ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 {final_video_path}")
     print(f"返回代码为:{return_code}")
     print(f"视频已经爬下来了,快去文件夹 '{final_video_absolute_path}' 里面看看吧,视频名字叫做 {name}.mp4 ")
     
if remove_code:
     os.remove(video_path)
     os.remove(audio_path)

if video_play:
     os.system(f"ffplay {final_video_path}")

print("感谢使用,快来投喂作者!!!!!")

