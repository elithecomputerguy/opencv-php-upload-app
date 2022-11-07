# opencv-php-upload-app
Allows you to upload pictures and see which ones are detected by OpenCV

This creates a web app to show you what OpenCV "sees"

PHP is used to create a HTML form that allows you to pick which Cascade Filter to use, and then upload multiple pictures

The pictures are uploaded and then PHP uses shell_exec to trigger the python script to scan the pictures and print out the results

These is a delete pictures PHP script using GET

For this to work your server needs PHP, Python3, OpenCV running, the OpenCV Data folder in the HTML root directory
