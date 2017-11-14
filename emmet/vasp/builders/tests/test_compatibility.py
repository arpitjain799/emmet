import unittest
import os

from emmet.vasp.builders.compatibility import MPWorksCompatibilityBuilder, \
        set_mongolike, convert_mpworks_to_atomate
from maggma.stores import JSONStore, MemoryStore
from monty.json import MontyEncoder, MontyDecoder

__author__ = "Joseph Montoya"
__email__ = "montoyjh@lbl.gov"

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
test_tasks = os.path.join(module_dir, "..","..","..", "..", "test_files", "mpworks_tasks.json")

class MPWorksCompatibilityBuilderTest(unittest.TestCase):
    def setUp(self):
        # Set up test db, set up mpsft, etc.
        self.test_tasks = JSONStore([test_tasks])
                                #,
                                    #lu_key=(me.encode, md.decode))
        self.elasticity = MemoryStore("atomate_tasks")
        self.test_tasks.connect()
        self.elasticity.connect()

    def test_builder(self):
        mpw_builder = MPWorksCompatibilityBuilder(self.test_tasks, self.elasticity, incremental=False)
        items = mpw_builder.get_items()
        processed = [mpw_builder.process_item(item) for item in items]
        mpw_builder.update_targets(processed)
    
    def test_set_mongolike(self):
        test_dict = {"stuff": {"this": 1}}
        set_mongolike(test_dict, "stuff.this", 2)
        assert test_dict["stuff"]["this"] == 2
        set_mongolike(test_dict, "new.value", 5)
        assert test_dict["new"]["value"] == 5

    def test_convert_mpworks_to_atomate(self):
        doc = self.test_tasks.collection.find_one({})
        new_doc = convert_mpworks_to_atomate(doc)
        

if __name__ == "__main__":
    unittest.main()
