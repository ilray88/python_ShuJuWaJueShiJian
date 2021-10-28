# -*- coding: utf-8-*-
import codecs

def handleEncoding(original_file, newfile):
    # newfile=original_file[0:original_file.rfind(.)]+'_copy.csv'
    f = open(original_file, 'rb+')
    content = f.read()  # ��ȡ�ļ����ݣ�contentΪbytes���ͣ�����string����
    source_encoding = 'gbk'
    #####ȷ��encoding����
    try:
        content.decode('utf-8').encode('utf-8')
        source_encoding = 'utf-8'
    except:
        try:
            content.decode('gbk').encode('utf-8')
            source_encoding = 'gbk'
        except:
            try:
                content.decode('gb2312').encode('utf-8')
                source_encoding = 'gb2312'
            except:
                try:
                    content.decode('gb18030').encode('utf-8')
                    source_encoding = 'gb18030'
                except:
                    try:
                        content.decode('big5').encode('utf-8')
                        source_encoding = 'gb18030'
                    except:
                        content.decode('cp936').encode('utf-8')
                        source_encoding = 'cp936'
    f.close()

    #####����ȷ����encoding��ȡ�ļ����ݣ������Ϊutf-8���룺
    block_size = 4096
    with codecs.open(original_file, 'r', source_encoding) as f:
        with codecs.open(newfile, 'w', 'utf-8') as f2:
            while True:
                content = f.read(block_size)
                if not content:
                    break
                f2.write(content)
if __name__ == "__main__":
    original_file='../data_file/latlng.csv'
    newfile='../data_file/latlng_utf_8.csv'
    handleEncoding(original_file,newfile)