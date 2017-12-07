勒索病毒漏洞修补程序说明：
【网御星云版权所有】


1、本修补程序功能【需以管理员身份运行程序】：
   1）MS17-010公告补丁修复，可支持的操作系统：WinXPSP3【32位】、Win2003SP2【32位/64位】、Win7SP1【32位/64位】、Win2008SP1【32位/64位】、VISTASP2【32位/64位】、Win8【32位/64位】。
         不支持为Win8.1、Win10、Win2012Server、Win2016Server安装补丁。这一部分操作系统存在系统版本较多，补丁文件巨大的情况，无法很好的集成至自动修补程序中。这一些补丁可手工至微软官网下载，下载链接可参考微软补丁公告。

   2）支持关闭全系列Windows操作系统SMB相关服务。并设置为禁用。关闭的服务名如下：
        browser
	rdr
	srv
	lmhosts
	netbt

   3）由于操作系统原因，部分终端有可能会出现安装补丁失败或停止服务失败情况，可尝试手工运行安装补丁和停止服务的操作。


3、微软官方的补丁包只支持部分在常维护的Windows操作系统版本，低版本操作系统如WinXPSP2、Win7SP0【无SP】需修复漏洞需先升级SP补丁才能支持安装MS17-010补丁。
部分低版本操作系统对应的SP补丁包可从这些地址下:
  1）、
XP简体中文版SP3补丁包下载地址：
【百度网盘】
http://pan.baidu.com/s/1jHJbSJc


  2）、
Win2003 Server简体中文版SP2补丁包下载地址：
【百度网盘】http://pan.baidu.com/s/1c3ZrL8

  3）、
Win7 X86/Win2008R2 X86 SP1补丁包下载地址：
【百度网盘】http://pan.baidu.com/s/1o8PV6rw

  4）、
Win7 X64/Win2008R2 X64 SP1补丁包下载地址：
【百度网盘】http://pan.baidu.com/s/1gfMMbB1



4、MS17-010补丁公告链接：https://technet.microsoft.com/zh-cn/library/security/ms17-010.aspx



注：本修补程序不支持病毒查杀和已中毒的终端文档解密，如需查杀病毒请使用辰信领创景云的专杀工具。

