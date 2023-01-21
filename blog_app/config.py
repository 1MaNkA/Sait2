import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'saD:Jlkgfmskldg;hwkenjt;sohntwekiujb flwe;jgnjwegf'
    DEBUG = True