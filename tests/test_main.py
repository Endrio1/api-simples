import uuid

from main import app, items

client = app.test_client()


def setup_function():
    items.clear()


def test_cria_item():
    data = {"nome": "Produto A", "descricao": "Desc", "preco": 10.5}
    resp = client.post("/items/", json=data)
    assert resp.status_code == 200
    js = resp.get_json()
    assert js["message"] == "Item criado"
    item = js["item"]
    assert item["nome"] == data["nome"]
    assert "id" in item


def test_mostrar_items():
    data1 = {"nome": "P1", "descricao": "D1", "preco": 1.0}
    data2 = {"nome": "P2", "descricao": "D2", "preco": 2.0}
    client.post("/items/", json=data1)
    client.post("/items/", json=data2)
    resp = client.get("/items/")
    assert resp.status_code == 200
    js = resp.get_json()
    assert len(js["items"]) == 2


def test_buscar_item_not_found():
    resp = client.get(f"/items/{str(uuid.uuid4())}")
    assert resp.status_code == 404


def test_atualiza_item():
    data = {"nome": "Prod", "descricao": "Desc", "preco": 5.0}
    r = client.post("/items/", json=data)
    item = r.get_json()["item"]
    item_id = item["id"]
    updated = {"id": item_id, "nome": "Prod2", "descricao": "Desc2", "preco": 6.0}
    resp = client.put(f"/items/{item_id}", json=updated)
    assert resp.status_code == 200
    js = resp.get_json()
    assert js["message"] == "Item atualizado"
    assert js["item"]["nome"] == "Prod2"


def test_apagar_item():
    data = {"nome": "Prod", "descricao": "Desc", "preco": 5.0}
    r = client.post("/items/", json=data)
    item = r.get_json()["item"]
    item_id = item["id"]
    resp = client.delete(f"/item/{item_id}")
    assert resp.status_code == 200
    js = resp.get_json()
    assert js["message"] == "Item deletado"
    assert item_id not in items
