from tests.base_test_runner import LogInWithAdminTestRunner


class AddCenterWithAdminTest(LogInWithAdminTestRunner):
    VALID_LOCATION_NAME = "ТестЛокація4"
    VALID_CITY_NAME = "Київ"
    VALID_CITY_DISTRICT = "Деснянський"
    VALID_ADDRESS = "вул. Садова, 1а"
    VALID_COORDINATES = "50.4485253, 30.4735083"
    VALID_TELEPHONE = "0977777777"

    def setUp(self):
        super().setUp()
        self.add_center_popup = self.homepage.header.open_user_menu().click_add_center_pop_up
        self.add_center_popup.wait_popup_open(5)

    def test_adding_location_with_valid_data_to_list(self):
        location_popup = self.add_center_popup.step_one_container.click_add_location_button()

        location_popup.name_input_element.set_input_value(self.VALID_LOCATION_NAME)
        self.assertEqual(self.VALID_LOCATION_NAME,
                         location_popup.name_input_element.get_input_value(),
                         "Location name should be " + self.VALID_LOCATION_NAME)

        location_popup.city_dropdown_element.click_dropdown().select_item(self.VALID_CITY_NAME)
        self.assertEqual(self.VALID_CITY_NAME,
                         location_popup.city_dropdown_element.get_dropdown_selected_item_text(),
                         "Location city should be " + self.VALID_CITY_NAME)

        location_popup.district_dropdown_element.click_dropdown().select_item(self.VALID_CITY_DISTRICT)
        self.assertEqual(self.VALID_CITY_DISTRICT,
                         location_popup.district_dropdown_element.get_dropdown_selected_item_text(),
                         "Location district should be " + self.VALID_CITY_DISTRICT)

        location_popup.address_input_element.set_input_value(self.VALID_ADDRESS)
        self.assertEqual(self.VALID_ADDRESS,
                         location_popup.address_input_element.get_input_value(),
                         "Location address should be " + self.VALID_ADDRESS)

        location_popup.coordinates_input_element.set_input_value(self.VALID_COORDINATES)
        self.assertEqual(self.VALID_COORDINATES,
                         location_popup.coordinates_input_element.get_input_value(),
                         "Location coordinates should be " + self.VALID_COORDINATES)

        location_popup.telephone_input_element.set_input_value(self.VALID_TELEPHONE)
        self.assertEqual(self.VALID_TELEPHONE,
                         location_popup.telephone_input_element.get_input_value(),
                         "Location telephone should be " + self.VALID_TELEPHONE)

        location_popup.click_submit_button()

        locations_list = self.add_center_popup.step_one_container.get_locations_list_names()
        self.assertEqual(1, len(locations_list), "List of locations should have one element")
        self.assertTrue(self.VALID_LOCATION_NAME in locations_list,
                        "List of locations should have location " + self.VALID_LOCATION_NAME)
