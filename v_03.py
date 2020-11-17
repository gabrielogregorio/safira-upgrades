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
            data="16/11/2020",
            release="0.3",
            descricao=
                {
                    "pt-br":"Versão de lançamento",
                    "en-us":"very much",
                    "es":""
                },
            nome=
                {
                    "pt-br":"betalfa",
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
                    "pt-br":"bug None",
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
                    "pt-br":"asset",
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
                    "pt-br":"Limpar tudo",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))

        self.comandos.update(add_comandos(
            id="#2",
            titulo={
                    "pt-br":"Limpar Screen",
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
                    "pt-br":"rec1",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))

        self.recursos.update(add_recursos(
            id="#2",
            titulo={
                    "pt-br":"rec2",
                    "en-us":"",
                    "es":""
                },
            descricao={
                    "pt-br":"",
                    "en-us":"",
                    "es":""
                }))
