# 概况
一个简单的抽人程序，起因是学校一体机上原来用的太卡了，启动时会导致严重的滞后，再加上它登不上去了，于是便有了这个程序。这个程序足够快，启动时几乎不会造成任何卡顿。  
基于python开发，需要python3.8.10的运行环境。  
python3.8.10下载地址：  
https://www.python.org/downloads/release/python-3810/  
python3.8安装教程：  
https://zhuanlan.zhihu.com/p/390819620  
安装时***一定***要勾选*add python3.8 to path*  
以CC0协议发布  
# 使用说明
在release处下载最新版本的压缩包，找个合适的位置解压。点击gui.pyw即可运行。  
### 如果要开机自启，请将gui.pyw的快捷方式扔到windows的启动文件夹。  
 * win7在C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup  
 * win10在使用win+r快捷键后输入shell:startup后即可打开。  
### 关于权重更改：  
 * ***目前版本只能通过更改name.ini来修改。格式为："name" = "value"***  
 * 其中"name"是要抽的人的名字，"value"是其对应的权重。  
 * "value"值***只能***为一个数字，否则整个程序会停止运行（因为我忘写异常处理了）  
修改后记得运行一次确定无误。  
***最好不要***用windows自带的记事本来编辑，哪怕是python自带的IDLE都比那强。  
# 更新计划
目前主要目标有：  
 * 打包成适用于各平台的.exe文件（我不确定pyinstaller在win10打包的文件能否在win7使用）  
 * 添加非手动的开机自启（这要等到我弄清windows注册表开机自启是怎么工作的）  
 * 足够方便的权重更改方式（要等到我弄清楚tkinter里面该死的Spinbox是怎么工作的）  
