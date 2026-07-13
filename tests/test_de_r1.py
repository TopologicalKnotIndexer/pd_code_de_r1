from copy import deepcopy
import unittest

import pd_code_sanity
from pd_code_de_r1 import de_r1


TREFOIL = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]


class ReidemeisterOneTests(unittest.TestCase):
    def test_removes_single_and_multiple_closed_r1_components(self):
        self.assertEqual(de_r1([[1, 1, 2, 2]]), [])
        self.assertEqual(de_r1([[1, 1, 2, 2], [3, 3, 4, 4]]), [])

    def test_reduced_diagram_is_stable_and_input_is_unchanged(self):
        source = deepcopy(TREFOIL)
        self.assertEqual(de_r1(source), TREFOIL)
        self.assertEqual(source, TREFOIL)

    def test_handles_disconnected_components_and_returns_valid_labels(self):
        pd_code = [*TREFOIL, [7, 7, 8, 8]]
        result = de_r1(pd_code)
        self.assertEqual(result, TREFOIL)
        self.assertTrue(pd_code_sanity.sanity(result))

    def test_rejects_structurally_invalid_code(self):
        with self.assertRaises(TypeError):
            de_r1([[1, 2, 3, 4]])


if __name__ == "__main__":
    unittest.main()
