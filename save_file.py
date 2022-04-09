#!/usr/bin/python3
import cgi, os
import cgitb; cgitb.enable()
import datamining3
# import subprocess
print ("Content-Type: text/html\r\n")
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   # open('../CPS5721/upload/' + fn, 'wb').write(fileitem.file.read())
   open('../CPS5721/upload/testimag.jpg', 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   # result = subprocess.run(['/usr/bin/python3 datamining3.py --image ../CPS5721/upload/testimag.jpg --labels ../CPS5721/labels.txt --graph ../CPS5721/IMG_graph2.pb --input_layer Placeholder'], stdout=subprocess.PIPE)
   # subprocess.call('/usr/bin/python3 datamining3.py --image ../CPS5721/upload/testimag.jpg --labels ../CPS5721/labels.txt --graph ../CPS5721/IMG_graph2.pb --input_layer Placeholder', shell=True)

else:
   message = 'No file was uploaded'
print(message)
print("<br><br><img src='../CPS5721/upload/testimag.jpg' height=300 /><br>")
print("<pre>")
datamining3.mine()
print("</pre>")