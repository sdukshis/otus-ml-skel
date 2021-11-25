from fastapi.testclient import TestClient

from titanic.data.make_dataset import load_titanic
from titanic.models.train import make_baseline_model

from .main import app, Model

client = TestClient(app)


def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Green"


def test_predict():
    dataset = load_titanic()
    y = dataset["Survived"]
    X = dataset.drop("Survived", axis=1)
    pipeline = make_baseline_model()
    pipeline.fit(X, y)
    Model.pipeline = pipeline

    passenger = {
        "Name": "John",
        "Pclass": 1,
        "Sex": "male",
        "Age": 27,
        "Embarked": "S",
        "Fare": 100,
        "SibSp": 0,
        "Parch": 0,
        "Ticket": "C101",
    }
    response = client.post("/predict?passenger_id=1", json=passenger)
    assert response.status_code == 200
    assert response.json() == {"passenger_id": 1, "survived": 0}
