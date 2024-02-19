from bson import ObjectId

from redbaby.behaviors.pyobjectid import PyObjectId
from redbaby.objectids import ObjectIdDoc


class TDoc1(ObjectIdDoc):
    attr: int


def test_id_use():
    doc = TDoc1(attr=1)
    assert doc.id is not None
    assert isinstance(doc.id, PyObjectId)
    assert len(str(doc.id)) == 24
    dumped = doc.model_dump(by_alias=True)
    assert PyObjectId(dumped["_id"]) == doc.id
    # TODO model_dump mode=python should output ObjectId, not str
    from_dumped = TDoc1(**dumped)
    assert from_dumped.id == doc.id
