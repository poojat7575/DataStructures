import pytest

from linked_list import LinkedList


@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    for i in range(1, 4):
        linked_list.insert_at_end(i)
    return linked_list


def test_init():
    assert None == LinkedList().head


def test_str(linked_list):
    assert '1 2 3 ' == linked_list.__str__()


def test_get_count(linked_list):
    assert 3 == linked_list.get_count()

def test_search_item_found(linked_list):
    assert True == linked_list.search_item(2)

def test_search_item_not_found(linked_list):
    assert False == linked_list.search_item(6)

@pytest.mark.delete
def test_delete_first(linked_list):
    linked_list.delete_first()
    assert '2 3 ' == linked_list.__str__()

@pytest.mark.delete
def test_delete_last(linked_list):
    linked_list.delete_last()
    assert '1 2 ' == linked_list.__str__()

@pytest.mark.delete
def test_delete_item(linked_list):
    linked_list.delete_item(2)
    assert '1 3 ' == linked_list.__str__()

@pytest.mark.delete
def test_delete_by_position(linked_list):
    linked_list.delete_by_position(3)
    assert '1 2 ' == linked_list.__str__()

@pytest.mark.insert
def test_insert_at_end(linked_list):
    linked_list.insert_at_end(4)
    assert '1 2 3 4 ' == linked_list.__str__()

def test_reverse(linked_list):
    linked_list.reverse()
    assert '3 2 1 ' == linked_list.__str__()

def test_get_middle_element(linked_list):
    assert 2 == linked_list.get_middle_element()

@pytest.mark.insert
def test_insert_at_start(linked_list):
    linked_list.insert_at_start(0)
    assert '0 1 2 3 ' == linked_list.__str__()


@pytest.mark.insert
def test_insert_after_item(linked_list):
    print("Inserting 4 after 3 ...")
    linked_list.insert_after_item(4, 3)
    assert '1 2 3 4 ' == linked_list.__str__()


@pytest.mark.insert
def test_insert_before_item(linked_list):
    print("Inserting 4 before 2 ...")
    linked_list.insert_before_item(4, 2)
    assert '1 4 2 3 ' == linked_list.__str__()


@pytest.mark.insert
def test_insert_at_position(linked_list):
    print("Inserting 4 at 3rd position (as 3rd node) ...")
    linked_list.insert_at_position(4, 3)
    assert '1 2 4 3 ' == linked_list.__str__()
