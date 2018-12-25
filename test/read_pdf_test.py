# encoding: utf-8
import fitz

def pdf2pic(path):
    
    checkXO = r"/Type(?= */XObject)" 
    checkIM = r"/Subtype(?= */Image)"  
     
    doc = fitz.open(path)
    lenXREF = doc._getXrefLength()
    print('文件名：{}，页数：{}，对象：{}'.format(path, len(doc), lenXREF-1))
    
    imgcount = 0
    for i in range(1, lenXREF):
        text = doc.getObjectString(i)
        print(text)

    
if __name__ == '__main__':
    path = u'D:/OCR/报关行企业报关资料/奥特斯/8.10-2/784-24610740.pdf'
    pdf2pic(path)