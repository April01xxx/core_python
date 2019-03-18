# 第二章网络编程（network programming）笔记
---

1. **TIPC协议：**爱立信开源的透明进程间通信协议，一般用于集群系统中，底层是基于socket
实现的，但是并非利用`IP地址+端口号`来标识通信的双方，而是将服务注册到内核中，这样对于
应用层而言，对端地址仅仅是一个服务类型。
2. python3中`send函数`发送的数据是`byte类型`的，不接受`str类型`，故数据在发送前需要
转码。
