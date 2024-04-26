# 抢票姬 Bilibili_show_ticket_auto_order 1.8.3

## 由 FriendshipEnder(CN小影) 根据 Just-Prog 的改版进行二次修改咩~, **有问题赶紧去提issue!**

关于版本升级: 如果您以前用过旧版本的 Bilibili_show_ticket_auto_order (由 FriendshipEnder 或者 Just-Prog 或者 fengx1a0 开发), 您可以选择将原来可用的 user_data.json 复制到新版本软件本体的所在目录 (和 抢票主程序.exe 放在一起)

### ps: 改来改去, 小影还是觉得自己fork一只比较好, 毕竟抢票姬也不能一直白嫖 得**作出贡献**mua~

### ~~我们也知道这类软件面临倒卖的威胁，但将软件闭源出售并非好的做法，毕竟黄牛可不在乎那几个钱，~~

## ~~而一般用户多是学生，必定支付不了那么高的费用，并且py代码的加密几乎可以视作没有（即使使用Cython或者PyArmor）~~

### ~~所以对付黄牛的最好办法还是人人都有媲美黄牛手里的工具，做到人人有剑，因此这个仓库会保持开源~~

## 简易使用说明

----

1. 进入项目的Github主页之后, 看到右边的Releases, 选择最新的那个版本号的(右边有Latest的), 点一下它.

2. 加载成功之后, 找到下面的Assets 再点击 ticket_win64_1.8.3.zip 即可下载

3. 下载好之后, 新建一个空白文件夹, 再把刚才那个压缩包里的文件解压到这个文件夹里

4. 运行 登录B站.exe, 根据终端提示登录B站

5. 登录成功之后, 运行 抢票主程序.exe, 直到显示输入购票链接的提示消息

6. 电脑端进入网页: https://show.bilibili.com/platform/home.html, 然后在网页上选择好你要去的展子.

7. 确定你想去的展子之后, 复制链接(&from=pc_ticketlist以前的所有内容), 粘贴到程序提示消息处.

链接范例: https://show.bilibili.com/platform/detail.html?id=84096&from=pc_ticketlist,

只需要复制 https://show.bilibili.com/platform/detail.html?id=84096 并粘贴即可

8. 根据程序提示一步一步操作

9. 直到显示开始抢票之后, 说明配置完成, 开始自动抢票, 静候抢票成功.

10. 弹出验证码窗口时, 需要手动滑动验证码.

## 作者软硬件信息: Edge浏览器版本号: 124.0.2478.51 , Win11版本号: 23H2 22631.3296 , Python版本号: 3.12.3

关于抢票间隔: 打开config.txt文件, 找到 sleep = 项目, 然后把时间设置为你需要的抢票间隔. 单位: 秒.

推荐0.1 我这边是挂了半小时不会封的, 不建议过低, 但是过高是没问题的

## Just-Prog: feat:添加自动生成付款二维码功能咩~

<img width="273" alt="屏幕截图 2023-08-09 182035" src="https://github.com/fengx1a0/Bilibili_show_ticket_auto_order/assets/74698099/f0b2d1ad-928b-498d-9a79-f735e3f01c00">

<img width="277" alt="屏幕截图 2023-08-09 182012" src="https://github.com/fengx1a0/Bilibili_show_ticket_auto_order/assets/74698099/4363ff9a-23a7-4f31-b0ea-0919ed1279d1">

# 原介绍

本项目核心借鉴自https://github.com/Hobr 佬咩~

Bilibili会员购抢票助手, 通过B站接口抢购目标漫展/演出mua~

本脚本仅供学习交流使用, 不得用于商业用途, 如有侵权请联系删除nia~

<img src="images\image-20230708221711220.png" alt="image-20230708221711220" style="zoom:50%;" />

<img src="images/a.png" alt="image-20230708221143842" style="zoom:50%;" />

## 致谢

以下排名不分先后，我也不想搞的攀比起来，因为很多都是学生，原则上我是不收赞助的，大家太热情了：nia~

------------------------------------------------++++

```
晚安乃琳Queen
kankele
倔强
宵宫
yxw
星海云梦
穆桉
mizore
傩祓
CChhdCC
w2768
iiiiimilet
利维坦战斧
路人
Impact
骤雨初歇
明月夜
晓读
Simpson
Goognaloli
闹钟
LhiaS
洛天华
猪猪侠
awasl
房Z
浙江大学第一深情
superset245
ChinoHao
神秘的miku
Red_uncle
czpwpq
Just-Prog
```

------------------------------------------------++++


## 功能截图

除了登录纯api请求

目前已经支持漫展演出等的 无证 / 单证 / 一人一证 的购买

<img src="images/image-20230708014050624.png" alt="image-20230708014050624" style="zoom:50%;" />

<img src="images\image-20230708014124395.png" alt="image-20230708014124395" style="zoom:50%;" />

## 使用

相关内容感谢@123485k的提交

### 执行exe

登录和抢票分开的，先运行登录.exe，登陆后再运行抢票.exe，运行了之后不要急着选，先把验证.exe启动起来

不需要依赖

如果运行失败的请安装依赖[Edgewebdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### 执行脚本

请确保引用的库安装正常。

```shell
pip install -r requirements.txt
```

```shell
python login.py     //登录.exe
python main.py      //抢票
python geetest.py   //极验滑块验证
```

### 新功能：微信公众号推送结果

需要关注pushplus微信公众号，关注后激活，然后点击个人中心-获取token，在config.txt中填入token即可在需要验证或者抢票成功后收到微信公众号通知

## 配置说明

config.txt为配置文件，不指定值为None

- proxies 指定代理 如：127.0.0.1:8080 (IP:PORT 请不要加前缀)
- specificID 多个用户登陆后指定某一个人uid(bilibili) (多用户还没做等后面有必要再写)
- sleep设置每次抢票请求间隔时间
- token设置pushplus的个人token

## API文档

pass

## 问题报告

提issue即可

## 更新

加入token验证，手动拉滑块

加入微信公众号推送消息功能

加入对实体票邮寄地址的支持（需要提前添加）

### 编译打包选项:

```shell
pyinstaller -D main.py --hidden-import plyer.platforms.win.notification --exclude-module PyQt5 --exclude-module numpy
```