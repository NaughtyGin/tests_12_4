import unittest
import logging
import rt_with_exceptions


logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    encoding='utf-8',
                    filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info('Тест "test_walk" выполнен успешно')
            test_obj = rt_with_exceptions.Runner('Nick', -5)
            for i in range(10):
                test_obj.walk()
            self.assertEqual(50, test_obj.distance)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            logging.info('Тест "test_run" выполнен успешно')
            test_obj = rt_with_exceptions.Runner(['Someone'], 8)
            for i in range(10):
                test_obj.run()
            self.assertEqual(100, test_obj.distance)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_not_equal(self):
        test_obj_1 = rt_with_exceptions.Runner('First', 9)  # неравенство speed => неравенство distance
        test_obj_2 = rt_with_exceptions.Runner('Second', 10)
        for i in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)

    # добавил тест на выявление ошибки в логике метода start
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_equal(self):
        test_obj_1 = rt_with_exceptions.Runner('First', 9)  # равенство speed => равенство distance
        test_obj_2 = rt_with_exceptions.Runner('Second', 9)
        for i in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        self.assertEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    unittest.main()
