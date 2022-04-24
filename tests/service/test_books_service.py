from src.service.books_service import get_all_books, get_book_by_id


def test_get_all_books(mocker):
    mocker.patch('src.repository.books_repository.get_all_book_from_db',
                 return_value=
                 {
                     "data":
                         {
                             "id1":
                                 {
                                     "author":"author1",
                                     "book":"book1",
                                     "genre":["genre1"]
                                 },
                             "id2":
                                 {
                                     "author":"author2",
                                     "book":"book2",
                                     "genre":["genre2"]
                                 }
                         }
                 })
    books = get_all_books()
    assert books["data"]["id1"]["author"] == "author1"
    assert books["data"]["id1"]["book"] == "book1"
    assert books["data"]["id1"]["genre"] == ["genre1"]
    assert books["data"]["id2"]["author"] == "author2"
    assert books["data"]["id2"]["book"] == "book2"
    assert books["data"]["id2"]["genre"] == ["genre2"]


def test_get_book_by_id(mocker):
    mocker.patch('src.repository.books_repository.get_book_by_id',
                 return_value=
                 {
                     "data":
                         {
                             "author":"author1",
                             "book":"book1",
                             "genre":["genre1"]
                         },
                     "documentId":"id1"
                 }
                 )
    books = get_book_by_id("id1")
    assert books["data"]["author"] == "author1"
    assert books["data"]["book"] == "book1"
    assert books["data"]["genre"] == ["genre1"]
    assert books["documentId"]== "id1"

