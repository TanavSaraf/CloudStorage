
import dropbox

class TransferData :
   def  __init__(self,access_token):
       self.access_token=access_token
   def upload(self,fileFrom,fileTo):
       dbx = dropbox.Dropbox(self.access_token)
       
       with open(fileFrom,'rb') as f:
           dbx.files_upload(f.read(),fileTo)

def main() :
    accessToken="sl.BFQYgi31X8BCR__wE-2vj-F0Qt-zAkXvKuNMtEN-cB3KXA6krypgLyyvWyoBIU-fGXTBztr-n78aqUoS1AIK1YUpELrU27wjgYaH4mfIDJx2oKdD2fLetdhoiVRPqpUyDYAm_8aMCo68"          
    transferData=TransferData(accessToken)
    fileFrom = input("The location of source fle to be uploaded : ")
    fileTo = input("The location on which it needs to be saved : ")
    
    transferData.upload(fileFrom, fileTo)
    
main()
