#Edited by Kaushal
import os
import pywhatkit as pwk
import datetime
import pyttsx3
import time
import speech_recognition as sr
from sys import platform
import subprocess
from pyasn1.type.univ import Null

def logo():
    x="""
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::     ARTH Team TASK 1 : Multi Tech Integration Menu    ::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                __
   #aws                      .-          -.             #teamwork
                            /              \    
                                                                                ####  copyright@ Team
        #s3                 |,  .-.    .-.  ,|    
                            | )( /    \ )( |
                            |/      /\      \|          $Cloudfront3
            (@_            <_       ^^     _> 
    _        ) \_____\ |IIIIII| /____________
    ( )@8@8@8@{}<_______________________/>>
             )_/                \ IIIIII  /                                     ::::::
            (@                    --------                                           ::
                                    @@@            
    =============================================================================================================

    ____ _____[ Voice ASSISTENT ]
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    _____________

    This Script will help in doing this task in Just simple steps. So, lets disscuss :

    """

    for i in range(len(x)):
        print(x[i],end='')
        time.sleep(0.0001)
    


def Auto_Clear():
    if platform == "win32":
        os.system("cls")
    else :
        os.system("clear")


# functions
def lcore():
    # f = os.popen("hostname -I | awk '{print $1}' ")
    nnip = input("enter the ip address of name node : ")
    os.system("echo \<configuration\> >> core-site.xml")
    os.system("echo \<property\> >> core-site.xml")
    os.system("echo \<name\>fs.default.name\</name\> >> core-site.xml")
    os.system("echo \<value\>hdfs\://{}\:9001\</value\> >> core-site.xml".format(nnip))
    os.system("echo \</property\> >> core-site.xml")
    os.system("echo \</configuration\> >> core-site.xml")
    os.system("rm -f  /etc/hadoop/core-site.xml ")
    os.system("cp core-site.xml /etc/hadoop/")
    os.system("rm -f core-site.xml")


def lhdfs():
    dirn = input("Enter the directory name eg. /namenode :  ")
    os.system("mkdir {}".format(dirn))
    os.system("echo \<configuration\> >> hdfs-site.xml")
    os.system("echo \<property\> >> hdfs-site.xml")
    os.system("echo \<name\>dfs.name.dir\</name\> >> hdfs-site.xml")
    os.system("echo \<value\>{}\</value\> >> hdfs-site.xml".format(dirn))
    os.system("echo \</property\> >> hdfs-site.xml")
    os.system("echo \</configuration\> >> hdfs-site.xml")
    os.system("rm -f  /etc/hadoop/hdfs-site.xml ")
    os.system("cp hdfs-site.xml /etc/hadoop/")
    os.system("rm -f hdfs-site.xml")


def lconfig():
    dirj = input("enter the directory name where java and hadoop file is present : ")
    os.system("rpm -i {}/jdk-8u171-linux-x64.rpm --force".format(dirj))
    os.system("rpm -i {}/hadoop-1.2.1-1.x86_64.rpm --force".format(dirj))
    lhdfs()
    lcore()
    os.system("systemctl stop firewalld")
    os.system("hadoop namenode -format")
    os.system("hadoop-daemon.sh start namenode")
    os.system("jps")



def ldhdfs():
    dird = input("Enter the directory name to Contribute  eg. /datanode :  ")
    os.system("mkdir {}".format(dird))
    os.system("echo \<configuration\> >> hdfs-site.xml")
    os.system("echo \<property\> >> hdfs-site.xml")
    os.system("echo \<name\>dfs.data.dir\</name\> >> hdfs-site.xml")
    os.system("echo \<value\>{}\</value\> >> hdfs-site.xml".format(dird))
    os.system("echo \</property\> >> hdfs-site.xml")
    os.system("echo \</configuration\> >> hdfs-site.xml")
    os.system("rm -f  /etc/hadoop/hdfs-site.xml ")
    os.system("cp hdfs-site.xml /etc/hadoop/")
    os.system("rm -f hdfs-site.xml")


def ldconfig():
    dir1 = input("enter the directory name where java and hadoop file is present : ")
    os.system("rpm -i {}/jdk-8u171-linux-x64.rpm --force".format(dir1))
    os.system("rpm -i {}/hadoop-1.2.1-1.x86_64.rpm --force".format(dir1))
    ldhdfs()
    lcore()
    os.system("systemctl stop firewalld")
    os.system("hadoop-daemon.sh start datanode")
    os.system("jps")


def rcore(koko):
    # f = os.popen("hostname -I | awk '{print $1}' ")
    os.system("ssh root@{} echo \<configuration\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<property\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<name\>fs.default.name\</name\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<value\>hdfs\://{}\:9001\</value\> >> core-site.xml".format(koko ,koko))
    os.system("ssh root@{} echo \</property\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \</configuration\> >> core-site.xml".format(koko))
    os.system("ssh root@{} rm -f  /etc/hadoop/core-site.xml".format(koko))
    os.system("ssh root@{} cp core-site.xml /etc/hadoop/core-site.xml".format(koko))
    os.system("ssh root@{} rm -f core-site.xml".format(koko))


def rhdfs(koko):
    dir1 = input("Enter the directory name eg. /namenode :  ")
    os.system("ssh root@{} mkdir {}".format(koko,dir1))
    os.system("ssh root@{} echo \<configuration\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<property\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<name\>dfs.name.dir\</name\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<value\>{}\</value\> >> hdfs-site.xml".format(koko,dir1))
    os.system("ssh root@{} echo \</property\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \</configuration\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} rm -f  /etc/hadoop/hdfs-site.xml".format(koko))
    os.system("ssh root@{} cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(koko))
    os.system("ssh root@{} rm -f hdfs-site.xml".format(koko))


def rnconfig(koko):
    rhdfs(koko)
    rcore(koko)
    os.system("ssh root@{} systemctl stop firewalld".format(koko))
    os.system("ssh root@{} hadoop namenode -format".format(koko))
    os.system("ssh root@{} hadoop-daemon.sh start namenode".format(koko))
    os.system("ssh root@{} jps".format(koko))


def rdcore(koko):
    # f = os.popen("hostname -I | awk '{print $1}' ")
    uu = input("Enter the Namenode IP : ")
    os.system("ssh root@{} echo \<configuration\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<property\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<name\>fs.default.name\</name\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \<value\>hdfs\://{}\:9001\</value\> >> core-site.xml".format(koko,uu))
    os.system("ssh root@{} echo \</property\> >> core-site.xml".format(koko))
    os.system("ssh root@{} echo \</configuration\> >> core-site.xml".format(koko))
    os.system("ssh root@{} rm -f  /etc/hadoop/core-site.xml".format(koko))
    os.system("ssh root@{} scp core-site.xml {}:/etc/hadoop/".format(koko))
    os.system("ssh root@{} rm -f core-site.xml".format(koko))


def rdhdfs(koko):
    dird = input("Enter the directory name to Contribute  eg. /datanode :  ")
    os.system("ssh root@{} mkdir {}".format(dird))
    os.system("ssh root@{} echo \<configuration\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<property\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<name\>dfs.data.dir\</name\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \<value\>{}\</value\> >> hdfs-site.xml".format(koko,dird))
    os.system("ssh root@{} echo \</property\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} echo \</configuration\> >> hdfs-site.xml".format(koko))
    os.system("ssh root@{} rm -f  /etc/hadoop/hdfs-site.xml".format(koko))
    os.system("ssh root@{} scp hdfs-site.xml {}:/etc/hadoop".format(koko))
    os.system("ssh root@{} rm -f hdfs-site.xml".format(koko))



def rdconfig(koko):
    rdhdfs(koko)
    rdcore(koko)
    os.system("ssh root@{} systemctl stop firewalld".format(koko))
    os.system("ssh root@{} hadoop-daemon.sh start datanode".format(koko))
    os.system("ssh root@{} jps".format(koko))

def rcconfig(koko):
    rdcore(koko)


def Intro():
    pyttsx3.speak("Hi Guys, I am Ronny. I am a Voice Assistent. I am here for your help. I can help you in several way. Like- Performing operation on various platforms and Technologies.")

def WindowMenu():
    flag=1
    while flag:
        pyttsx3.speak("Windows Menu ")
        windowsdata = ("""
            =====================================================================================================================
                ################################## *  Windows MENU  * ###########################################
            =====================================================================================================================

                Services:

                        1.chrome                    [say: open chrome or run chrome]
                        2.who are you               [say:who are you or tell me about your self]
                        3.notepad editor            [say:open editor]
                        4.microsoft edge            [say: open web browser]
                        5.whatsapp                  [say: open whatsapp]
                        6.direct message send       [say: send message]
                        7.telegram                  [say: open telegram ]
                        8.instragram                [say: open instragram]
                        9.calculater                [say: open calculater ]
                        10.zoom                     [say: open zoom]
                        11.vlc                      [say: open vlc]
                        12.wm player                [say: run windows player ]
                        13.control panel            [say: open control panel ]
                        14. facebook                [say: open fb ]
                        15. youtube                 [say: open youtube ]
                        16.video                    [say: play video ]
                        17.search or browse         [say: search ]
                        18.tell about topic         [say: tell me about topic]
                        19.shutdown                 [say: shutdown or poweroff ]
                        20.maps                     [say: open maps]
                        21.today weather            [say: today weather report]
                        22. music                   [say: play music or sing a song]
                        23.calculater               [say: open calculater ]
                        24.hi or hello              [say: hello ]

                Say " Menu " For Main Menu & "Exit or bye" for Exit.

                
            * Adding More Services Soon...


            """)
        path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        while 1:
            Auto_Clear()
            print(windowsdata)
            pyttsx3.speak("I can help in these services. Potal is under construction. We are adding more services soon. ")
            a=getAudioInput()
            a=a.upper()
            print(a)
            if ('DO NOT' in a or 'NOT' in a or 'DOES NOT' in a or 'NOT OPEN' in a):
                    pyttsx3.speak("As follows your cammends")
                    time.sleep(1)
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('CHROME' in a or 'CREAM' in a or 'GOOGLE' in a):
                pyttsx3.speak('   opening chrome browser for you')
                os.system('chrome')
            elif ('WHO ARE YOU' in a or 'WAHT IS YOUR NAME ' in a or 'TELL ME ABOUT YOURSELF' in a or 'TELL ME ABOUT YOU' in a or 'INTRODUCE YOURSELF' in a):
                pyttsx3.speak(
                    'my name is Ajay and i am here to help you in doing any task you can ask anything from me .')
            elif ('START' in a or'RUN' in a or 'OPEN' in a) and ('EDITOR' in a or 'TEXT EDITOR' in a):
                pyttsx3.speak('   opening notepad for u')
                os.system('notepad')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('MICROSOFT' in a or 'MICROSOFT EDGE' in a):
                pyttsx3.speak('   opening microsoft edge  for u')
                os.system('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
                os.system('pause')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('WHATSAPP' in a or 'WHATS APP' in a ):
                pyttsx3.speak('   opening whatsapp  for u')
                os.system('chrome whatsapp.com')
            elif ((('START' in a or 'RUN' in a or 'OPEN' in a) and ('TELEGRAM' in a))or ('TELEGRAM' in a)):
                pyttsx3.speak('  opening telegram  for u')
                os.system('chrome telegram.com')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('INSTAGRAM' in a or 'INSTA' in a):
                pyttsx3.speak('  opening instragram  for u')
                os.system('chrome instragram.com')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('CALCULATOR' in a or 'KELSIE' in a):
                pyttsx3.speak('  opening calculater  for u')
                os.system('chrome https://www.calculator.net/')
            elif ('LIVE' in a or 'RUN' in a or 'OPEN' in a) and ('ZOOM' in a or "video" in a):
                pyttsx3.speak('   opening zoom  for u')
                os.system('chrome zoom.us')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('WINDOWS MEDIA PLAYER' in a or 'WINDOW MEDIA PLAYER' in a):
                pyttsx3.speak('  opening windows media player  for u')
                os.system('wmplayer')
                os.system("pause")
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('VLC MEDIA PLAYER' in a  or 'VLC' in a):
                pyttsx3.speak('  opening vlc media player  for u')
                os.system('vlc')
                os.system("pause")

            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('CONTROL PANEL' in a):
                pyttsx3.speak('  opening control panel  for u')
                os.system('control panel')
                os.system("pause")
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('FACEBOOK' in a or 'FB' in a):
                pyttsx3.speak('  opening facebook  for u')
                os.system('chrome facebook.com')
            elif ('START' in a or 'RUN' in a or 'OPEN' in a) and ('YOUTUBE' in a or 'YOUTUBE.COM' in a):
                pyttsx3.speak('  opening youtube for u')
                os.system('chrome youtube.com')
            elif ('PLAY A VIDEO' in a or 'OPEN A VIDEO' in a or 'PLAY VIDEO' in a or 'OPEN VIDEO' in a):
                pyttsx3.speak('  which video do u want to play')
                print('which video do u want to play : ')
                video=getAudioInput()
                pyttsx3.speak('  playing {} for u'.format(video))
                pwk.playonyt(video)
                os.system("pause")
            elif ('SEND' in a or 'TEXT' in a) and (
                    'WHATSAPP MESSAGE ' in a or 'MESSAGE BY WHATSAPP' in a or 'MESSAGE FROM WATSAPP' in a or 'MESSAGE' in a):
                z = datetime.datetime.today()
                pyttsx3.speak('  plzz enter contect number ')
                contect = input('plz inter contect number : ')
                pyttsx3.speak('  plzz enter message to be sent ')
                msg = input('plz inter message to be sent : ')
                pwk.sendwhatmsg('+91' + contect, msg, z.hour, z.minute + 2)
                os.system("pause")

            elif ('SEARCH' in a or 'BROWSE' in a):
                pyttsx3.speak('  plzz tell me what do you want to search ')
                print('what do u want to search : ')
                browse=getAudioInput()
                pyttsx3.speak('searching' + browse + 'on google')
                pwk.search(browse)
                os.system("pause")
            elif ('TELL' in a or 'SPEAK' in a):
                pyttsx3.speak('  plzz tell me the topic ')
                topic = input('enter a topic : ')
                pyttsx3.speak(pwk.info(topic, 5))
                os.system("pause")
            elif ('DATE' in a or 'DINAK' in a):
                pd = datetime.date.today()
                pyttsx3.speak(pd)
                print(pd)
            elif ('SHUTDOWN' in a):
                pyttsx3.speak('closing window')
                print('closing window! in 30 second')
                pwk.shutdown(30)
                os.system("countdown 29")


            elif ('OPEN' in a or 'RUN' in a) and ('GOOGLE MAPS' in a or 'MAPS' in a):
                pyttsx3.speak('opening google maps')
                os.system('chrome https://www.google.com/maps/@23.2664042,77.4357627,15z')
                os.system("pause")
            elif ('OPEN' in a or 'RUN' in a or 'TODAY' in a) and (
                    'today weather' in a or ' weather' in a or 'weather report' in a):
                pyttsx3.speak('opening weather report')
                os.system(
                    'chrome https://www.google.com/search?q=today+weather&rlz=1C1CHBF_enIN912IN912&oq=today+we&aqs=chrome.1.69i57j0l7.9358j0j7&sourceid=chrome&ie=UTF-8')
            elif ('OPEN' in a or 'RUN' in a) and (
                    'AMAZON.COM' in a or 'AMAZON.IN' in a or 'SHOPING WEB SITE' in a or 'SHOPPING SITE' in a):
                pyttsx3.speak('opening amazon')
                os.system('chrome https://www.amazon.in/ ')
            elif ('OPEN' in a or 'RUN' in a or 'PLAY' in a) and ('MUSIC' in a or 'PLAY MUSIC' in a or 'SONG' in a):
                pyttsx3.speak('  which song do u want to play')
                print('which song do u want to play : ')
                song=getAudioInput()  
                pyttsx3.speak('  playing {} for u on Youtube'.format(song))
                pwk.playonyt(song)
                os.system("pause")
            elif ('HI' in a or 'HELLO' in a):
                pyttsx3.speak('hello sir wellcome you please assign a task')
                print('hello sir wellcome you please assign a task')
            elif(("MENU" in a) ):
                flag=0
                break
            elif(("EXIT"in a) or ("BYE" in a) ):

                out()
            elif("PAUSE" in ch):
                os.system("pause")
            else:
                pyttsx3.speak(" 'sorry sir i am not able to understand what do you want.  type exit or close to leave the program !")
        pyttsx3.speak("Going back to Menu")

def StandardPartition(ip):
    os.system("ssh root@{} fdisk -l".format(ip))
    diskName = input("Enter the disk name")
    os.system("ssh root@{} fdisk {}".format(ip,diskName))
    os.system("ssh root@{} udevadm settle".format(ip))
    os.system("ssh root@{} fdisk {} -l ".format(ip,diskName))
    pp = input("enter the new Partition name to format")
    os.system("ssh root@{} mkfs.ext4 {}".format(ip,pp))
    mm = input("enter the directory to mount on : ")
    os.system("ssh root@{} mount {} {}".format(ip,pp, mm))
    print("partition is successfully created")

def LvmPartition(aa):
    os.system("ssh root@{} fdisk -l".format(aa))
    pp = input("Enter disk name")
    os.system("ssh root@{} pvcreate {}".format(aa,pp))
    os.system("ssh root@{} pvdisplay".format(aa))
    vg = input("Enter Volume Group Name : ")
    pv1 = input("Enter Physical Volume 1 : ")
    pv2 = input("Enter Physical Volume 2 : ")
    os.system("ssh root@{} vgcreate {} {} {} ".format(aa,vg, pv1, pv2))
    os.system("ssh root@{} vgdisplay".format(aa))
    lv = input("Enter the Logical volume Name : ")
    sz = input("Enter size ")
    os.system("ssh root@{} lvcreate --size {} --name {}".format(aa,sz, vg))
    os.system("ssh root@{} mkfs.ext4 /dev/{}/{}".format(aa,vg, lv))
    mn = input("Enter the directory you want to mount on : ")
    os.system("ssh root@{} mount /dev/{}/{} {}".format(aa,vg, lv, mn))
    os.system("ssh root@{} df -h".format(aa))

def LinuxMenu():
    #flag=1
    #while flag:    
    Auto_Clear()
    pyttsx3.speak("linux menu")
    linuxdata = ("""
        =====================================================================================================================
            ################################## *  Linux MENU  * ###########################################
        =====================================================================================================================
                services:

                    1 : Standard Partition    [say standard partiton or disk partition]
                    2 : LVM Partition         [say LVM partition]
                    3 : Random Command        [say Random ]
                    

                Say " Menu " For Main Menu & "Exit or bye" for Exit.

                
            * Adding More Services Soon...

        """)

    while 1:
        print(linuxdata)
        pyttsx3.speak("I can help in these services. Potal is under construction. We are adding more services soon. ")
        if platform == "win32":
            pyttsx3.speak("I found that you are on Windows Platform. You can't access these service here. So, use remote login. So, Enter your Remote IP :")
            ip = input("\nEnter Remote IP (e for exit) : ")
        else:
            pyttsx3.speak("I found that you are on Linux Platform. So, Enter your your IP to access services:")
            ip = input("\nEnter your IP (e for exit) : ")

        if(ip=="e"):
            pyttsx3.speak("Returning to Service Menu")
            #flag=0
            break
        pyttsx3.speak("Which Service do you want to access.")
        ch = getAudioInput()
        print(ch)
        if("Standard partition" in ch )or("disk"in ch) or ("disk partition")or("Disk Partition"in ch):
            StandardPartition(ip)
        elif (("LVM" in ch) or ("Lvm" in ch) or ("lvm" in ch) or ("LVM Partition" in ch) or ("lvm partition" in ch)):
            LvmPartition(ip)
        elif (("random" in ch) or ("Command" in ch) or ("command" in ch) or ("Random" in ch)):
            print("Enter Random Command")
            pyttsx3.speak("Enter Random Command")
            command = input()
            pyttsx3.speak("Executing Command.")
            os.system("ssh root@{} {}".format(ip,command))
            os.system("pause")
        elif(("menu" in ch) ):
            #flag=0
            pyttsx3.speak("back to service menu.")
            break
        elif(("exit"in ch) or ("bye" in ch) ):
            out()
        elif ("PAUSE" in ch):
            os.system("pause")
        else:
            print("Input is invalid")
            pyttsx3.speak("Invalid Input")
            time.sleep(1)




def HadoopMenuMaker(data):
    Assigndata=("""
        =====================================================================================================================
            ################################## *  BigData {} MENU  * ###########################################
        =====================================================================================================================
        
                # Services :

                        1. Configure Namenode           [say : create namenode]
                        2. Configure Datanode           [say : create datanode]
                        3. Configure Client             [say : create Client ]
                        4. Open Web Interface           [say : open web app]
                        5. Check Hadoop Report          [say : show report]
                        6. List all Files (/ folder)    [say : list all]
                        7. Upload file                  [say : upload file]
                        


            Say " Menu " For Main Menu & "Exit or bye" for Exit.

    """).format(data)
    return Assigndata

def HadoopRemotely():
    pyttsx3.speak("Bigdata Remote Menu")
    Remotedata=HadoopMenuMaker("Remote")
    print(Remotedata)
    ch=getAudioInput()
    print(ch)
    koko=input("Enter the IP address")
    if("configure"in ch)or("Namenode "in ch)or("Configure Name Node" in ch)or ("Configure Data" or ch):
        #rnip = input("Enter the remote IP address you want to configure as  name node : ")
        rnconfig(koko)
    elif("Configure" in ch) or ("Datanode" in ch) or ("Configure Data Node" in ch) or ("Configure Data" or ch):
        
        rdconfig(koko)
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
                
        rcconfig(koko)
    elif("open web" in ch) or ("web Interface" in ch) or ("Interface" in ch) or ("open web services" or ch):
        kk=input("Enter the IP address of Namenode")
        os.system("chrome 50070:{}".format(kk))
    elif("Check Hadoop Report" in ch) or ("Check Report" in ch) or ("Check" in ch) or ("hadoop Report" or ch):
              
        os.system("ssh root@{} hadoop dfsadmin -report | less".format(koko))
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
        os.system("ssh root@{} hadoop fs -ls /".format(koko))
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
        path=input("Enter the path of the file : ")
        os.system("ssh root@{} hadoop fs -put {} /".format(koko))
    else :
        print("Inupt is invalid")
            
    

def HadoopLocal():
    pyttsx3.speak("Bigdata Local Menu")
    Remotedata=HadoopMenuMaker("Local")
    print(Remotedata)
    print(ch)
    koko=input("Enter the IP address")
    if("configure"in ch)or("Namenode "in ch)or("Configure Name Node" in ch)or ("Configure Data" or ch):
        #rnip = input("Enter the remote IP address you want to configure as  name node : ")
        rnconfig(koko)
    elif("Configure" in ch) or ("Datanode" in ch) or ("Configure Data Node" in ch) or ("Configure Data" or ch):
        
        rdconfig(koko)
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
                
        rcconfig(koko)
    elif("open web" in ch) or ("web Interface" in ch) or ("Interface" in ch) or ("open web services" or ch):
        kk=input("Enter the Namenode IP address of ")
        os.system("chrome 50070:{}".format(kk))
    elif("Check Hadoop Report" in ch) or ("Check Report" in ch) or ("Check" in ch) or ("hadoop Report" or ch):
              
        os.system("ssh root@{} hadoop dfsadmin -report | less".format(koko))
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
        os.system("ssh root@{} hadoop fs -ls /".format(koko))
    elif("Configure" in ch) or ("client" in ch) or ("Configure client" in ch):
        path=input("Enter the path of the file : ")
        os.system("ssh root@{} hadoop fs -put {} /".format(koko))
    else :
        print("Inupt is invalid")

    

def HadoopCloud():
    pyttsx3.speak("Bigdata Cloud Menu")
    Remotedata=HadoopMenuMaker("Cloud")
    print(Remotedata)
    os.system("pause")

def BigDataMenu():
    pyttsx3.speak("Big Data Menu")
    bigdata=("""
        =====================================================================================================================
            ################################## *  BigData Access MENU  * ###########################################
        =====================================================================================================================
        
        
                                                        Configure Hadoop
                                                                |    
                                                                |
                            --------------------------------------------------------------------------
                            |                                     |                                   |
                            |                                     |                                   |
                        Local login                          Remote login                   Cloud Login (using key)
                        (say : local)                       (say : Remote)                      (say : Cloud)




                            Say " Menu " For Main Menu & "Exit or bye" for Exit.

                        
            * Adding More Services Soon...

    """)
    while 1:
        print(bigdata)
        pyttsx3.speak(" Where do you want to work ? . Locally or Remotely or on cloud. ")
        ch=getAudioInput()
        print(ch)
        if("remote"in ch)or("Remote "in ch)or("Remote Login" in ch):
            HadoopRemotely()
        elif(("local" in ch) or ("Local" in ch) or ("Local login" in ch)):
            HadoopLocal()
        elif(("cloud" in ch) or ("Cloud" in ch) or ("aws login" in ch) or ("Cloud login")):
            HadoopCloud()
        elif(("menu" in ch) ):
            break
        elif(("exit"in ch) or ("bye" in ch) ):
            out()
        elif ("pause" in ch)or("Pause" in ch):
            os.system("pause")
        else:
            print("Input is invalid")
            pyttsx3.speak("Invalid Input")
            time.sleep(1)


        


def PythonMenu():
    flag=1
    while flag:
        Auto_Clear()
        pyttsx3.speak("I am forwarding you to Python World.")
        pythondata="""
        =====================================================================================================================
                ################################## *  Python World  * ###########################################
            =====================================================================================================================
                                                    WORKSPACE
                                                        |    
                                                        |
                                    -------------------------------------------
                                    |                                         |
                                    |                                         |
                            Python REPL                            Jupyter Notebook
                            (say: repl)                            (say: Notebook)

                Say " Menu " For Main Menu & "Exit or bye" for Exit.

                
            * Adding More Services Soon...

        """
        while 1:
            print(pythondata)
            pyttsx3.speak("Where you want to work.  1. Python REPL. 2. Jupter Notebook.")
            ch=getAudioInput()
            if(("repl" in ch) or ("apple" in ch) or ("Repl" in ch) or ("Apple" in ch)):   
                if platform == "win32":
                    os.system("python")
                else :
                    os.system("python3")
            elif(("notebook" in ch) or ("Notebook" in ch) or ("book" in ch) or ("Book" in ch)):
                pyttsx3.speak("Click Quit to quit Jupyter Notebook server in Browser.")
                print("Click Quit to quit Jupyter Notebook server in Browser.")
                time.sleep(1)
                pyttsx3.speak("Starting Jupyter Notebook")
                os.system('jupyter notebook')
                time.sleep(2)
                pyttsx3.speak("Going Back to Python Menu.")
                break
            elif(("menu" in ch) ):
                flag=0
                break
            elif(("exit"in ch) or ("bye" in ch) ):
                out()
            elif ("pause" in ch) or ("Pause" in ch):
                os.system("pause")
            else:
                pyttsx3.speak("Sorry Sir I don't get You. Please assign me again.")
                print("Sorry Sir I don't get You. Please assign me again.")
                time.sleep(1)
    

def AWSMenu():
    
    pyttsx3.speak("AWS Menu ")
    AWSData=("""


    =====================================================================================================================
        ################################## *  Aws MENU  * ###########################################
    =====================================================================================================================


            Services :
                
                 1  : Install AWS CLI                      [say: Install AWS]
                 2  : AWS Configure                        [say: Configure]
                 3  : Create Key                           [say: create key]
                 4  : Create Security Group                [say: create SG or create group]
                 5  : Launch New AWS Instance              [say: launch instance]
                 6  : Start Instance                       [say: start instance]
                 7  : Stop Instance                        [say: Stop instance]
                 8  : Create EBS Volume                    [say: create volume]
                 9  : Attach EBS Volume To Instance        [say: Attach Volume]
                 10 : Detach EBS Volume                    [say: remove volume]
                 11 : Delete EBS Volume                    [say: Delete Volume]
                 12 : Create S3 Bucket                     [say : Create bucket]
                 13 : Upload Data in S3 Bucket             [say: upload data]
                 14 : Create Cloud Fornt Distribution      [say: create CDN]
                 15 : Create Snapshot                      [say: create snaps]
                		

                

            
            Say " Menu " For Main Menu & "Exit or bye" for Exit.

            * Adding More Services Soon...

    """)

    while 1:
        print(AWSData)
        pyttsx3.speak("I can help in these services. Portal is under construction. We are adding more services soon. ")
        ch=getAudioInput()
        print(ch)
        
        if ("Install" in ch) or ("AWS CLI" in ch):
            pyttsx3.speak("processing please wait....")
            os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip' ")
            os.system("unzip awscliv2.zip")
            os.system("sudo ./aws/install")
            print(" aws --version   echo \AWS is success fullly installed")

         
        elif ("AWS" in ch) or ("Configure" in ch) or ("AWS Configure" in ch):
            pyttsx3.speak("processing please wait....")
            os.system("aws configure")
        elif ("pair" in ch) or ("key" in ch):
            pyttsx3.speak("processing please wait....")
            na =input("Enter key name : ")
            os.system("aws ec2 create-key-pair --key-name  {} --output text > {}.pem".format(na,na) )
        elif ("security" in ch) or ("group" in ch):
            pyttsx3.speak("processing please wait....")
            nam= input("Enter Security group name : ")
            desc = input("enter description : ")
            os.system("aws ec2 create-security-group --group-name {} --description {}".format(nam,desc))
        elif ("launch" in ch)or ("Instance" in ch):
            pyttsx3.speak("processing please wait....")
            na = input("Enter key name : ")
            sgi = input("Enter Security group id : ")
            co = input("Enter no. of instance you want to launch : ")
            os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count {} --subnet-id subnet-4d225201 --security-group-ids {} --key-name {}".format(co,sgi,na) )
        elif ("Start" in ch) or ("Instance" in ch) or ("Start Instance" in ch ):
            pyttsx3.speak("processing please wait....")
            ids =input("Enter Instance-Ids : ")
            os.system("aws ec2 start-instances --instance-ids {}".format(ids))
        elif ("Stop" in ch) or ("Instance" in ch) or ("Stop Instance" in ch ):
            pyttsx3.speak("processing please wait....")
            na =input("Enter Instance-Ids : ")
            os.system("aws ec2 stop-instances --instance-ids {} ".format(na) )
        elif ("EBS" in ch) or ("Volume" in ch) or (" Create EBS Volume" in ch ) :
            pyttsx3.speak("processing please wait....")
            sz =input("Enter size in GB's : ")
            os.system("aws ec2 create-volume  --volume-type gp2 --size {}  --availability-zone ap-south-1b".format(sz))
        elif ("attach" in ch) or ("attach volume " in ch) :
            pyttsx3.speak("processing please wait....")
            vid =input("Enter Volume Id : ")
            iid =input("Enter Instance-Ids : ")
            os.system("aws ec2 attach-volume  --volume-id {} --instance-id {} --device /dev/sdf".format(vid,iid))
        elif ("detach" in ch) or (" Detach Volume" in ch) :
            pyttsx3.speak("processing please wait....")
            sz =input("Enter volume Id  : ")
            os.system("aws ec2 detach-volume  --volume-id {} ".format(sz))
        elif ("Delete" in ch) or ("Delete Volume" in ch) :
            pyttsx3.speak("processing please wait....")
            sz =input("Enter volume Id  : ")
            os.system("aws ec2 delete-volume  --volume-id {} ".format(sz))
        elif (" Create Bucket" in ch) or (" Create S3" in ch) or ("S3 Bucket" in ch ):
            pyttsx3.speak("processing please wait....")
            sz =input("Enter Name for Bucket : ")
            os.system("aws s3api create-bucket --bucket {}  --create-bucket-configuration LocationConstraint=ap-south-1".format(sz))
        elif ("upload in s3" in ch) or ("upload in bucket" in ch) or ("upload" in ch ):
            pyttsx3.speak("processing please wait....")
            sz =input("Enter the path of file : ")
            ph =input("Enter Name of Bucket : ")
            os.system("aws s3 cp {} s3://{} --acl public-read-write ".format(sz,ph))
        elif ("cloud front" in ch) or ("Distribution" in ch) or ("Create Distribution " in ch ):
            pyttsx3.speak("processing please wait....")
            sz =input("Enter S3 bucket name : ")
            ph =input("Enter Data Name : ")
            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {} ".format(sz,ph))
        
        elif ("Snapshot" in ch) or (" create" in ch) or (" create snapshot" in ch ):
            pyttsx3.speak("processing please wait....")
            sz =input("Enter Volume Id : ")
            os.system("aws ec2 create-snapshot --volume-id {}".format(sz))
        elif(("menu" in ch) ):
            break
        elif(("exit"in ch) or ("bye" in ch) ):
            out()
        else:
            print("Input is invalid")
        


def out():
    pyttsx3.speak("Thanks for Using Me. Good Day. Bye, See ya")
    exit()
    

def getAudioInput():
    while 1:
        with sr.Microphone() as source:
                pyttsx3.speak('start saying........................')
                print("start saying........................")
                audio = r.listen(source)
                pyttsx3.speak('speech done...wait a second..')
        #try:
        ch = r.recognize_google(audio)
        break
        #except ValueError:
        #    pyttsx3.speak("Sorry Sir I don't get You. Please assign me again.")
        #    print("Sorry Sir I don't get You. Please assign me again.")
        #    ch="ok"        
    return ch

def DevopsMenu():
    pyttsx3.speak("Devops Menu ")
    DevopsData=("""


    =====================================================================================================================
        ################################## *  Devops MENU  ** ###########################################
    =====================================================================================================================


            Services :
                
                 1 : Docker Images                                  [say : list images]
                 2 : Download Docker images                         [say : pull image]
                 3 : Launch Docker Container                        [say : Launch container]
                 4 : Live running Containers                        [say : running container or live container]
                 5 : Start the existing Docker Container            [say : start container ]
                 6 : Delete the Docker Container                    [say : delete or remove container ]
                 7 : Delete the Docker Image                        [say : delte image or remove image]
                 8 : Delete all the Docker Containers in 1 Go       [say : delete all or Reset ]

                

            
            Say " Menu " For Main Menu & "Exit or bye" for Exit.

            
            * Adding More Services Soon...

    """)

    while 1:
        if platform == "win32":
            print(DevopsData)
            pyttsx3.speak("I found that you are on Windows Platform. You can't access these service here. So, use remote login. So, Enter your Remote IP :")
            ip = input("\nEnter Remote IP (e for exit) : ")
            pyttsx3.speak("I can help in these services. Potal is under construction. We are adding more services soon. ")
            ch=getAudioInput()
            print(ch)
        
            if(("menu" in ch) ):
                break
            elif ("List images" in ch )or ("list images" in ch):
                os.system("ssh root@{} docker images").format(ip)
            elif ("pull" in ch or "Pull" in ch or "Pull images" in ch):
                im = input("enter the name of OS : ")
                os.system("ssh root@{} docker pull {}".format(ip,im))
            elif  ("Launch" in ch or "launch" in ch or "Launch container" in ch or  "Run container" in ch):
                im = input("Enter the name of OS you want to Launch : ")
                na = input("Enter name of container : ")
                os.system("ssh root@{} docker run -it --name {}  {}".format(ip,na, im))     
            elif  ("Live" in ch or "Running" in ch or "Live container" in ch or  "Running container" in ch):
                os.system("ssh root@{} docker ps -a").format(ip)
            elif  ("Start" in ch or "start" in ch and "container" in ch or  "Container" in ch):
                na = input("Enter the name or Id of container")
                os.system("ssh root@{} docker start -ai {}".format(ip,na))
            elif  ("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "container" in ch or  "Container" in ch):
                na = input("Enter name or ID of container : ")
                os.system("ssh root@{} docker rm {}".format(ip,na))
            elif  ("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "image" in ch or  "Image" in ch):
                na = input("Enter name of Image : ")
                os.system("ssh root@{} docker rmi {} ".format(ip,na))
            elif  (("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "all" in ch or  "All" in ch) or "reset" in ch or "Reset" in ch):
                os.system("ssh root@{} docker rm `docker ps -a -q`").format(ip)
            elif(("exit"in ch) or ("bye" in ch) ):
                out()
            elif ("pause" in ch)or("Pause" in ch):
                os.system("pause")
            else:
                print("Input is invalid")
                pyttsx3.speak("Invalid Input")
                time.sleep(1)
        
        else:
            print(DevopsData)
            pyttsx3.speak("I found that you are on Linux Platform. So, Enter your your IP to access services:")
            ip = input("\nEnter your IP (e for exit) : ")
            pyttsx3.speak("I can help in these services. Potal is under construction. We are adding more services soon. ")
            ch=getAudioInput()
            print(ch)
            if(("menu" in ch) ):
                break
            elif ("List images" in ch )or ("list images" in ch):
                os.system("ssh root@{} docker images").format(ip)
            elif ("pull" in ch or "Pull" in ch or "Pull images" in ch):
                im = input("enter the name of OS : ")
                os.system("ssh root@{} docker pull {}".format(ip,im))
            elif  ("Launch" in ch or "launch" in ch or "Launch container" in ch or  "Run container" in ch):
                im = input("Enter the name of OS you want to Launch : ")
                na = input("Enter name of container : ")
                os.system("ssh root@{} docker run -it --name {}  {}".format(ip,na, im))     
            elif  ("Live" in ch or "Running" in ch or "Live container" in ch or  "Running container" in ch):
                os.system("ssh root@{} docker ps -a").format(ip)
            elif  ("Start" in ch or "start" in ch and "container" in ch or  "Container" in ch):
                na = input("Enter the name or Id of container")
                os.system("ssh root@{} docker start -ai {}".format(ip,na))
            elif  ("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "container" in ch or  "Container" in ch):
                na = input("Enter name or ID of container : ")
                os.system("ssh root@{} docker rm {}".format(ip,na))
            elif  ("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "image" in ch or  "Image" in ch):
                na = input("Enter name of Image : ")
                os.system("ssh root@{} docker rmi {} ".format(ip,na))
            elif  (("Remove" in ch or "remove" in ch  or "delete" in ch or "Delete" in ch and "all" in ch or  "All" in ch) or "reset" in ch or "Reset" in ch):
                os.system("ssh root@{} docker rm `docker ps -a -q`").format(ip)
            elif(("exit"in ch) or ("bye" in ch) ):
                out()
            elif ("pause" in ch)or("Pause" in ch):
                os.system("pause")
            else:
                print("Input is invalid")
                pyttsx3.speak("Invalid Input")
                time.sleep(1)
        
            
            

def ServiceMenu():
    while 1 :
        Auto_Clear()
        pyttsx3.speak("Service Menu ")

        ServiceData=("""


        =====================================================================================================================
            ################################## *  SERVICE MENU  ** ###########################################
        =====================================================================================================================


                Services :
                    
                    
                    1. AWS Services 
                    2. Windows Services
                    3. Linux Services
                    4. Devops Services 
                    5. Big Data Related Services 
                    6. Python Intrperator


                
                Say " Exit or bye" For Exit Program.

                
            * Adding More Services Soon...

        """)

        print(ServiceData)
        pyttsx3.speak("I can help in following services. 1. AWS Services. 2. Windows Sevices. 3. Linux Services. 4. Devops Services. 5. Big Data Related Services. 6. Python Intrperator. ")

        while True:
            ch = getAudioInput()
            print(ch)
        
            if ("aws" in ch) or ("AWS" in ch) or ("aw services" in ch) or ("e w s" in ch)or ("ebs services" in ch)or("tws services" in ch):
                AWSMenu()
                break               
            elif ("windows" in ch) or ("Windows" in ch) or ("Windows services" in ch) or ("Win Services" in ch):
                WindowMenu()
                break
            elif ("Linux" in ch) or ("linux" in ch) or ("Linux services" in ch) or ("linux services" in ch):
                LinuxMenu()
                break
            elif ("Devops" in ch) or ("devops" in ch) or ("Devops services" in ch) or ("devops services" in ch)or("Docker services" in ch )or ("docker services" in ch):
                DevopsMenu()
                break
                
            elif ("Bigdata" in ch) or ("big Data" in ch)or("bigdata" in ch) or ("Big Data" in ch)or("bigdata services" in ch) or ("big" in ch)or("hadoop services" in ch )or ("data services" in ch)or("hadoop" in ch):
                BigDataMenu()
                break
            
            elif ("python" in ch) or ("py" in ch) or ("Python" in ch) or ("python services" in ch )or ("Python services" in ch):
                PythonMenu()
                break
            
            elif ("exit" in ch) or ("Exit" in ch) or ("Out" in ch) or ("shutup" in ch )or ("bye" in ch):
                out()
            elif ("pause" in ch) or ("Pause" in ch):
                os.system("pause")
            else:
                pyttsx3.speak("Sorry Sir I don't get You. Please assign me again.")
                print("Sorry Sir I don't get You. Please assign me again.")
                time.sleep(1)      
            Auto_Clear() 
            print(ServiceData)
            pyttsx3.speak("How I can help you Sir.")
                
        
            
def StartProgram(): 
    #logo()
    #Intro()
    Auto_Clear()
    ServiceMenu()

r = sr.Recognizer()


StartProgram()
