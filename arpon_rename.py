#!/usr/bin/env python
#coding: utf-8

import sys
import os
#from os import listdir
#from os import rename
#from os.path import isdir
#from os.path import isdir



def renomear(pasta,terminacao):
    """
    renomeia arquivos de um pasta, e se o arquivo nao for arquivo e sim uma pasta, entao chama recursivamente.
    """
#    print "Na pasta %s " %pasta
    for arquivo in os.listdir(pasta):
        arquivo_fp = os.path.join(pasta,arquivo)
#        print "\tabspath: %s" %os.path.abspath(arquivo)
        if os.path.isdir(arquivo_fp):            
#            print "\tpasta:'%s'" % arquivo
            renomear(os.path.abspath(arquivo_fp),terminacao)
        else:
            if not terminacao in arquivo:
                arquivo_novo = arquivo_fp+terminacao            
                os.rename(arquivo_fp, arquivo_novo)
                print "\tarquivo:'%s' -> novo: '%s'" %(arquivo_fp, arquivo_novo)

if __name__ == "__main__":
    #a pasta em que o programa fara o renomeio dos arquivos(tem q ser absoluto)
    #Ex: /home/usuario/Musicas/
    pasta_root = sys.argv[1]
    #a terminacao que sera add em cada arquivo, ex: .MP3
    terminacao = sys.argv[2]
#    print pasta_root 
#    print terminacao 
    renomear(os.path.abspath(pasta_root),terminacao)
