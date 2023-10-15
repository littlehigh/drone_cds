# drone_cds
Use RTI DDS_Cloud Discovery Service to get Drone Information in Python
## 環境:
我的電腦:
> 作業系統: Window 10
> 已安裝程式: RTI DDS 6.1.1 + RTI DDS Connector Python

虛擬機(VMware):
> 作業系統: Ubuntu 22.04
> 已安裝程式: RTI DDS 6.1.1 + RTI DDS Connector Python + 無人機模擬器(px4 sitl)

## 執行步驟:
1. 先在虛擬機(VMware)的終端機執行無人機模擬器
`cd PX4-Autopilot`
`make px4_sitl jmavsim`
2. 在虛擬機(VMware)執行程式`pub.py` >>> 藉由pub.py 讓它write 無人機相關資訊到Topic: Drone中
3. 在我的電腦執行程式`sub.py`
4. 藉由RTI Lanucher 6.1.1 監視到程式是成功的

RTI Lanucher 6.1.1 監視畫面:
![image](https://github.com/littlehigh/drone_cds/blob/main/CDS_Success_RTI%20Launcher.JPG)

VS Code Terminal畫面:
![image](https://github.com/littlehigh/drone_cds/blob/main/CDS_Success_VS%20code.JPG)

