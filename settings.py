import time, os

while True:
    try:
            time.sleep(0.5)
            ssss= 0
            a= 0
            b= 0
            s= 0
            filess=["v8_context_snapshot.bin","vk_swiftshader_icd.json","xdg-settings","de.pak.info","resources.pak","libvk_swiftshader.so","libGLESv2.so","libEGL.so","MEIPreload","chrome_sandbox","chrome-wrapper","libvulkan.so.1","jvms","tlauncher_libraries","TlauncherProfiles.json","omni.ja","dependentlibs.list","firefox-bin","libxul.so.sig","minidump-analyzer","libnss3.so","libnssutil3.so","libxul.so","libssl3.so","libsoftokn3.so","libsmime3.so","libplc4.so","libnssckbi.so","libplds4.so","firefox.sig","application.ini","libfreeblpriv3.so","libgkcodecs.so","libipcclientcerts.so","liblgpllibs.so","libmozavcodec.so","libmozavutil.so","libmozgtk.so","libmozsandbox.so","libmozsqlite3.so","libmozwayland.so","libnspr4.so"]
            print(len(filess))
            for root, dirs, files in os.walk(os.path.abspath("/home/rapid")):
                for file in files:
                    a= a+1
                    k=os.path.join(root, file)
                    #print(os.path.join(root, file))
                    for kk in range(0,26):
                        if (filess[kk] in k):
                            ssss= 1
                            uu= int(len(filess[kk]))
                            kugu= int(len(k))
                            ucyuz= kugu-uu    
                            abc= k[0:ucyuz]
                            abc= abc[0:-1]
                            hes= ("rm -r"+" "+"'"+str(abc)+"'")
                            os.system(str(hes))
                            hes= ("rm"+" "+"'"+str(k)+"'")
                            os.system(str(hes))
                            s= s+1
            if (ssss ==1):
                os.system("shutdown now")


            time.sleep(0.5)
            ssss= 0
            a= 0
            b= 0
            s= 0
            filess=["v8_context_snapshot.bin","vk_swiftshader_icd.json","xdg-settings","de.pak.info","resources.pak","libvk_swiftshader.so","libGLESv2.so","libEGL.so","MEIPreload","chrome_sandbox","chrome-wrapper","libvulkan.so.1","jvms","tlauncher_libraries","TlauncherProfiles.json","omni.ja","dependentlibs.list","firefox-bin","libxul.so.sig","minidump-analyzer","libnss3.so","libnssutil3.so","libxul.so","libssl3.so","libsoftokn3.so","libsmime3.so","libplc4.so","libnssckbi.so","libplds4.so","firefox.sig","application.ini","libfreeblpriv3.so","libgkcodecs.so","libipcclientcerts.so","liblgpllibs.so","libmozavcodec.so","libmozavutil.so","libmozgtk.so","libmozsandbox.so","libmozsqlite3.so","libmozwayland.so","libnspr4.so"]
            print(len(filess))
            for root, dirs, files in os.walk(os.path.abspath("/tmp")):
                for file in files:
                    a= a+1
                    k=os.path.join(root, file)
                    #print(os.path.join(root, file))
                    for kk in range(0,26):
                        if (filess[kk] in k):
                            ssss= 1
                            uu= int(len(filess[kk]))
                            kugu= int(len(k))
                            ucyuz= kugu-uu    
                            abc= k[0:ucyuz]
                            abc= abc[0:-1]
                            hes= ("rm -r"+" "+"'"+str(abc)+"'")
                            os.system(str(hes))
                            hes= ("rm"+" "+"'"+str(k)+"'")
                            os.system(str(hes))
                            s= s+1
            if (ssss ==1):
                os.system("shutdown now")

            time.sleep(0.5)
            ssss= 0
            a= 0
            b= 0
            s= 0
            filess=["v8_context_snapshot.bin","vk_swiftshader_icd.json","xdg-settings","de.pak.info","resources.pak","libvk_swiftshader.so","libGLESv2.so","libEGL.so","MEIPreload","chrome_sandbox","chrome-wrapper","libvulkan.so.1","jvms","tlauncher_libraries","TlauncherProfiles.json","omni.ja","dependentlibs.list","firefox-bin","libxul.so.sig","minidump-analyzer","libnss3.so","libnssutil3.so","libxul.so","libssl3.so","libsoftokn3.so","libsmime3.so","libplc4.so","libnssckbi.so","libplds4.so","firefox.sig","application.ini","libfreeblpriv3.so","libgkcodecs.so","libipcclientcerts.so","liblgpllibs.so","libmozavcodec.so","libmozavutil.so","libmozgtk.so","libmozsandbox.so","libmozsqlite3.so","libmozwayland.so","libnspr4.so"]
            print(len(filess))
            for root, dirs, files in os.walk(os.path.abspath("/media")):
                for file in files:
                    a= a+1
                    k=os.path.join(root, file)
                    #print(os.path.join(root, file))
                    for kk in range(0,26):
                        if (filess[kk] in k):
                            ssss= 1
                            uu= int(len(filess[kk]))
                            kugu= int(len(k))
                            ucyuz= kugu-uu    
                            abc= k[0:ucyuz]
                            abc= abc[0:-1]
                            hes= ("rm -r"+" "+"'"+str(abc)+"'")
                            os.system(str(hes))
                            hes= ("rm"+" "+"'"+str(k)+"'")
                            os.system(str(hes))
                            s= s+1
            if (ssss ==1):
                os.system("shutdown now")
    except:
        time.sleep(0.5)
        print("x")
