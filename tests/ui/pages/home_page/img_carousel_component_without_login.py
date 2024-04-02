from tests.base_test_runner import BaseTestRunner


class TestImgCarouselWithoutLogin(BaseTestRunner):
    def setUp(self):
        super().setUp()

    def test_check_that_slick_dots_container_is_centered(self):
        self.assertIn("center", self.homepage.carousel_img_component.slick_dots_container.value_of_css_property("justify-content"))
