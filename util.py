
def add_upgrade(data:str, release:str, descricao:str, nome:str, bugs:dict, comandos:dict, recursos:dict) -> dict:

    return {
        release:
        {
        "nome":nome,
        "data":data,
        "descricao":descricao,
        "upgrades":{
            "bugs":bugs,
            "novos recursos":recursos,
            "novos comandos":comandos
            }
        }
    }

def add_bug(id:str, titulo:dict, descricao:dict) -> dict:
    return {id: {
        "titulo": titulo,
        "descricao": descricao
    }}

def add_comandos(id:str, titulo:dict, descricao:dict) -> dict:
    return {id: {
        "titulo": titulo,
        "descricao": descricao
    }}

def add_recursos(id:str, titulo:dict, descricao:dict) -> dict:
    return {id: {
        "titulo": titulo,
        "descricao": descricao
    }}
