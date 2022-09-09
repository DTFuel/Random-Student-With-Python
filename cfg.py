import configparser as cfg

Name = cfg.ConfigParser()
Name.read("name.ini", encoding="utf-8")
name = Name.items("name")
