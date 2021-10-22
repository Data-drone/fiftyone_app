import fiftyone as fo
import fiftyone.zoo as foz


dataset=foz.load_zoo_dataset("quickstart")
session=fo.launch_app(dataset, port=8082)

session.wait()