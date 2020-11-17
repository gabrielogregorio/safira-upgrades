from util import *

class Upgrade:
    def __init__(self):
        self.bugs = {}
        self.comandos = {}
        self.recursos = {}
        self.upgrades = {}

        self.add_bugs()
        self.add_recursos()
        self.add_comandos()

        self.upgrade()


    def upgrade(self):
        self.upgrades.update(add_upgrade(
            data="10/11/2020",
            release="0.29",
            descricao=
                {
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                },
            nome=
                {
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                },
            bugs=self.bugs,
            comandos=self.comandos,
            recursos=self.recursos))


    def add_bugs(self):
        self.bugs.update(add_bug(
            id="#1",
            titulo={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))

        self.bugs.update(add_bug(
            id="#2",
            titulo={
                    "pt-br":"Recursos 2",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))

    def add_comandos(self):
        self.comandos.update(add_comandos(
            id="#1",
            titulo={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))

    def add_recursos(self):
        self.recursos.update(add_recursos(
            id="#1",
            titulo={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))
