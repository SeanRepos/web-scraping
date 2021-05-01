from main import main


class TestMain:
    def test_fetches_data(self):
        assert len(main()) != 0
