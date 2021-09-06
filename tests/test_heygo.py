from pylenium.driver import Pylenium


def test_tour_under_15_min_has_no_book_button(py: Pylenium):
    py.visit("https://www.heygo.com/")
    starts_in_element = py.getx("//div[contains(text(), 'Starts')]").scroll_into_view()
    starts_in_text = starts_in_element.text()
    minutes = int(starts_in_text.split()[2])
    starts_in_element.parent().get("a").click(force=True)  # <a> is 0x0

    if minutes < 15:
        assert py.should().not_contain("Book")
    else:
        assert py.should().contain("Book")
