# Image-Compressor
Image Compressor with good image quality

I have use Xampp Server for running imagecompressor.html
====================================================================================
make necessary changes in Xampp control pannel Under Apache Module inside config :
- select Apache(httpd.conf):
===================================================================================
Find AddHandler and add this line just after completing comments #:
   
AddHandler cgi-script .cgi .pl .asp .py
===================================================================================
Find <Directory "C:/xampp/htdocs"> and below that just after Options add this :

Options +Indexes +FollowSymLinks +Includes +ExecCGI

=====================================================================================
Now run that site on 127.0.0.1/your_folder_name/
